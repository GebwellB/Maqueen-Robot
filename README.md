# Maqueen Robot - The Downfall of Humanity

## Implementation – how did I do?
For this project, I used the following components:
1x Maqueen Robot
2x Microbit boards (1 Transmitter, 1 Receiver / controlling the Maqueen Robot)

To get these to work together, I first send serial commands via my PC to the Microbit Transmit board, this decodes the serial messages then via radio transmits them to the Microbit Receiver board. On that board, it's simplying listening for events over radio then depending what is received, will control the motors.

To go further indepth, the PC is listening for keyboard input, Up Arrow, Left Arrow and Right Arrow. When these buttons are pressed, they are added to a set(). This is to stop spamming across serial and radio. The code then checks to see if the button is part of the set. If it isn't, it first gets added to the set then continues on to start sending the command. While the button is held down, it'll continue to check but the serial command is only sent once, rather than being queued up and spammed. Once a button is released, the set() is cleared and the stop command is sent via serial.

On the Microbit Transmit board, this is simply listening for serial commands from the PC. Once it receives anything over serial, it decodes it. The code then checks to see what was said in the message. Depending on what was received, it'll then send the corrosponding code over radio to the receiver board.

On the Microbit Receiver board, this does basically the same as the transmit board just in reverse. It's just waiting for messages, then depending on what's received, it turns on the corrosponding motors.

The full run down: Up Arrow Pressed -> Adds to held_keys set() -> sends "forward" via serial to Microbit Transmit board -> Decodes serial message, then sends on via radio -> Microbit Receiver board gets message, turns on motor based on the message. Once the key is released, the key is removed from held_keys and "stop" is send via serial.

## Describe the functions

## The requirements for the robots / pip freeze

## What type of license
