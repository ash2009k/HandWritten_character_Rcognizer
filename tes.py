__author__ = 'Ashwini'

from tkinter import *


def make_image():
    photo  = PhotoImage(file="C:/Users/Ashwini/Desktop/by_class/6a/hsf_0/hsf_0_00003.png")
    myCanvas.image = photo
    myCanvas.create_image(0,0, image = photo, anchor = "nw")



root = Tk()

myCanvas = Canvas(root, width=100, height=100)
myCanvas.grid()


make_image()

root.mainloop()
'''
from tkinter import *
from tkinter import filedialog


root = Tk()

photu=PhotoImage(file="C:/Users/Ashwini/Desktop/by_class/6a/hsf_0/hsf_0_00003.png")
photu_label=Label(root,image=photu)
photu_label.pack()


root.mainloop()
'''