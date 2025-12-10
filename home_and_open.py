from dobotapi import Dobot
import time

# Warte kurz damit Verbindung stabil ist
time.sleep(0.2)

port = "/dev/ttyACM0"
device = Dobot(port=port)
device.connect()

home = (261.16, -106.34, 104.47, -22.16)

try:
    print("🏠 Fahre zu Home...")
    device.move_to(*home)
    time.sleep(0.3)
    
    print("🖐️  Gripper öffnet...")
    device.gripper.open()
    time.sleep(0.3)
    print("✓ Bereit für nächstes Objekt")  
    
finally:
    device.close()