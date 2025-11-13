from serial.tools import list_ports
from serial import Serial, SerialException
import time
import dobotapi as bot

# -------------------------------
# 1) Port-Finder
# -------------------------------
def find_dobot_port():
    for p in list_ports.comports():
        desc = (p.description or "").upper()
        if any(k in desc for k in ("CP210", "USB", "UART", "SLAB")):
            return p.device
    return None

def ensure_port_openable(port):
    if port is None:
        raise RuntimeError("Kein Dobot-Port gefunden. Treiber/Kabel prüfen.")
    try:
        s = Serial(port=port, baudrate=115200, timeout=0.1)
        s.close()
    except SerialException as e:
        raise RuntimeError(f"Port {port} lässt sich nicht öffnen: {e}")

# -------------------------------
# 2) IR-Sensor Reader (versucht mehrere API-Varianten)
#    Rückgabe: True=BLOCKED, False=clear, None=unbekannt
# -------------------------------
def read_ir(arm, fallback_pin=1):
    # Variante A: conveyor_belt.get_ir()
    try:
        if hasattr(arm, "conveyor_belt") and hasattr(arm.conveyor_belt, "get_ir"):
            v = arm.conveyor_belt.get_ir()
            # viele Implementierungen geben 1/0 zurück
            return bool(int(v))
    except Exception:
        pass

    # Variante B: arm.get_ir() / arm.get_ir_sensor()
    for name in ("get_ir", "get_ir_sensor"):
        try:
            if hasattr(arm, name):
                v = getattr(arm, name)()
                return bool(int(v))
        except Exception:
            pass

    # Variante C: digitale Eingänge (wenn IR an DI/GP angeschlossen ist)
    # Häufig GP1/DI1 -> fallback_pin=1
    for name in ("get_digital_input", "get_io_digital"):
        try:
            if hasattr(arm, name):
                v = getattr(arm, name)(fallback_pin)  # erwartet 0/1 oder True/False
                return bool(int(v))
        except Exception:
            pass

    # Variante D: gesamter IO-State als Dict
    for name in ("get_io_state", "get_io", "io_state"):
        try:
            if hasattr(arm, name):
                state = getattr(arm, name)()
                # Versuche typische Keys
                for k in ("DI1", "DI01", "IR", "IR1", "GP1"):
                    if isinstance(state, dict) and k in state:
                        return bool(int(state[k]))
        except Exception:
            pass

    return None  # keine bekannte Methode gefunden

# -------------------------------
# 3) Hauptprogramm
# -------------------------------
def main(run_conveyor=False, conveyor_speed=0.3, poll_hz=10, debounce_samples=3):
    port = find_dobot_port()
    print("Gefundener Port:", port)
    ensure_port_openable(port)

    arm = bot.Dobot(port=port)
    arm.connect()
    print("✅ Verbunden.")

    # OPTIONAL: Förderband starten
    if run_conveyor and hasattr(arm, "conveyor_belt"):
        try:
            arm.conveyor_belt.move(speed=conveyor_speed)
            print(f"Conveyor ON @ speed={conveyor_speed}")
        except Exception as e:
            print("Hinweis: Conveyor ließ sich nicht starten:", e)

    try:
        interval = 1.0 / max(1, poll_hz)
        history = []

        print("Starte IR-Polling. Abbruch mit Ctrl+C.")
        while True:
            v = read_ir(arm)  # True=BLOCKED, False=clear, None=unbekannt
            history.append(v)
            if len(history) > debounce_samples:
                history.pop(0)

            # einfache Entprellung: n identische Werte in Folge
            stable = (len(history) == debounce_samples) and all(x == history[0] for x in history)

            if v is None:
                print("IR: unbekannt (keine passende API gefunden) — bitte Pins/Lib prüfen")
            else:
                if stable:
                    print("IR:", "BLOCKED" if v else "clear")
                else:
                    # noch instabil – leiser ausgeben
                    print("IR (unstable):", "BLOCKED" if v else "clear")

            time.sleep(interval)

    except KeyboardInterrupt:
        print("\n⏹️  Stop durch Benutzer.")
    finally:
        # Conveyor stoppen (falls vorhanden)
        if hasattr(arm, "conveyor_belt"):
            try:
                arm.conveyor_belt.idle()
            except Exception:
                pass
        try:
            arm.close()
        except Exception:
            pass
        print("Verbindung geschlossen.")

if __name__ == "__main__":
    # run_conveyor=True, wenn du beim Testen etwas durchlaufen lassen möchtest
    main(run_conveyor=False, conveyor_speed=0.3, poll_hz=10, debounce_samples=3)

