from tkinter import *

window = Tk()
window.title("tk -image")
window.geometry("500x500")
window.iconbitmap("C:\Users\joshu\Downloads\piza.png")

label = Label(window,
              bd =5,
              relief= SUNKEN)
label.pack(padx =10, pady =10)


button = Button(window,
                bd=5,
                relief=SUNKEN)
button.pack(padx=10, pady=10)

window.mainloop()
