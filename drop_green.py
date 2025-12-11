from dobotapi import Dobot
import time

# Warte kurz damit Verbindung stabil ist
time.sleep(0.1)

port = "/dev/ttyACM0"
device = Dobot(port=port)
device.connect()

path_to_green = [
    (268.60, -113.15, 35.41, -22.85),
    (263.27, -99.34, 117.24, -20.68),
    (218.25, 201.19, 105.51, 42.67),
    (162.36, 243.24, 99.77, 56.27),
    (173.22, 260.28, 0.65, 56.35),
]

try:
    print("🚀 Fahre zur grünen Plattform...")
    for pos in path_to_green[1:]:
        device.move_to(*pos)
        time.sleep(0.3)
    
    print("🖐️  Gripper öffnet...")
    device.gripper.open()
    time.sleep(0.3)

    print ("⬆️ Fahre hoch...")
    device.move_to(173.22, 260.28, 90.65, 56.35)
    time.sleep(0.1)
    print("✓ Objekt auf grüner Plattform abgelegt")
finally:
    device.close()