from dobotapi import Dobot
import time

# Warte kurz damit Verbindung stabil ist
time.sleep(0.2)

port = "/dev/ttyACM0"
device = Dobot(port=port)
device.connect()

path_to_white = [
    (268.60, -113.15, 35.41, -22.85),
    (258.85, -113.15, 118.51, -23.62),
    (215.74, 179.65, 121.74, 39.78),
    (38.59, 280.43, 112.21, 82.16),
    (33.23, 299.73, 1.28, 83.67),
]

try:
    print("🚀 Fahre zur weissen Plattform...")
    for pos in path_to_white[1:]:
        device.move_to(*pos)
        time.sleep(0.3)
    
    print("🖐️  Gripper öffnet...")
    device.gripper.open()
    time.sleep(0.3)
    print ("⬆️ Fahre hoch...")
    device.move_to(33.23, 299.73, 80.28, 83.67)
    time.sleep(0.3)
    print("✓ Objekt auf weisser Plattform abgelegt")
finally:
    device.close()