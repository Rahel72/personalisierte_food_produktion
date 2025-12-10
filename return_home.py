from dobotapi import Dobot
import time

# Warte kurz damit Verbindung stabil ist
time.sleep(0.2)

port = "/dev/ttyACM0"
device = Dobot(port=port)
device.connect()

home = (261.16, -106.34, 104.47, -22.16)
path_from_white = [
    (262.02, 125.08, 128.12, 25.51),
    (261.16, -106.34, 104.47, -22.16),
]
path_from_green = [
    (161.57, 242.05, 109.83, 56.27),
    (279.85, 65.00, 121.98, 13.07),
    (261.16, -106.34, 104.47, -22.16),
]

try:
    print("🚀 Fahre zurück zu Home...")
    # Fahre beide Wege (es ist ok wenn einer nicht nötig ist)
    for pos in path_from_white:
        device.move_to(*pos)
        time.sleep(0.3)
    print("✓ Home erreicht")
finally:
    device.close()