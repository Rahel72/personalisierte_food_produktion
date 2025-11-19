from serial.tools import list_ports
from dobotapi import Dobot
import time

port = "/dev/ttyACM0"
device = Dobot(port=port)
device.connect()
print("✓ Verbunden")


# Starte Förderband
device.conveyor_belt.move(speed=0.5)  
print("✓ Förderband läuft")

# Warte 10 Sekunden
time.sleep(10)


# Stoppe Förderband
device.conveyor_belt.idle()  
print("✓ Förderband gestoppt")


# Schließe Verbindung
device.close()
print("✓ Fertig")

# Geschwindigkeit:
# 0.5 = halbe Geschwindigkeit
# 1.0 = maximale Geschwindigkeit
# -0.5 = halbe Geschwindigkeit in die andere Richtung
# -1.0 = maximale Geschwindigkeit rückwärts