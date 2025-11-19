from dobotapi import Dobot
import time


port = "/dev/ttyACM0"
device = Dobot(port=port)
device.connect()

# Clear any existing alarms
# device.clear_alarms_alarms()

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
    device.move_to(281.21, -52.48, 113.57, -10.54)
    time.sleep(1)


    # device.move_to(222.35, -75.21, 45.82, -18.69)
    # device.clear_alarms()

    # Function to attach the gripper to the claw
    # device.grip(True)  # Close gripper (True = close, False = open)


    positions = [   (282.21, -52.48, 113.57, -10.54),
                    (282.21, -51.48, 113.57, -10.54),
                    (282.21, -53.48, 113.57, -10.54)]
    
    for pos in positions:
        device.move_to(*pos)
        time.sleep(1)

    # Function to release the gripper from the claw
    # device.grip(False)  # Open gripper 
    # device.suck(False)


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



