from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x785+0+0")
        self.root.title("Face Recognition System")
        
if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()