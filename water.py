import RPi.GPIO as GPIO
import time as try:

GPIO.setmode(GPIO.BCM)

GPIO.setup(3, GPIO.OUT, pull_up_down=GPIO.PUD_UP)

GPIO.setup(2, GPIO.OUT, )

while True:
    if (GPIO.input(3) ==1):
        print ("button pressed")

GPIO.cleanup()
