from tkinter import *
from pynput import keyboard
import time

# Root configuration
root = Tk()
root.resizable(False, False)
root.geometry("400x200")

def getButton():
    if event.key == "None":
        return
    button.config(text=event)

def onClick():
    with keyboard.Events() as events:
        global event
        for event in events:
            if event.key == keyboard.Key.esc:
                break
            else:
                getButton()
                break

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

