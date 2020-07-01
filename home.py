__author__ = 'Ashwini'
from tkinter import *
from tkinter import filedialog
import tensorflow as tf
import numpy as np
import cv2

#Creating a tkinter gui window

root = Tk()
root.config(background="#A9CCE3")
root.title("HCR")
root.iconbitmap(r"C:/Users/Ashwini/PycharmProjects/deep/guihcr/iconfinder_Ocr S_38896.ico")


#Defining our recognizer function
def recognizer():
    #Getting path of the file to recognize
    file_path=pathlabel.cget("text")
    #Used for finding characters based on class number predicted
    CATEGORIES = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    img_array = cv2.imread((file_path) ,cv2.IMREAD_GRAYSCALE)
    #Resizing to desired size
    new_array = cv2.resize(img_array, (60, 60))
    X = []
    X.append(new_array)
    X = tf.cast(X, tf.float32)
    #creating numpy array with required size
    X = np.array(X).reshape(-1,60,60,1)

    #Loading our model
    final_model = tf.keras.models.load_model('final.model')

    #Predicting our image class
    category_list= final_model.predict(X)
    print(category_list[0])
    category=np.argmax(category_list)
    print(category,CATEGORIES[category])
    #Predicted character sent as output to GUI
    pathlabel1.config(text= str(CATEGORIES[category]), font=("Helvetica", 20))





#Initial window size of Application
root.geometry("1280x720")

#Header
w = Label(root, text="HandWritten Character Recognizer",  fg="black", font=("Helvetica", 32),background="#D0ECE7")
w.pack(pady=15)

#for browsing image and setting new image file and its directory in GUI
def browsefunc():
    filename = filedialog.askopenfilename(initialdir = "C:/Users/Ashwini/Desktop/by_class",title = "Select png image to recognize",filetypes = [("PNG files","*.png")])
    '''initialdir = "C:/Users/Ashwini/Desktop/by_class",'''
    pathlabel.config(text=filename)
    photu=PhotoImage(file=filename)
    photu_label.img=photu
    photu_label.config(image=photu_label.img)


#For displaying image to be recognised

photu_label=Label(root)
photu_label.pack()
photu=PhotoImage(file="IMG_20180703_104908-01.png")
photu_label.config(image=photu)

#For displaying path of image to be recognised
pathlabel = Label(root,text="You are currently viewing an AMBIGRAM.")
pathlabel.pack(pady=10)

pathlabel2 = Label(root,text="IMAGE Recognized as ------->>>  ")
pathlabel2.pack(pady=10)

#For displaying our predicted output of our image
pathlabel1 = Label(root)
pathlabel1.pack(pady=10)


#Button for browse action
browsebutton = Button(root, text="Browse", command=browsefunc,bg="#00ffff")
browsebutton.pack(pady=5)
browsebutton.config(height=1,width=20)

#Button for recognize action
recognizebutton = Button(root, text="Recognize", command=recognizer,bg="#00ffff")
recognizebutton.pack()
recognizebutton.config(height=1,width=20)




mainloop()





