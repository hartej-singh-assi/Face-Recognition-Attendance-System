from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x785+0+0")
        self.root.title("Face Recognition System")
        
        # variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_faculty=StringVar()
        
        # Top Images
        # First Image
        img1=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\facialrecognition.png")
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
        img3=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\facialrecognition.png")
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
        
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1520,height=600)
        
        # Left Label Frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=745,height=580)
        
        img_left=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\facialrecognition.png")
        img_left=img_left.resize((735,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        lbl_left=Label(left_frame,image=self.photoimg_left)
        lbl_left.place(x=5,y=0,width=735,height=130)
        
        # Current Course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course infomation",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=735,height=125)
        
        # Department
        dep_lbl=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_lbl.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","Information Technology","Maths","BMS")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        # Course
        course_lbl=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_lbl.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","FY","SY","TY","M.Sc")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        # Year
        year_lbl=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_lbl.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
        
        # Semester
        Sem_lbl=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        Sem_lbl.grid(row=1,column=2,padx=10,sticky=W)
        
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),width=20,state="readonly")
        sem_combo["values"]=("Select Semester","Semester-1","Semester 2","Semester 3","Semester 4","Semester 5","Semester 6")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        # Class student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=735,height=300)
        
        # Student ID
        stud_id_lbl=Label(class_student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        stud_id_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        stud_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        stud_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        # Student Name
        stud_name_lbl=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        stud_name_lbl.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        stud_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        stud_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # Class Division
        class_div_lbl=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_lbl.grid(row=1,column=0,padx=10,pady=5,sticky=W)  
        
        class_div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),width=18,state="readonly")
        class_div_combo["values"]=("None","A","B","C")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        # Roll No
        roll_no_lbl=Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_lbl.grid(row=1,column=2,padx=10,pady=5,sticky=W)  
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        # Gender
        gender_lbl=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_lbl.grid(row=2,column=0,padx=10,pady=5,sticky=W)  
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        # Date of Birth
        DOB_lbl=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        DOB_lbl.grid(row=2,column=2,padx=10,pady=5,sticky=W)  
        
        DOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        # Email
        email_lbl=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_lbl.grid(row=3,column=0,padx=10,pady=5,sticky=W) 
         
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        # Phone No
        phone_lbl=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_lbl.grid(row=3,column=2,padx=10,pady=5,sticky=W)  
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        # Adderss
        add_lbl=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        add_lbl.grid(row=4,column=0,padx=10,pady=5,sticky=W) 
        
        add_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        add_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        # Faculty
        fac_lbl=Label(class_student_frame,text="Faculty:",font=("times new roman",13,"bold"),bg="white")
        fac_lbl.grid(row=4,column=2,padx=10,pady=5,sticky=W)  
        
        fac_entry=ttk.Entry(class_student_frame,textvariable=self.var_faculty,width=20,font=("times new roman",13,"bold"))
        fac_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        # Radio Button
        radio_lbl=Label(class_student_frame,text="Take Photo:",font=("times new roman",13,"bold"),bg="white")
        radio_lbl.grid(row=6,column=0,padx=10,pady=5,sticky=W)
        
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Yes",value="Yes")
        radiobtn1.grid(row=6,column=1)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No",value="No")
        radiobtn2.grid(row=6,column=2)
        
        # Button Frame
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=200,width=730,height=35)
        
        save_btn=Button(btn_frame1,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=1)
        
        update_btn=Button(btn_frame1,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=1)
        
        delete_btn=Button(btn_frame1,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=1)
        
        reset_btn=Button(btn_frame1,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=1)
        
        btn_frame2=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=0,y=235,width=730,height=35)
        
        take_photo_btn=Button(btn_frame2,command=self.generate_dataset,text="Take Photo",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0,padx=2)
        
        update_photo_btn=Button(btn_frame2,text="Update Photo",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1,padx=1)
        
        # Right Label Frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=765,y=10,width=745,height=580)
        
        img_right=Image.open(r"C:\Users\harte\Desktop\CS PRACTICALS\sem 6\Project\Face Recognition + Attendance System\images\facialrecognition.png")
        img_right=img_right.resize((735,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        lbl_right=Label(right_frame,image=self.photoimg_right)
        lbl_right.place(x=5,y=0,width=735,height=130)
        
        # --------------- Search System ---------------------
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=735,height=70)
        
        search_lbl=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="white")
        search_lbl.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=20,pady=5,sticky=W)
        
        search_btn=Button(search_frame,text="Seaarch",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        show_all_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        show_all_btn.grid(row=0,column=4,padx=4)
        
        # Table Frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE,)
        table_frame.place(x=5,y=210,width=735,height=345)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","faculty","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("faculty",text="Faculty")
        self.student_table.heading("photo",text="Photo Sample")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("faculty",width=100)
        self.student_table.column("photo",width=150)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    # Function
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_faculty.get(),
                                                                                                                self.var_radio1.get()
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                
                
    
    #--------------------fetch data----------------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    #---------------get cursor--------------
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_faculty.set(data[13]),
        self.var_radio1.set(data[14])
        
    # update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Faculty=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_std_name.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_faculty.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_std_id.get()                                                                                                                                                                
                                                                                                                                                                            ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}")
    
    # delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete confirmation","Do you want to delete this student record",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Deleted student record successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                
    # reset 
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_faculty.set("")
        self.var_radio1.set("")   
        
    ############### Generate data set or take photo sample ##############
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:    
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Faculty=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_faculty.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_std_id.get()==id+1                                                                                                                                                                
                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                #============================= load predefined data on face frontal from opencv ========================
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3  Minimum Neighbor=5
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Data set generated")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
            
if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()