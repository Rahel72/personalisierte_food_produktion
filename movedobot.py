from dobotapi import Dobot
import time


port = "/dev/ttyACM0"
device = Dobot(port=port)
device.connect()

# Define the x, y, z, r coordinates for various positions
home_position = (282.21, -52.48, 113.57, -10.54)

try:
    # Aktuelle Position holen
    pose = device.get_pose().position  # Nicht get_pose() - die Methode heißt pose()
    print(f"Aktuelle Position: x={pose[0]:.2f}, y={pose[1]:.2f}, z={pose[2]:.2f}, r={pose[3]:.2f}")
    device.move_to(*home_position)
    pose = device.get_pose().position  # Nicht get_pose() - die Methode heißt pose()

    # Bewegungen ausführen
    x, y, z, r = pose[0:4]
    
    # 20mm in X-Richtung
    device.move_to(262.21, -52.48, 113.57, -10.54)
    time.sleep(1)

finally:
    # Verbindung schließen
    device.close()



