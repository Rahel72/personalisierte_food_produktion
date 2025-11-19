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
SENSOR_INITIALIZED = False

def initialize_sensor(arm):
    """Aktiviert den IR-Sensor einmalig"""
    global SENSOR_INITIALIZED
    if not SENSOR_INITIALIZED:
        try:
            arm.ir_toggle(enable=True)
            SENSOR_INITIALIZED = True
        except Exception as e:
            raise RuntimeError(f"Sensor-Aktivierung fehlgeschlagen: {e}")

def read_ir(arm, fallback_pin=1):
    """
    Liest den IR-Sensor aus.
    
    Rückgabe:
    - True = BLOCKED (Objekt erkannt)
    - False = CLEAR (kein Objekt)
    - None = Fehler
    """
    try:
        initialize_sensor(arm)
        result = arm.get_ir()
        return result
    except Exception as e:
        print(f"[ERROR] IR-Sensor Fehler: {e}")
        return None  

# -------------------------------
#  Hauptprogramm
# -------------------------------
def main(run_conveyor=False, conveyor_speed=0.3, poll_hz=10, debounce_samples=3):
    port = find_dobot_port()
    print(f"Gefundener Port: {port}")
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
            print(f"Hinweis: Conveyor ließ sich nicht starten:, {e}")
    # Starte IR-Polling
    try:
        interval = 1.0 / max(1, poll_hz)
        history = []

        print("Starte IR-Polling. Abbruch mit Ctrl+C.")
        while True:
            v = read_ir(arm)  # True=BLOCKED, False=clear, None=unbekannt
            history.append(v)

            if len(history) > debounce_samples:
                history.pop(0)

            # Prüfe Stabilität
            stable = (len(history) == debounce_samples) and all(x == history[0] for x in history)
            
            if v is None:
                print("IR: unbekannt (keine passende API gefunden)")
            else:
                status = "BLOCKED" if v else "CLEAR"
                stability = "" if stable else "(unstable)"
                print(f"IR {stability}: {status}")
            
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\n⏹️  Stop durch Benutzer.")
    finally:
        # Conveyor stoppen (falls vorhanden)
        if run_conveyor and hasattr(arm, "conveyor_belt"):
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

