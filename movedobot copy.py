from dobotapi import Dobot
import time

port = "/dev/ttyACM0"
device = Dobot(port=port)
device.connect()
print("✓ Verbunden\n")

# ============================================
# HOME POSITION
# ============================================
home = (282.21, -52.48, 113.57, -10.54)

# ============================================
# WEIßE PLATTFORM - ALLE ZWISCHENPUNKTE
# ============================================
path_to_white = [
    (291.80, -3.51, 35.19, -0.69),      # Pickup-Station
    (274.16, 10.26, 125.30, 2.14),        # Weg 1
    (173.75, 204.59, 133.82, 49.66),      # Weg 2
    (-23.54, 239.53, 126.05, 95.61),      # Weg 3
    (-15.02, 242.31, -12.87, 93.55),      # Drop weiß
]

path_from_white = [
    (-20.05, 234.05, 123.08, 94.90),      # Zurück Weg 1
    (120.90, 239.74, 129.67, 63.24),      # Zurück Weg 2
    (221.89, 140.38, 133.99, 32.32),      # Zurück Weg 3
    (282.21, -52.48, 113.57, -10.54),     # Home
]

# ============================================
# GRÜNE PLATTFORM - ALLE ZWISCHENPUNKTE
# ============================================
path_to_green = [
    (291.80, -3.51, 35.19, -0.69),      # Pickup-Station
    (258.39, -59.01, 146.38, -12.67),     # Weg 1
    (123.12, 261.97, 122.72, 65.02),      # Weg 2
    (90.83, 303.20, -9.65, 73.33),        # Drop grün
]

path_from_green = [
    (72.44, 298.68, 103.47, 76.56),       # Zurück Weg 1
    (249.38, 102.76, 115.87, 22.59),      # Zurück Weg 2
    (282.21, -52.48, 113.57, -10.54),     # Home
]

# ============================================
# FUNKTIONEN
# ============================================

def pickup_and_go_to_white():
    print("🚀 Fahre zur Pickup-Station...")
    device.move_to(*path_to_white[0])  # Nur erste Position (Pickup)
    time.sleep(1)
    
    print("✋ Gripper schließt...")
    device.gripper.close()
    time.sleep(1)
    
    print("🚀 Fahre zur weißen Plattform...")
    for pos in path_to_white[1:]:  # Ab Position 2 fahren
        device.move_to(*pos)
        time.sleep(1)
    print("✓ Weiße Plattform erreicht")

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
    
    print("✋ Gripper schließt...")
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