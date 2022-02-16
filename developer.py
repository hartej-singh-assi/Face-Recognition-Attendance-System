from tkinter import *
from PIL import Image,ImageTk


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x785+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1600,height=45)
        
        img=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\Hipster-Developer-Dice.jpg")
        img=img.resize((1600,720),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        lbl_1=Label(self.root,image=self.photoimg)
        lbl_1.place(x=0,y=55,width=1600,height=720)
        
        # Frame
        main_frame=Frame(lbl_1,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=500,height=600)
        
        img_1=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\IMG-20210722-WA0040.jpg")
        img_1=img_1.resize((180,200),Image.ANTIALIAS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)
         
        lbl_2=Label(main_frame,image=self.photoimg_1)
        lbl_2.place(x=320,y=0,width=175,height=200)
        
        # Developer 
        dev_lbl1=Label(main_frame,text="Hello my name is Hartej",font=("times new roman",20,"bold"),bg="white")
        dev_lbl1.place(x=0,y=5)
        
        dev_lbl2=Label(main_frame,text="I am Full Stack Developer",font=("times new roman",20,"bold"),bg="white")
        dev_lbl2.place(x=0,y=40)
        
        img3=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\Screenshot_20220213-195807_Google.jpg")
        img3=img3.resize((495,386),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lbl_3=Label(main_frame,image=self.photoimg3)
        lbl_3.place(x=0,y=210,width=495,height=386)
        
        
        
if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()