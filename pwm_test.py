#!/usr/bin/python
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setup(12, gpio.OUT)

g = gpio.PWM(11, 100)
r = gpio.PWM(12, 100)

count = 0
decrement = 100

g.start(count)
r.start(count)

while count < 100:
	g.ChangeDutyCycle(count)
	r.ChangeDutyCycle(count)
	time.sleep(0.01)
	count += 1
	
	if count == 100:
		while count > 0:
			g.ChangeDutyCycle(count)
			r.ChangeDutyCycle(count)
			time.sleep(0.01)
			count -= 1
g.stop()
r.stop()
gpio.cleanup()

