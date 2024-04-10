from tkinter import *

# Global Variables Declaration Part
btnList = [None] * 9
fnameList = ["honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif", "lolipop.gif", "marshmallow.gif", "pinguin.gif", "fox.gif", "android.gif"]
photoList = [None] * 9
i, k = 0, 0
xPos, yPos = 0, 0
num = 0

# Main Code Part
window = Tk()
window.geometry("210x210")

import os

for i in range(0, 9):
    file_path = os.path.join("gif", "E:\\22. i-SEED Programming\\Picture Assg 5", fnameList[i])
    photoList[i] = PhotoImage(file=file_path)
    btnList[i] = Button(window, image=photoList[i], borderwidth=0)

# Place buttons in grid
for i in range(0, 3):
    for k in range(0, 3):
        btnList[num].place(x=xPos, y=yPos)
        num += 1
        xPos += 70
    xPos = 0
    yPos += 70

window.mainloop()