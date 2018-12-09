import RPi.GPIO as GPIO
from time import sleep
from weather import weather
from notify import notify
relay1 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay1, GPIO.OUT)

# Define Colors for console output
class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Function to Reset GPIOs
def resetGPIO(relay):
    GPIO.output(relay1,GPIO.LOW)

# 27 sec --> 200ml
# 13.5 sec --> 100ml


# Function to start relay and give water
def water():
    resetGPIO(relay1)
    print(colors.BLUE + "Watering Plants...")
    GPIO.output(relay1,GPIO.HIGH)
    #Should give 100 ml water
    sleep(90)
    # Disable Relay
    resetGPIO(relay1)
    print (colors.GREEN + "Done Watering Plants")
    #Get Weather information
    weather()
    #Call function notify to send email notification
    notify_mailgun()
    # clean up GPIO
    GPIO.cleanup()
    # Exit script
    exit()

water()
