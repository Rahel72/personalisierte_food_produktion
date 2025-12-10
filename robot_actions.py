import sys
import time
from dobotapi import Dobot

# Konfiguration
PORT = "/dev/ttyACM0"
HOME = (261.16, -106.34, 104.47, -22.16)

# Pfad zur weissen Plattform (dein path_to_white)
PATH_TO_WHITE = [
    (268.60, -113.15, 35.41, -22.85),
    (258.85, -113.15, 118.51, -23.62),
    (215.74, 179.65, 121.74, 39.78),
    (38.59, 280.43, 112.21, 82.16),
    (33.23, 299.73, 1.28, 83.67),
]

# Pfad zur grünen Plattform (dein path_to_green)
PATH_TO_GREEN = [
    (268.60, -113.15, 35.41, -22.85),
    (263.27, -99.34, 117.24, -20.68),
    (218.25, 201.19, 105.51, 42.67),
    (162.36, 243.24, 99.77, 56.27),
    (173.22, 260.28, 0.65, 56.35),
]

def connect_dobot():
    """Stellt Verbindung zum Dobot her und gibt das Gerät zurück."""
    try:
        device = Dobot(port=PORT)
        device.connect()
        return device
    except Exception as e:
        print(f"Fehler beim Verbinden mit Dobot: {e}", file=sys.stderr)
        sys.exit(1)

def pick_up(device):
    """Fährt zur Aufnahme-Position, schließt den Greifer."""
    print("🤖 Aktion: PICK")
    device.gripper.open()
    time.sleep(0.5)
    device.move_to(*PATH_TO_WHITE[0]) # Startposition des Picken-Vorgangs
    time.sleep(0.5)
    device.gripper.close()
    time.sleep(0.5)
    device.move_to(*PATH_TO_WHITE[1]) # Auf sichere Höhe fahren
    print("✓ Objekt gegriffen")

def drop_object(device, target_path, target_name):
    """Fährt zur Ziel-Plattform (Grün/Weiss) und öffnet den Greifer."""
    print(f"🤖 Aktion: DROP auf {target_name}")
    
    # Bewege entlang des Pfades zur Ablageposition
    for pos in target_path[1:]:
        device.move_to(*pos)
        # time.sleep(0.5) # Optional, falls der Roboter zu schnell ist
        
    device.gripper.open()
    time.sleep(0.5)
    print(f"✓ Objekt auf {target_name} abgelegt")

def go_home(device):
    """Fährt in die Home-Position zurück und öffnet den Greifer."""
    print("🤖 Aktion: HOME")
    device.move_to(*HOME)
    time.sleep(0.5)
    device.gripper.open()
    time.sleep(0.5)
    print("✓ Home erreicht & Greifer geöffnet")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Fehler: Kommando-Argument fehlt (HOME, PICK, DROP_W, DROP_G)", file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1].upper()
    device = None
    
    try:
        device = connect_dobot()
        
        if command == "HOME":
            go_home(device)
        elif command == "PICK":
            pick_up(device)
        elif command == "DROP_W":
            drop_object(device, PATH_TO_WHITE, "WEISS")
        elif command == "DROP_G":
            drop_object(device, PATH_TO_GREEN, "GRÜN")
        else:
            print(f"Unbekanntes Kommando: {command}", file=sys.stderr)
            sys.exit(1)
            
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}", file=sys.stderr)
        sys.exit(1)
        
    finally:
        # Nur schließen, wenn eine Verbindung aufgebaut wurde
        if device:
            device.close()