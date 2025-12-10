from dobotapi import Dobot
import time
import signal
import sys

# ============================================
# Signal Handler - für sauberes Beenden
# ============================================
def signal_handler(sig, frame):
    """Wird aufgerufen wenn Ctrl+C gedrückt wird"""
    print("\n\n⏹️  STOPP durch Signal empfangen")
    print("🔴 Stoppe Förderband...")
    try:
        device.conveyor_belt.idle()
        device.close()
    except:
        pass
    print("✓ Programm beendet")
    sys.exit(0)

# Registriere Signal Handler
signal.signal(signal.SIGINT, signal_handler)  # Ctrl+C
signal.signal(signal.SIGTERM, signal_handler)  # Terminierungssignal

# ============================================
# Hauptprogramm
# ============================================

# Verbinde
device = Dobot(port="/dev/ttyACM0")
device.connect()
device.ir_toggle(enable=True)

print("✓ Start")
print("(Drücke Ctrl+C zum Beenden)\n")

# Endlosschleife (läuft bis Signal kommt)
try:
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

except Exception as e:
    print(f"✗ Fehler: {e}")
    device.close()