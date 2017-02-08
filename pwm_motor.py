#!/usr/bin/python
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setup(12, gpio.OUT)

in1 = gpio.PWM(11, 100)
in2 = gpio.output(12, False)

count = 0
decrement = 100
a=0

in1.start(count)
while a < 3:
	while count < 100:
		in1.ChangeDutyCycle(count)
		time.sleep(0.01)
		count += 1
	
		if count == 100:
			while count > 0:
				in1.ChangeDutyCycle(count)
				time.sleep(0.01)
				count -= 1
	a += 1
in1.stop()
gpio.cleanup()

