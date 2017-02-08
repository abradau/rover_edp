import os
# make sure module is in the path
os.chdir('/home/pi/lcd')
import lcd
# Define GPIO to LCD mapping
LCD_RS = 26
LCD_E  = 19
LCD_D4 = 13 
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 20
lcd.lcd_init()
# set cursor to line 1
lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
# display text centered on line 1
lcd.lcd_string("Raspberry Pi", 2)
# set cursor to line 2
lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
# display additional text on line 2
lcd.lcd_string("Model B+", 2)
lcd.GPIO.cleanup()
