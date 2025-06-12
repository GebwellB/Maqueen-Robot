import radio
from microbit import *

radio.config(channel=69)
display.set_pixel(2, 2, 9)

while True:
    if button_a.is_pressed():
        break
    if uart.any():
        msg = uart.readline()
        if msg:
            decoded = msg.decode().strip()
            
        if decoded == "1": # Forward
            radio.send("forward")
            
        elif decoded == "2": # Left
            radio.send("left")
            
        elif decoded == "3": # Right
            radio.send("right")
            
        elif decoded == "0": # Stop
            radio.send("halt")
            
        sleep(100)
    