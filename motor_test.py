#!/usr/bin/python
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setup(12, gpio.OUT)

number = 0

while number < 5:
	gpio.output(11, True)
	gpio.output(12, False)
	time.sleep(2)
	gpio.output(11, False)
	gpio.output(12, True)
	time.sleep(2)
	gpio.output(11, False)
	gpio.output(12, False)
	print 'Loop : ', number
	number += 1

