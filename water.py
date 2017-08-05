import RPi.GPIO as GPIO
import time as t

GPIO.setmode(GPIO.BCM)

GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(2, GPIO.OUT, )

while True:
    if (GPIO.input(3) == 0):
        print ("button pressed")

GPIO.cleanup()
