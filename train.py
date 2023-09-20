from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np
class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("OM Face Recognition")

        title_lbl=Label(self.root,text="Train Dataset",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=-150,y=0,width=1500,height=45)

        # Image on the left label
        img_top=Image.open(r"C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\facepic.png")
        img_top=img_top.resize((1530,320),Image.ANTIALIAS)
        self.photo_top=ImageTk.PhotoImage(img_top)

        l_lbl=Label(self.root,image=self.photo_top)
        l_lbl.place(x=0,y=50,width=1530,height=320)
        #button
        b1_l=Button(self.root,text=" Train Data ",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="white")
        b1_l.place(x=0,y=380,width=1530,height=60)

    def train_classifier(self):
        data_dir=(r"C:\Users\PRACHI SINGH\Desktop\OM PYTHON\New folder\New folder\data")
        
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')#grayscale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        #using classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Trainning Dataset Completed.")
    


if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
