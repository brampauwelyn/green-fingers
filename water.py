from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
button1 = 3
relay1 = 17
GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(relay1, GPIO.OUT)

# 27 sec --> 200ml
# 13.5 sec --> 100ml

# Reset GPIO's
# Disable Relay by default
GPIO.cleanup()
GPIO.output(relay1,False)
while(1):
    print "Watering Plants"
    GPIO.output(relay1,True)
    #Should give 100 ml water
    sleep(13.5)
    GPIO.output(relay1,False)
    print "Stop Watering Plants"
    break
# clean up GPIO
GPIO.cleanup()
# Exit script
exit()
