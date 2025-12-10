import time
from dobotapi import Dobot
import sys

# Konfiguration
PORT = "/dev/ttyACM0"
CONVEYOR_SPEED = 0.5 # Geschwindigkeit des Förderbands

def connect_dobot():
    """Stellt Verbindung zum Dobot her und gibt das Gerät zurück."""
    try:
        device = Dobot(port=PORT)
        device.connect()
        device.ir_toggle(enable=True) # IR Sensor aktivieren
        return device
    except Exception as e:
        print(f"Fehler beim Verbinden mit Dobot: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    device = None
    try:
        device = connect_dobot()
        
        print(f"🟢 Förderband startet mit Geschwindigkeit {CONVEYOR_SPEED}...")
        device.conveyor_belt.move(speed=CONVEYOR_SPEED)
        
        # Warte, bis Objekt erkannt wird (get_ir() == True)
        # HINWEIS: Je nach Verkabelung ist True oder False das Signal für "Objekt da".
        # Wir nehmen an, True bedeutet "Objekt erkannt".
        while device.get_ir() == False:
            time.sleep(0.05)
            
        print("🔴 STOPP - Objekt erkannt")
        device.conveyor_belt.idle() # Förderband stoppen
        
        # Das Skript beendet sich jetzt, damit Node-RED zum Roboter-Schritt übergeht.
        
    except Exception as e:
        print(f"✗ Fehler: {e}", file=sys.stderr)
        sys.exit(1)
        
    finally:
        if device:
            device.close()