from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
button1 = 3
GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while(1):
    if GPIO.input(button1) == 0:
        print "Button 1 was pressed"
        sleep(.1)
