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
class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("OM Face Recognition")
        img=Image.open(r"C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\face_header.jpg")
        img=img.resize((1500,150),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(img)
        
        #text variables
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendence=StringVar()


        f_lbl=Label(self.root,image=self.photo)
        f_lbl.place(x=0,y=0,width=1500,height=150)

        #bg
        img3=Image.open(r"C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\white.jpg")
        img3=img3.resize((1500,710),Image.ANTIALIAS)
        self.bgphoto=ImageTk.PhotoImage(img3)

        bg_lbl=Label(self.root,image=self.bgphoto)
        bg_lbl.place(x=0,y=100,width=1500,height=710)

        title_lbl=Label(bg_lbl,text="ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=-150,y=0,width=1500,height=45)
        #one big frame
        main_frame=Frame(bg_lbl,bd=2,bg="white")
        main_frame.place(x=0,y=55,width=1500,height=600)
        #left frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=0,width=600,height=480)
        #left inside frame
        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=12,y=10,width=570,height=300)
        #label and entries
        #attnendence
        attendendeID_label=Label(left_inside_frame,text="Attendence ID :",font=("times new roman",12,"bold"),bg="white")
        attendendeID_label.grid(row=0,column=0,padx=15,pady=10,sticky=W)

        attendendeID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_id,width=21,font=("times new roman",12,"bold"))
        attendendeID_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)
        
        #roll
        roll_label=Label(left_inside_frame,text="Roll :",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend_roll,font=("times new roman",12,"bold"))
        roll_entry.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #name
        name_label=Label(left_inside_frame,text="Name :",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=15,pady=10,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,width=21,textvariable=self.var_attend_name,font=("times new roman",12,"bold"))
        name_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

        #time 
        time_label=Label(left_inside_frame,text="Time :",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=1,column=2,padx=5,pady=10,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend_time,font=("times new roman",12,"bold"))
        time_entry.grid(row=1,column=3,padx=5,pady=10,sticky=W)

        #department
        department_label=Label(left_inside_frame,text="Department :",font=("times new roman",12,"bold"),bg="white")
        department_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        department_entry=ttk.Entry(left_inside_frame,width=21,textvariable=self.var_attend_dep,font=("times new roman",12,"bold"))
        department_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #date
        date_label=Label(left_inside_frame,text="Date :",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=5,pady=10,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_attend_date,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #attendence
        dep_lbl=Label(left_inside_frame,text="Attendence",textvariable=self.var_attend_attendence,font=("times new roman",12,"bold"),bg="white")
        dep_lbl.grid(row=3,column=0,padx=10,pady=10)
    
        dep_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_attend_attendence,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Status","Present","Absent")
        dep_combo.current(0)#for select department option
        dep_combo.grid(row=3,column=1,padx=10,pady=10)

        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=210,width=545,height=35)

        #Import CSV
        save_btn=Button(btn_frame,text="Import CSV",command=self.import_csv,width=19,font=("times new roman",12,"bold"),bg="black",fg="white")
        save_btn.grid(row=0,column=0)

        #Export CSV
        update_btn=Button(btn_frame,text="Export CSV", command=self.export_csv,width=19 ,font=("times new roman",12,"bold"),bg="black",fg="white")
        update_btn.grid(row=0,column=1)

        #Update
        # delete_btn=Button(btn_frame,text="Update", width=14 ,font=("times new roman",12,"bold"),bg="black",fg="white")
        # delete_btn.grid(row=0,column=2)

        #reset button
        reset_btn=Button(btn_frame,text=" Reset",width=19,command=self.reset,font=("times new roman",12,"bold"),bg="black",fg="white")
        reset_btn.grid(row=0,column=2)

        #right frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman",12,"bold"))
        right_frame.place(x=620,y=0,width=630,height=480)
        #table frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=10,width=604,height=350)
        #scrollbar and table
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        #attendence table in python
        self.AttendenceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendenceReportTable.xview)
        scroll_y.config(command=self.AttendenceReportTable.yview)

        self.AttendenceReportTable.heading("id",text="Attendence ID")
        self.AttendenceReportTable.heading("roll",text="Roll No.")
        self.AttendenceReportTable.heading("name",text="Name")
        self.AttendenceReportTable.heading("department",text="Deparmtent")
        self.AttendenceReportTable.heading("time",text="Time")
        self.AttendenceReportTable.heading("date",text="Date")
        self.AttendenceReportTable.heading("attendence",text="Attendence")
        
        self.AttendenceReportTable["show"]="headings"

        self.AttendenceReportTable.column("id",width=100)
        self.AttendenceReportTable.column("roll",width=100)
        self.AttendenceReportTable.column("name",width=100)
        self.AttendenceReportTable.column("department",width=100)
        self.AttendenceReportTable.column("time",width=100)
        self.AttendenceReportTable.column("date",width=100)
        self.AttendenceReportTable.column("attendence",width=100)
         
        self.AttendenceReportTable.pack(fill=BOTH,expand=1)
        self.AttendenceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #fetch_data
    def fetch_data(self,rows):
        self.AttendenceReportTable.delete(*self.AttendenceReportTable.get_children())
        for i in rows:
            self.AttendenceReportTable.insert("",END,values=i)

    def import_csv(self):
        global mydata
        mydata.clear()
        fname=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fname) as myfile:
            csv_read=csv.reader(myfile,delimiter=",")
            for i in csv_read:
                mydata.append(i)
            self.fetch_data(mydata)
    #export csv
    def export_csv(self):
        #to check whether the table is empty
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found",parent=self.root)
                return False
            else:
                #file bna rhe hai to export
                fname=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
                with open(fname,mode="w",newline="\n") as myfile:
                    exp_write=csv.writer(myfile,delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fname)+" successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=root)
    def get_cursor(self,event=""):
        cursor_row=self.AttendenceReportTable.focus()
        content=self.AttendenceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendence.set(rows[6])

    #reset
    def reset(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendence.set("")






if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)
    root.mainloop()