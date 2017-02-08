import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setup(12, gpio.OUT)
gpio.cleanup()

