from dobotapi import Dobot
import time


port = "/dev/ttyACM0"
device = Dobot(port=port)

# Clear any existing alarms
# device.clear_alarms()

# Define the x, y, z, r coordinates for various positions
home_position = (160.0, 0.0, 80.0, 0.0)

# Aktuelle Position holen
pose = device.get_pose().position  # Nicht get_pose() - die Methode heißt pose()
# print(f"Aktuelle Position: x={pose[0]:.2f}, y={pose[1]:.2f}, z={pose[2]:.2f}, r={pose[3]:.2f}")
# device.move_to(*home_position)
while True:
    # time.sleep(1)
    old_pose = pose
    pose = device.get_pose().position  # Nicht get_pose() - die Methode heißt pose()
    if pose != old_pose:
        print(f" ({pose[0]:.2f}, {pose[1]:.2f}, {pose[2]:.2f}, {pose[3]:.2f}),")