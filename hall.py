#!/usr/bin/python

# Import required libraries
import RPi.GPIO as GPIO
from RPLCD import CharLCD
import time
import datetime

def sensorCallback1(channel):
  # Called if sensor output goes LOW
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  print "Sensor LOW " + stamp

def sensorCallback2(channel):
  # Called if sensor output goes HIGH
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  lcd.clear()
  lcd.write_string(u'ON')
  print "Sensor HIGH " + stamp

lcd = CharLCD(cols=16, rows=2, numbering_mode= GPIO.BCM, pin_rs=26, pin_e=19, pins_data= [13, 6, 5, 20])

def main():

  try:
    # Loop until users quits with CTRL-C
    while True :
      time.sleep(0.1)
      lcd.clear()
      lcd.write_string(u'OFF')
  except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()  
  
# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

print "Setup GPIO pin as input"

# Set Switch GPIO as input
GPIO.setup(22 , GPIO.IN)
#GPIO.add_event_detect(22, GPIO.FALLING, callback=sensorCallback1)
GPIO.add_event_detect(22, GPIO.RISING, callback=sensorCallback2)

if __name__=="__main__":
   main()
