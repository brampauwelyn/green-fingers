 from gpiozero import Button
 button = Button(3)

 button.wait_for_press()
 print('You pushed me')

 
