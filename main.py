from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
import tkinter
from train import Train
from face_recognition import face_recognition
from attendence import Attendence
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("OM Face Recognition")

        #first
        img=Image.open(r"C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\face_header.jpg")
        img=img.resize((1500,130),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photo)
        f_lbl.place(x=0,y=0,width=1500,height=150)

        #background image
        img3=Image.open(r"C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\white.jpg")
        img3=img3.resize((1500,710),Image.ANTIALIAS)
        self.bgphoto=ImageTk.PhotoImage(img3)

        bg_lbl=Label(self.root,image=self.bgphoto)
        bg_lbl.place(x=0,y=100,width=1500,height=710)

        title_lbl=Label(bg_lbl,text="FACE RECOGNITION SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=-150,y=0,width=1500,height=45)
        
        #student button
        img4=Image.open(r"C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\stu_image.jpg")
        img4=img4.resize((300,180),Image.ANTIALIAS)
        self.stuphoto=ImageTk.PhotoImage(img4)

        b1=Button(bg_lbl,image=self.stuphoto,cursor="hand2",command=self.student_details)
        b1.place(x=80,y=100,width=300,height=180)
         
        b1_l=Button(bg_lbl,text="Student Details ",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_l.place(x=80,y=250,width=300,height=40)

        #detect face button
        img5=Image.open(r"C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\detect_face.jpeg")
        img5=img5.resize((300,180),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_lbl,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=465,y=100,width=300,height=180)
         
        b1_l=Button(bg_lbl,text="Face Detector ",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_l.place(x=465,y=250,width=300,height=40)

        #train facebutton
        img8=Image.open(r"C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\train.png")
        img8=img8.resize((300,180),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
    
        b1=Button(bg_lbl,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=850,y=100,width=300,height=180)

        b1_l=Button(bg_lbl,text=" Train Data ",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_l.place(x=850,y=250,width=300,height=40)

        # photos face button
        img9=Image.open(r"C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\image.png")
        img9=img9.resize((300,180),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
       
        b1=Button(bg_lbl,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=300,y=300,width=300,height=180)
       
        b1_l=Button(bg_lbl,text=" Photos ",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_l.place(x=300,y=450,width=300,height=40)

        # Exit  button
        img11=Image.open(r"C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\exit.png")
        img11=img11.resize((300,180),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_lbl,image=self.photoimg11,cursor="hand2",command=self.exit)
        b1.place(x=700,y=300,width=300,height=180)
       
        b1_l=Button(bg_lbl,text=" Exit ",cursor="hand2",command=self.exit,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_l.place(x=700,y=450,width=300,height=40)

    def open_img(self):
        # os.startfile("data")
        os.startfile(r'C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\New folder\data')


        #functions for new window
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
       #train 
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        #face recognition function
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)
        #attendence
    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)
    #exit
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit ?",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return

    


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()