from dobotapi import Dobot
import time

port = "/dev/ttyACM0"
device = Dobot(port=port)

# Clear any existing alarms
# device.clear_alarms()
# device.set_ir()
device.ir_toggle(True)


pose = device.get_ir()  # Nicht get_pose() - die Methode heißt pose()
print(f"IR Sensor Wert: {pose}")

while True:
    # time.sleep(1)
    old_pose = pose
    pose = device.get_ir()  # Nicht get_pose() - die Methode heißt pose()
    if pose != old_pose: 
        print(f"IR Sensor Wert: {pose}")
        if pose:
            print("Objekt erkannt")
            

        