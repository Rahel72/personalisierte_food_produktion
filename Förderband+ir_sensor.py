from dobotapi import Dobot
import time

# Warte kurz damit Verbindung stabil ist
time.sleep(0.5)

device = Dobot(port="/dev/ttyACM0")
device.connect()
device.ir_toggle(enable=True)

print("🟢 Förderband läuft...")
device.conveyor_belt.move(speed=0.5)

# Warte bis Objekt erkannt
while device.get_ir() == False:
    time.sleep(0.1)

print("🔴 Objekt erkannt - STOP")
device.conveyor_belt.idle()

# Warte bis Objekt weg
while device.get_ir() == True:
    time.sleep(0.1)

print("✓ Fertig - pick.py startet jetzt")
device.close()