from serial import Serial, SerialException
try:
    s=Serial(port="/dev/ttyACM0", baudrate=115200, timeout=0.1)
    s.close()
    print("✅ Verbindung zum Dobot hergestellt.")
except SerialException:
    print("❌ Verbindung zum Dobot fehlgeschlagen. Bitte überprüfen Sie die Verbindung und versuchen Sie es erneut.")   

from dobotapi import Dobot
bot = Dobot(port="/dev/ttyACM0")
bot.connect()
bot.close()
 