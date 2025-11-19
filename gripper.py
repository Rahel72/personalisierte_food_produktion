from dobotapi import Dobot
import time

port = "/dev/ttyACM0"
device = Dobot(port=port)
device.connect()
print("✓ Verbunden")


# Gripper öffnen 
device.gripper.open()
print("✓ Gripper offen")
time.sleep(2)


# Gripper schliessen
device.gripper.close()
print("✓ Gripper geschlossen")
time.sleep(2)

# Gripper öffnen
device.gripper.open()
print("✓ Gripper offen")
time.sleep(2)

# Disconnect
device.close()
print("\n✓ Fertig")