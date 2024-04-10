from tkinter import *
from time import sleep

fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]

num = 0

def click_next():
    global num
    num = (num + 1) % len(fnameList)
    pLabel.configure(text=fnameList[num])

def click_prev():
    global num
    num = (num - 1) % len(fnameList)
    pLabel.configure(text=fnameList[num])

window = Tk()
window.title("Image Viewer")

pLabel = Label(window, text=fnameList[num])
pLabel.pack()

next_button = Button(window, text="Next", command=click_next)
next_button.pack(side=RIGHT)

prev_button = Button(window, text="Previous", command=click_prev)
prev_button.pack(side=LEFT)

window.mainloop()