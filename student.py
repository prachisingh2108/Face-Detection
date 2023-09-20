from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("OM Face Recognition")

        #variables to add data
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_stuid=StringVar()
        self.var_stu_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
      
         #first
        img=Image.open(r"C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\face_header.jpg")
        img=img.resize((1500,130),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photo)
        f_lbl.place(x=0,y=0,width=1500,height=150)

        #bg
        img3=Image.open(r"C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\white.jpg")
        img3=img3.resize((1500,710),Image.ANTIALIAS)
        self.bgphoto=ImageTk.PhotoImage(img3)

        bg_lbl=Label(self.root,image=self.bgphoto)
        bg_lbl.place(x=0,y=100,width=1500,height=710)

        title_lbl=Label(bg_lbl,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=-150,y=0,width=1500,height=45)

        #frame bna rhe hai
        main_frame=Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=0,y=55,width=1500,height=600)

        #left label
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text=" Student Details ",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=0,width=600,height=480)
      
        #current course information just below left image
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text=" Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=0,width=580,height=115)

        dep_lbl=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_lbl.grid(row=0,column=0)
        #department
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical","MCA")
        dep_combo.current(0)#for select department option
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,pady=10,sticky=W)

        #Year 
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","2020-21","20210-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select your Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=3,pady=10,sticky=W)

        #Class student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text=" Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=120,width=585,height=330)
        #student id
        studentID_label=Label(class_student_frame,text="Student ID :",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #Text field
        studentID_entry=ttk.Entry(class_student_frame,width=15,textvariable=self.var_stuid,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #student name
        studentName_label=Label(class_student_frame,text="Student Name :",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        #Text field
        studentName_entry=ttk.Entry(class_student_frame,width=21,textvariable=self.var_stu_name,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,sticky=W)

        #class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=10)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)


        #roll no
        rollno_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        #Text field
        rollno_entry=ttk.Entry(class_student_frame,width=21,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        rollno_entry.grid(row=1,column=3,sticky=W)

        #gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #Text field
        # gender_entry=ttk.Entry(class_student_frame,width=15,textvariable=self.var_gender,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=10)
        gender_combo["values"]=("Female","Male","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)


        #dob
        dob_label=Label(class_student_frame,text="Date of Birth:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        #Text field
        dob_entry=ttk.Entry(class_student_frame,width=21,textvariable=self.var_dob,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,sticky=W)

        #email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        #Text field
        email_entry=ttk.Entry(class_student_frame,width=15,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #phone
        phone_label=Label(class_student_frame,text="Phone:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        #Text field
        phone_entry=ttk.Entry(class_student_frame,width=21,textvariable=self.var_phone,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,sticky=W)

        #address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        #Text field
        address_entry=ttk.Entry(class_student_frame,width=15,textvariable=self.var_address,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        #teachername
        teachername_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teachername_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        #Text field
        teachername_entry=ttk.Entry(class_student_frame,width=21,textvariable=self.var_teacher,font=("times new roman",12,"bold"))
        teachername_entry.grid(row=4,column=3,sticky=W)

        #radio button with the help of ttk
        self.var_radio1=StringVar()
        rd1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text=" Take a photo sample.",value="Yes")
        rd1.grid(row=6,column=0)
        rd2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text=" No photo sample.",value="No")
        rd2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=210,width=570,height=35)

        #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=20 ,font=("times new roman",12,"bold"),bg="black",fg="white")
        save_btn.grid(row=0,column=0)

        #update button
        update_btn=Button(btn_frame,text="Update", width=20 , command=self.update_data,font=("times new roman",12,"bold"),bg="black",fg="white")
        update_btn.grid(row=0,column=1)

        #delete button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data, width=20 ,font=("times new roman",12,"bold"),bg="black",fg="white")
        delete_btn.grid(row=0,column=2)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=10,y=245,width=560,height=35)
        #take a photo sample btn
        take_phto_btn=Button(btn_frame1,text="Take a photo sample.",command=self.generate_dataset, width=30 ,font=("times new roman",12,"bold"),bg="black",fg="white")
        take_phto_btn.grid(row=0,column=0)
        
        #reset 
        reset_btn=Button(btn_frame1,text=" Reset", command=self.reset,width=30 ,font=("times new roman",12,"bold"),bg="black",fg="white")
        reset_btn.grid(row=0,column=1)
        
        #right label 
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        right_frame.place(x=620,y=0,width=630,height=480)

        #Image on the Right label
        img_right=Image.open(r"C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\students.webp")
        img_right=img_right.resize((600,110),Image.ANTIALIAS)
        self.photo_right=ImageTk.PhotoImage(img_right)

        r_lbl=Label(right_frame,image=self.photo_right)
        r_lbl.place(x=10,y=10,width=600,height=100)

        #table frame
        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        table_frame.place(x=5,y=120,width=615,height=350)
        #scrollbar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("Department","Course","Year","Sem","id","name","div","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        #to show header
        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Sem")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="Date of Birth")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone Number")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        #function to add data in the database
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()==""or self.var_stuid.get()=="":
            messagebox.showerror("Error","All fills are mandatory",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face")
                my_curser=conn.cursor()
                my_curser.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_stuid.get(),
                                self.var_stu_name.get(),
                                self.var_div.get(),
                                self.var_roll.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                self.var_teacher.get(),
                                self.var_radio1.get()
                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face")
        my_curser=conn.cursor()
        my_curser.execute("Select * from student")
        data=my_curser.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_stuid.set(data[4]),
        self.var_stu_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()==""or self.var_stuid.get()=="":
            messagebox.showerror("Error","All fills are mandatory",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update ?",parent=self.root)
                if Update>0:
                    #create connection
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face")
                    my_curser=conn.cursor()
                    my_curser.execute("UPDATE student SET Department=%s,course=%s,year=%s,name=%s,semester=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where StudentID=%s",(
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_stu_name.get(),
                                self.var_semester.get(),
                                self.var_div.get(),
                                self.var_roll.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                self.var_teacher.get(),
                                self.var_radio1.get(),
                                self.var_stuid.get()
                                ))
                else:
                    if  not Update:
                        return  
                messagebox.showinfo("Success","Student details updates",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=root)      
    #delete
    def delete_data(self):
        if self.var_stuid.get()=="":
            messagebox.showerror("Error","Student Id must be required.",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to this student ?",parent=self.root)

                if delete>0:
                     #create connection
                    conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face")
                    my_curser=conn.cursor()
                    #another way of writing a query
                    sql="delete from student where StudentID=%s"
                    val=(self.var_stuid.get(),)
                    my_curser.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details,",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=root)
    #reset
    def reset(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_stuid.set("")
        self.var_stu_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Female")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
    #photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_stu_name.get()==""or self.var_stuid.get()=="":
            messagebox.showerror("Error","All fills are mandatory",parent=self.root)
        else:
            try:
                #create connection
                conn=mysql.connector.connect(host="localhost",username="root",password="12345",database="face")
                my_curser=conn.cursor()
                my_curser.execute("Select * from student")
                myresult=my_curser.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_curser.execute("UPDATE student SET Department=%s,course=%s,year=%s,name=%s,semester=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where StudentID=%s",(
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_stu_name.get(),
                                self.var_semester.get(),
                                self.var_div.get(),
                                self.var_roll.get(),
                                self.var_gender.get(),
                                self.var_dob.get(),
                                self.var_email.get(),
                                self.var_phone.get(),
                                self.var_address.get(),
                                self.var_teacher.get(),
                                self.var_radio1.get(),
                                self.var_stuid.get()==id+1
                                ))
                conn.commit()
                self.fetch_data()
                self.reset()
                conn.close()

                #loading frontal face
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                # face_classifier=cv2.CascadeClassifier(r"C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\New folder \haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #1.3 Scaling factor
                    #minimum neighbour=5
                    for (x,y,w,h)in faces:
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
                        # file_name_path="C:/Users/PRACHI SINGH/Desktop/OM PYTHON/New folder/New folder/data/user."+str(id)+"."+str(img_id)+".jpg"
                        file_name_path="C:/Users/PRACHI SINGH/Desktop/OM PYTHON/New folder/New folder/data/user."+str(id)+"."+str(img_id)+".jpg"
                        # file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed.!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=root)
            


 




if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()