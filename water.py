from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
button1 = 3
relay1 = 2
GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(relay1, GPIO.OUT)
while(1):
    if GPIO.input(button1) == 0:
        print "Button 1 was pressed"
        GPIO.output(relay1,True)
        sleep(.5)
