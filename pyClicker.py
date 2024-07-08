from tkinter import *
from pynput import keyboard
import time

# Root configuration
root = Tk()
root.resizable(False, False)
root.geometry("400x200")

# Functions
def on_key_press(key):
    startKey = key
    print(startKey)
    if hasattr(key, "char") and key.char == "z":
        print("Z Pressed")

keyboard_listener = keyboard.Listener(
    on_press=on_key_press
)

def onClick():
    key = keyboard_listener.start()

# Widgets
label = Label(root, text="pyAutoclicker")
button = Button(root, command=onClick)


# Positioning
label.place(x=200, y=0, anchor=N)
button.place(x=200, y=50, anchor=N)


# Main
root.mainloop()

