from tkinter import *

class My_Buttons:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.messageButton = Button(frame, text="output this message",command=self.outputmy_Message)
        self.messageButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="quit!", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def outputmy_Message(self):
        print("wowowin haha")

root = Tk()
m = My_Buttons(root)
root.mainloop()
