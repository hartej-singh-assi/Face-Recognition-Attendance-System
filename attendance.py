from operator import delitem
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x785+0+0")
        self.root.title("Face Recognition System")
        
        # -------------- variables ---------------
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        # Top Images
        # First Image
        img1=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\images (2).jpg")
        img1=img1.resize((768,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lbl_1=Label(self.root,image=self.photoimg1)
        lbl_1.place(x=0,y=0,width=768,height=200)
        
        # Second Image
        img2=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\Screenshot_20220213-191427_Chrome.jpg")
        img2=img2.resize((768,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lbl_2=Label(self.root,image=self.photoimg2)
        lbl_2.place(x=768,y=0,width=768,height=200)
        
        # Background Image
        bckimg=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\37ab0be887b5a74c48c21b7928381ca0.jpg")
        bckimg=bckimg.resize((1600,710),Image.ANTIALIAS)
        self.photobckimg=ImageTk.PhotoImage(bckimg)
        
        bg_img=Label(self.root,image=self.photobckimg)
        bg_img.place(x=0,y=200,width=1600,height=710)
        
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1520,height=600)
        
        # Left Label Frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=745,height=580)
        
        img_left=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\Screenshot_20220213-194207_Chrome.jpg")
        img_left=img_left.resize((735,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        lbl_left=Label(left_frame,image=self.photoimg_left)
        lbl_left.place(x=5,y=0,width=735,height=130)
        
        left_in_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_in_frame.place(x=0,y=135,width=735,height=370)
        
        # Label and entry field
        # attendance ID
        attendance_lbl=Label(left_in_frame,text="Attendance ID:",font=("times new roman",13,"bold"),bg="white")
        attendance_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendance_entry=ttk.Entry(left_in_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendance_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        # Roll no
        roll_lbl=Label(left_in_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_lbl.grid(row=0,column=2,padx=4,pady=8)
        
        roll_entry=ttk.Entry(left_in_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        roll_entry.grid(row=0,column=3,pady=8)
        
        # Name
        Name_lbl=Label(left_in_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        Name_lbl.grid(row=1,column=0,padx=4,pady=8)
        
        Name_entry=ttk.Entry(left_in_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        Name_entry.grid(row=1,column=1,pady=8)
        
        # Department
        dep_lbl=Label(left_in_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        dep_lbl.grid(row=1,column=2)
        
        dep_entry=ttk.Entry(left_in_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        dep_entry.grid(row=1,column=3,pady=8)
        
        # time
        time_lbl=Label(left_in_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        time_lbl.grid(row=2,column=0)
        
        time_entry=ttk.Entry(left_in_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        time_entry.grid(row=2,column=1,pady=8)
        
        
        # date
        date_lbl=Label(left_in_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        date_lbl.grid(row=2,column=2)
        
        date_entry=ttk.Entry(left_in_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        date_entry.grid(row=2,column=3,pady=8)
        
        # attendance
        attendance_lbl=Label(left_in_frame,text="Attendance Status",font=("times new roman",13,"bold"),bg="white")
        attendance_lbl.grid(row=3,column=0)
        
        attendance_combo=ttk.Combobox(left_in_frame,textvariable=self.var_atten_attendance,font=("times new roman",11,"bold"),width=20,state="readonly")
        attendance_combo["values"]=("Status","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3,column=1,pady=8)
        
        # Button Frame
        btn_frame1=Frame(left_in_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=300,width=730,height=35)
        
        import_btn=Button(btn_frame1,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0,padx=1)
        
        export_btn=Button(btn_frame1,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1,padx=1)
        
        update_btn=Button(btn_frame1,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2,padx=1)
        
        reset_btn=Button(btn_frame1,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=1)
        
        
        # Right Label Frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=765,y=10,width=745,height=580)
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=725,height=455)
        
        # ------------------- Scroll bar & table ------------------------
        
        scroll_X=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_X.set,yscrollcommand=scroll_Y.set)
        
        scroll_X.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)
        
        scroll_X.config(command=self.AttendanceReportTable.xview)
        scroll_Y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=110)
        self.AttendanceReportTable.column("roll",width=110)
        self.AttendanceReportTable.column("name",width=110)
        self.AttendanceReportTable.column("department",width=110)
        self.AttendanceReportTable.column("time",width=110)
        self.AttendanceReportTable.column("date",width=110)
        self.AttendanceReportTable.column("attendance",width=110)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    # --------------------- fetch data ----------------------
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    # Import csv        
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=',')
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    # Export csv
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data","No data found for export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=',')
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data has been exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                
    def get_cursor(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
    
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
        
if __name__== "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()