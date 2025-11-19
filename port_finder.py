from serial.tools import list_ports
from serial import Serial, SerialException
import time
import dobotapi as bot

# -------------------------------
# 1) Port-Finder
# -------------------------------
def find_dobot_port():
    for p in list_ports.comports():
        desc = (p.description or "").upper()
        if any(k in desc for k in ("CP210", "USB", "UART", "SLAB")):
            return p.device
    return None

def ensure_port_openable(port):
    if port is None:
        raise RuntimeError("Kein Dobot-Port gefunden. Treiber/Kabel prüfen.")
    try:
        s = Serial(port=port, baudrate=115200, timeout=0.1)
        s.close()
    except SerialException as e:
        raise RuntimeError(f"Port {port} lässt sich nicht öffnen: {e}")
    
port = find_dobot_port()
print(f"Gefundener Port: {port}")
ensure_port_openable(port)
 

