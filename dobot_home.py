from dobotapi import Dobot

# Verbinde mit Dobot
device = Dobot(port="/dev/ttyACM0")
device.connect()
print("✓ Verbunden")


# Home - Fahre in Homeposition
print("\n🏠 Fahre in Home-Position...")
device.move_to(261.16, -106.34, 104.47, -22.16)
print("✓ Home-Position erreicht")


# Disconnect
device.close()
print("✓ Fertig")