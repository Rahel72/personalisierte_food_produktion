from serial.tools import list_ports
from dobotapi import Dobot

port = "/dev/ttyACM0"
device = Dobot(port=port)



# Control the conveyor belt
device.conveyor_belt.enable()
device.conveyor_belt.set_speed(speed=0.9, direction=-1)
import time
time.sleep(2)
device.conveyor_belt.disable()

device.close()






# from time import sleep
# from dobotapi import Dobot

# # -------------------------------
# # 1) Port-Finder
# # -------------------------------

# Dobot = Dobot()
# Dobot.connect()

# def find_dobot_port():
#     Dobot = Dobot()  # Mit Einrückung (4 oder 8 Leerzeichen)
#     Dobot.connect()
#     return port

# # port = "/dev/ttyACM0"
# # bot = Dobot(port=port)

# # Speed can range from -1.0 to 1.0 (negative values move the belt in the opposite direction)
# Dobot.conveyor_belt.move(speed=1.0, direction=1) # Start the conveyor belt moving forward at full speed

# sleep(5) # Wait for 5 seconds

# Dobot.conveyor_belt.idle() # Stop the conveyor belt

# Dobot.close()