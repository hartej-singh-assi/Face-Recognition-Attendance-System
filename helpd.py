from tkinter import *
from PIL import Image,ImageTk


class Helpd:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x785+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1600,height=45)
        
        img=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\b903ea254dfaa706337d9ce39fe93fa5.jpg")
        img=img.resize((1600,720),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        lbl_1=Label(self.root,image=self.photoimg)
        lbl_1.place(x=0,y=55,width=1600,height=720)
        
        email_lbl=Label(self.root,text="Email: hartejsinghassi@gmail.com",font=("times new roman",20,"bold"),fg="blue",bg="light blue")
        email_lbl.place(x=600,y=400)
        
if __name__== "__main__":
    root=Tk()
    obj=Helpd(root)
    root.mainloop()