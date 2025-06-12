import serial
from pynput import keyboard

# Configure the serial port
ser = serial.Serial('COM7', 115200)

# Track which keys are currently held down, to avoid spam
held_keys = set()

def on_press(key):
    if key not in held_keys:
        held_keys.add(key)
        if key == keyboard.Key.up:
            ser.write(b"1\n")
            print("Forward")
        elif key == keyboard.Key.right:
            ser.write(b"2\n")
            print("Right")
        elif key == keyboard.Key.left:
            ser.write(b"3\n")
            print("Left")

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    else:
        held_keys.clear()
        ser.write(b"0\n")
        print("Stop")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
