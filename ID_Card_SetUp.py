import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD

lcd = CharLCD('PCF8574', 0x27)
reader = SimpleMFRC522()
lcd.clear()

try:
    text = input('New Data:')
    print("Plase your tag to write")
    reader.write(text)
    print("Written")
    
finally:
    GPIO.cleanup() 