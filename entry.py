from tkinter import *

def submit():
    username = entry.get()
    print("Good evening " + username)
def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()
entry = Entry(window, 
              font=("Arial", 40),
              fg="#00ff00",
              bg="black"
              )
entry.pack(side=LEFT)
submitbutton = Button(window, text="submit", command=submit)
submitbutton.pack(side=LEFT)

deletebutton = Button(window, text="delete", command=delete)
deletebutton.pack(side=LEFT)

backspacebutton = Button(window, text="backspace", command=backspace)
backspacebutton.pack(side=LEFT)

window.mainloop()
