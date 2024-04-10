from tkinter import *
from tkinter import filedialog

# Function Declaration Part
def func_open():
    global current_index, image_list
    filenames = filedialog.askopenfilenames(parent=window, filetypes=[("GIF files", "*.gif"), ("All files", "*.*")])
    if filenames:
        image_list = [PhotoImage(file=filename) for filename in filenames]
        current_index = 0
        display_image()

def display_image():
    global current_index
    if image_list:
        photo = image_list[current_index]
        pLabel.configure(image=photo)
        pLabel.image = photo

def next_image():
    global current_index
    if image_list:
        current_index = (current_index + 1) % len(image_list)
        display_image()

def prev_image():
    global current_index
    if image_list:
        current_index = (current_index - 1) % len(image_list)
        display_image()

def func_exit():
    window.quit()
    window.destroy()

# Main Code Part
window = Tk()
window.geometry("400x400")
window.title("Image Viewer")

image_list = []
current_index = 0

pLabel = Label(window)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=func_exit)

# Navigation buttons
prev_button = Button(window, text="Previous", command=prev_image)
prev_button.pack(side=LEFT, padx=10)
next_button = Button(window, text="Next", command=next_image)
next_button.pack(side=RIGHT, padx=10)

window.mainloop()
