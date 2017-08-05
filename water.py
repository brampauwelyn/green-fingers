import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
    if(GPIO.input(3) == 1):
        print("Yeah")
