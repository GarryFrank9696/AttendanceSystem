import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD
import time as t

lcd = CharLCD('PCF8574', 0x27)
reader = SimpleMFRC522()

try:
    while True:
        lcd.write_string('Please scan card')
        id, text = reader.read()
        print(id)
        print(text)
        lcd.clear()
        lcd.write_string('\r\n')
        lcd.write_string(text)
        lcd.write_string('\r\n')
        lcd.write_string(str(id))
        t.sleep(3)
        lcd.clear()
        
finally:
    GPIO.cleanup()