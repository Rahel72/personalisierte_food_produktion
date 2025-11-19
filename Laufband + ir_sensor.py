from dobotapi import Dobot
import time

# Verbinde
device = Dobot(port="/dev/ttyACM0")
device.connect()
device.ir_toggle(enable=True)

print("✓ Start\n")

# Endlosschleife
while True:
    # Starte Förderband
    print("🟢 Förderband läuft...")
    device.conveyor_belt.move(speed=0.5)
    
    # Warte bis Objekt erkannt
    while device.get_ir() == False:
        time.sleep(0.1)
    
    # Stoppe Förderband
    print("🔴 STOPP - Objekt erkannt")
    device.conveyor_belt.idle()
    
    # Warte bis Objekt weg
    while device.get_ir() == True:
        time.sleep(0.1)
    
    print("✓ Objekt weg - Neustart\n")