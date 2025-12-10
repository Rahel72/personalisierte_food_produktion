from dobotapi import Dobot
import time

port = "/dev/ttyACM0"
device = Dobot(port=port)
device.connect()
print("✓ Verbunden\n")

# ============================================
# HOME POSITION
# ============================================
home = (261.16, -106.34, 104.47, -22.16)

# ============================================
# WEIßE PLATTFORM - ALLE ZWISCHENPUNKTE
# ============================================
path_to_white = [
    (268.60, -113.15, 35.41, -22.85),      # Pickup-Station
    (258.85, -113.15, 118.51, -23.62),        # Weg 1
    (215.74, 179.65, 121.74, 39.78),      # Weg 2
    (38.59, 280.43, 112.21, 82.16),      # Weg 3
    (33.23, 299.73, 1.28, 83.67),       # Drop weiß 2
]

path_from_white = [
    (262.02, 125.08, 128.12, 25.51),      # Zurück Weg 1
    (261.16, -106.34, 104.47, -22.16),     # Home
]

# ============================================
# GRÜNE PLATTFORM - ALLE ZWISCHENPUNKTE
# ============================================
path_to_green = [
    (268.60, -113.15, 35.41, -22.85),      # Pickup-Station
    (263.27, -99.34, 117.24, -20.68),     # Weg 1
    (218.25, 201.19, 105.51, 42.67),      # Weg 2
    (162.36, 243.24, 99.77, 56.27),      # Weg 3
    (173.22, 260.28, 0.65, 56.35),        # Drop grün
]

path_from_green = [
    (161.57, 242.05, 109.83, 56.27),       # Zurück Weg 1
    (279.85, 65.00, 121.98, 13.07),      # Zurück Weg 2
    (261.16, -106.34, 104.47, -22.16),     # Home
]

# ============================================
# FUNKTIONEN
# ============================================

def pickup_and_go_to_white():
    print("🚀 Fahre zur Pickup-Station...")
    device.move_to(*path_to_white[0])  # Nur erste Position (Pickup)
    time.sleep(1)
    
    print("✋ Gripper schliesst...")
    device.gripper.close()
    time.sleep(1)
    
    print("🚀 Fahre zur weissen Plattform...")
    for pos in path_to_white[1:]:  # Ab Position 2 fahren
        device.move_to(*pos)
        time.sleep(1)
    print("✓ Weisse Plattform erreicht")

def open_and_return_from_white():
    print("🖐️  Gripper öffnet...")
    device.gripper.open()
    time.sleep(1)
    
    print("🚀 Fahre zurück zu Home...")
    for pos in path_from_white:
        device.move_to(*pos)
        time.sleep(1)
    print("✓ Home erreicht")

def pickup_and_go_to_green():
    print("🚀 Fahre zur Pickup-Station...")
    device.move_to(*path_to_green[0])  # Nur erste Position (Pickup)
    time.sleep(1)
    
    print("✋ Gripper schliesst...")
    device.gripper.close()
    time.sleep(1)
    
    print("🚀 Fahre zur grünen Plattform...")
    for pos in path_to_green[1:]:  # Ab Position 2 fahren
        device.move_to(*pos)
        time.sleep(1)
    print("✓ Grüne Plattform erreicht")

def open_and_return_from_green():
    print("🖐️  Gripper öffnet...")
    device.gripper.open()
    time.sleep(1)
    
    print("🚀 Fahre zurück zu Home...")
    for pos in path_from_green:
        device.move_to(*pos)
        time.sleep(1)
    print("✓ Home erreicht")

# ============================================
# HAUPTSCHLEIFE
# ============================================

try:
    counter = 0
    while True:
        counter += 1
        print(f"\n{'='*50}")
        print(f"ZYKLUS {counter}")
        print(f"{'='*50}\n")
        
        # Gehe zu Home
        print("🏠 Fahre zu Home...")
        device.move_to(*home)
        time.sleep(1)
        print("🖐️  Gripper öffnet...")
        device.gripper.open()
        time.sleep(1)
        
        # 1. Objekt auf weiß
        print("\n--- 1. Objekt auf weiß ---")
        pickup_and_go_to_white()
        open_and_return_from_white()
        
        # 2. Objekt auf weiß
        print("\n--- 2. Objekt auf weiß ---")
        pickup_and_go_to_white()
        open_and_return_from_white()
        
        # 3. Objekt auf grün
        print("\n--- 3. Objekt auf grün ---")
        pickup_and_go_to_green()
        open_and_return_from_green()
        
        print(f"\n✓ Zyklus {counter} abgeschlossen!\n")

except KeyboardInterrupt:
    print("\n\n⏹️  Gestoppt durch Benutzer")
finally:
    device.close()
    print("✓ Fertig")