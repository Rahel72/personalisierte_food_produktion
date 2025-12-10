from dobotapi import Dobot
import time

port = "/dev/ttyACM0"
device = Dobot(port=port)
device.connect()

home = (261.16, -106.34, 104.47, -22.16)
path_to_white = [
    (268.60, -113.15, 35.41, -22.85),
    (258.85, -113.15, 118.51, -23.62),
    (215.74, 179.65, 121.74, 39.78),
    (38.59, 280.43, 112.21, 82.16),
    (33.23, 299.73, 1.28, 83.67),
]
path_to_green = [
    (268.60, -113.15, 35.41, -22.85),
    (263.27, -99.34, 117.24, -20.68),
    (218.25, 201.19, 105.51, 42.67),
    (162.36, 243.24, 99.77, 56.27),
    (173.22, 260.28, 0.65, 56.35),
]

try:
    device.gripper.open()
    time.sleep(1)
    print("🚀 Fahre zur Pickup-Station...")
    device.move_to(*path_to_white[0])
    time.sleep(1)
    
    print("✋ Gripper schliesst...")
    device.gripper.close()
    time.sleep(1)
    print("✓ Objekt gegriffen")
finally:
    device.close()