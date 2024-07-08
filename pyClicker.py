from tkinter import *
from pynput import keyboard
import time

# Root configuration
root = Tk()
root.resizable(False, False)
root.geometry("400x200")

startKey = ""

# Functions
def on_key_press(x):
    global startKey
    startKey = x
    print(x)
    if hasattr(x, "char") and x.char == "z":
        print("Z Pressed")
    keyboard_listener.stop()

keyboard_listener = keyboard.Listener(
    on_press=on_key_press
)


def onClick():
    global startKey

    button.config(text="press any key")

    keyboard_listener.start()
    time.sleep(5)

    print("zmačkle")
    button.config(text=startKey)


# Widgets
label = Label(root, text="pyAutoclicker")
button = Button(root, text="Nothing", command=onClick)
errorLabel = Label(root, text="")


# Positioning
label.place(x=200, y=0, anchor=N)
button.place(x=200, y=50, anchor=N)
errorLabel.place(x=10, y=20)

# Main
root.mainloop()

