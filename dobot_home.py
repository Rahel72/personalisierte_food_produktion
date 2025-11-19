from dobotapi import Dobot

# Verbinde mit Dobot
device = Dobot(port="/dev/ttyACM0")
device.connect()
print("✓ Verbunden")


# Home - Fahre in Homeposition
print("\n🏠 Fahre in Home-Position...")
device.move_to(282.21, -52.48, 113.57, -10.54)
print("✓ Home-Position erreicht")


# Disconnect
device.close()
print("✓ Fertig")