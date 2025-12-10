from dobotapi import Dobot
import time

# Warte kurz damit Verbindung stabil ist
time.sleep(0.5)

try:
    device = Dobot(port="/dev/ttyACM0")
    device.connect()
    
    print("🤖 Pick startet...")
    time.sleep(1)
    
    device.gripper.open()
    time.sleep(1)
    
    print("🚀 Fahre zur Pickup-Station...")
    device.move_to(268.60, -113.15, 35.41, -22.85)
    time.sleep(2)
    
    print("✋ Gripper schliesst...")
    device.gripper.close()
    time.sleep(1)
    
    print("✓ Objekt gegriffen - Pick fertig")
    device.close()

except Exception as e:
    print(f"✗ Fehler: {e}")
    try:
        device.close()
    except:
        pass