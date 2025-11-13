from dobotapi import Dobot
import time


port = "/dev/ttyACM0"
device = Dobot(port=port)

# Clear any existing alarms
device.clear_alarms_alarms()

# Define the x, y, z, r coordinates for various positions
home_position = (160.0, 0.0, 80.0, 0.0)

try:
    # Aktuelle Position holen
    pose = device.get_pose().position  # Nicht get_pose() - die Methode heißt pose()
    print(f"Aktuelle Position: x={pose[0]:.2f}, y={pose[1]:.2f}, z={pose[2]:.2f}, r={pose[3]:.2f}")
    device.move_to(*home_position)
    pose = device.get_pose().position  # Nicht get_pose() - die Methode heißt pose()

    # Bewegungen ausführen
    x, y, z, r = pose[0:4]
    
    # 20mm in X-Richtung
    device.move_to(177.75, -60.22, 147.45, -18.71)
    time.sleep(1)


    # device.move_to(222.35, -75.21, 45.82, -18.69)
    device.clear_alarms()

    # Function to attach the gripper to the claw
    device.grip(True)  # Close gripper (True = close, False = open)


    positions = [   (209.66, -76.80, 58.67, -20.12),
                    (202.99, 33.30, 131.73, 9.32),
                    (124.16, 166.65, 132.18, 53.31),
                    (140.34, 165.24, -2.08, 49.66), 
                    (2.46, 190.08, -3.34, 89.26),
                    (110.30, 117.35, 169.38, 46.78),
                    (201.18, -82.57, 147.18, -22.31),
                    (218.03, -68.18, 54.70, -17.36)]
    
    for pos in positions:
        device.move_to(*pos)
        time.sleep(1)

    # Function to release the gripper from the claw
    device.grip(False)  # Open gripper 
    device.suck(False)


    # # Zurück zur Startposition
    # device.move_to(x, y, z, r+5)
    # time.sleep(1)
    
    # # 20mm in Y-Richtung
    # device.move_to(x, y + 20, z, r)
    # time.sleep(1)
    
    # # Zurück zur Startposition
    # device.move_to(x, y, z, r)

finally:
    # Verbindung schließen
    device.close()



