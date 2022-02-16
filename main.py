from time import strftime
from datetime import datetime
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from helpd import Helpd
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from helpd import Helpd



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x785+0+0")
        self.root.title("Face Recognition System")
        
        # Top Images
        # First Image
        img1=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\dormakaba-Blog-Post-pictures-_-1024-x-683-83.jpg")
        img1=img1.resize((517,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lbl_1=Label(self.root,image=self.photoimg1)
        lbl_1.place(x=0,y=0,width=517,height=130)
        
        # Second Image
        img2=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\facialrecognition.png")
        img2=img2.resize((502,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lbl_2=Label(self.root,image=self.photoimg2)
        lbl_2.place(x=517,y=0,width=502,height=130)
        
        # Third Image
        img3=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\Screenshot_20220213-194451_Chrome.jpg")
        img3=img3.resize((517,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lbl_3=Label(self.root,image=self.photoimg3)
        lbl_3.place(x=1019,y=0,width=517,height=130)
        
        # Background Image
        bckimg=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\anything.jpg")
        bckimg=bckimg.resize((1600,710),Image.ANTIALIAS)
        self.photobckimg=ImageTk.PhotoImage(bckimg)
        
        bg_img=Label(self.root,image=self.photobckimg)
        bg_img.place(x=0,y=130,width=1600,height=710)
        
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        # time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl=Label(title_lbl,font=('times new roman',14,'bold'),background = 'white',foreground = 'blue')
        lbl.place(x=0,y=(-15),width=110,height=50)
        time()
        
        # Student Button
        img4=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\Screenshot_20220213-191248_Chrome.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=200,y=300,width=220,height=40)
        
        # Face Detection Button
        img5=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\2428101-1024x683.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=500,y=300,width=220,height=40)
        
        # Attendance Button
        img6=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\office-software-attendance-management-business-concept-infographics-for-web-banner-calendar-task-list-and-chart-the-user-personal-account-vector.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance)
        b1.place(x=800,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        # Help Desk Button
        img7=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\Help-Desk.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_desk)
        b1.place(x=1100,y=100,width=220,height=220)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_desk,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=1100,y=300,width=220,height=40)
        
        # Train Button
        img8=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\Screenshot_20220213-195013_Chrome.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=200,y=600,width=220,height=40)
        
        # Photos Button
        img9=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\Screenshot_20220213-202038_Chrome.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=400,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photo's",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=500,y=600,width=220,height=40)
        
        # Developer Button
        img10=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\Screenshot_20220213-200158_Chrome.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_info)
        b1.place(x=800,y=400,width=220,height=220)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_info,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=800,y=600,width=220,height=40)
        
        # Exit Button
        img11=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\Screenshot_20220216-215721_Chrome.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit)
        b1.place(x=1100,y=400,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="white",fg="red")
        b1_1.place(x=1100,y=600,width=220,height=40)       
        
    def open_img(self):
        os.startfile("data")
        
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure that you want to exit",parent=self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return 
        
    # ---------------------------------function button-------------------------------
    
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window) 
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
        
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_info(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpd(self.new_window)
        
if __name__== "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()