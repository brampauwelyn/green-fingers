from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

# No color 
O = (0,0,0)

# lightblue
L = (62,216,255) 

# darkblue 
D = (65,198,255)

# drawing

# Make the pixel heart
drop1 = [
O, O, O, D, O, O, O, O,
O, O, D, L, D, O, O, O,
O, D, L, D, L, D, O, O,
O, L, D, L, D, L, O, O,
O, D, L, D, L, D, O, O,
O, O, D, L, D, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

drop2 = [
O, O, O, O, O, O, O, O,
O, O, O, D, O, O, O, O,
O, O, D, L, D, O, O, O,
O, D, L, D, L, D, O, O,
O, L, D, L, D, L, O, O,
O, D, L, D, L, D, O, O,
O, O, D, L, D, O, O, O,
O, O, O, O, O, O, O, O
]

drop3 = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, D, O, O, O, O,
O, O, D, L, D, O, O, O,
O, D, L, D, L, D, O, O,
O, L, D, L, D, L, O, O,
O, D, L, D, L, D, O, O,
O, O, D, L, D, O, O, O
]

drop4 = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, D, O, O, O, O,
O, O, D, L, D, O, O, O,
O, D, L, D, L, D, O, O,
O, L, D, L, D, L, O, O,
O, D, L, D, L, D, O, O
]

drop5 = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, D, O, O, O, O,
O, O, D, L, D, O, O, O,
O, D, L, D, L, D, O, O,
O, L, D, L, D, L, O, O
]

drop6 = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, D, O, O, O, O,
O, O, D, L, D, O, O, O,
O, D, L, D, L, D, O, O
]

drop7 = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, D, O, O, O, O,
O, O, D, L, D, O, O, O
]

drop8 = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, D, O, O, O, O
]

drop9 = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O
]

sense.set_pixels(drop1)
sleep(1)
sense.set_pixels(drop2)
sleep(1)
sense.set_pixels(drop3)
sleep(1)
sense.set_pixels(drop4)
sleep(1)
sense.set_pixels(drop5)
sleep(1)
sense.set_pixels(drop6)
sleep(1)
sense.set_pixels(drop7)
sleep(1)
sense.set_pixels(drop8)
sleep(1)
sense.set_pixels(drop9)