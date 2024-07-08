from tkinter import *

# Root configuration
root = Tk()
root.resizable(False, False)
root.configure(height=200, width=400)

# Widgets
label = Label(root, text="pyAutoclicker")

# Positioning
label.place(x=200, y=0, anchor=N)


# Main
root.mainloop()

