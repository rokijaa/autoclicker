from tkinter import *
from pynput import keyboard

# Root configuration
root = Tk()
root.resizable(False, False)
root.geometry("400x200")

def getButton():
    if event.key == "None":
        return
    key = event.key
    button.config(text=key)
    upButtonLabel.config(text="")

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
label = Label(root, text="Click button and then select a key, which will be used to start autoclicking")
upButtonLabel = Label(root, text="! Key empty !")
button = Button(root, text="", command=onClick)
errorLabel = Label(root, text="")

button.config(width=8, height=2)

# Positioning
label.place(x=200, y=0, anchor=N)
upButtonLabel.place(x=200, y=30, anchor=N)
button.place(x=200, y=50, anchor=N)
errorLabel.place(x=10, y=20)

# Main
root.mainloop()

