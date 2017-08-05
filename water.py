from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
# button1 = 3
relay1 = 2
#test
# GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(relay1, GPIO.OUT)
while(1):
    GPIO.output(relay1,False)
    sleep(.5)
    GPIO.output(relay1,True)
    sleep(.5)
