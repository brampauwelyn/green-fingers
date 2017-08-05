from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
relay1 = 17
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
    GPIO.output(relay1,False)

# 27 sec --> 200ml
# 13.5 sec --> 100ml

# Reset GPIO's
# Disable Relay by default
resetGPIO(relay1)

while(1):
    print(colors.BLUE + "Watering Plants...")
    GPIO.output(relay1,True)
    #Should give 100 ml water
    sleep(13.5)
    # Disable Relay
    resetGPIO(relay1)
    print (color.GREEN + "Done Watering Plants")
    break
# clean up GPIO
# GPIO.cleanup()
# Exit script
exit()
