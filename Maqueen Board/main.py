import radio
import random
from microbit import *
import maqueen

motor = maqueen.MaqueenMotors()

radio.config(channel=69)

display.clear()
sleep(1)
display.on()

display.show(Image.HAPPY)

while True:    
    incoming = radio.receive()
    
    if incoming == 'forward':
        motor.forwards(9) 
        
    if incoming == 'right':
        motor.right_motor(9)
        
    if incoming == 'left':
        motor.left_motor(9)
        
    if incoming == 'halt':
        motor.stop()
    
