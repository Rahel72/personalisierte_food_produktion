from pydobotplus import Dobot
import time


port = "/dev/ttyACM0"
device = Dobot(port=port)

# # Clear any existing alarms
# device.clear_alarms()

# Pumpe muss am GP1 angeschlossen sein!
# Function to release the gripper from the claw 
device.grip(False)  # Open gripper (True = close, False = open)
time.sleep(2)
device.grip(True)
time.sleep(2)

device.suck(False)
device.close() # Open gripper
