from tkinter import *

root = Tk()
def myName(event):
        print("Joshua Meredores")

button_1 = Button(root, text="Click to see my name")
button_1.bind("<Button-1>", myName)
button_1.pack()
root.mainloop()
