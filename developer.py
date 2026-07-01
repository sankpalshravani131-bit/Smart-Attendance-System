from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import psycopg2
import cv2



class Devlpoer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Rocognition System")

        title_lb1=Label(self.root,text="DEVLOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lb1.place(x=0,y=0,width=1530,height=45)     

        img_top=Image.open(r"college_images\develpoer.jpg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        # Frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=1000,y=0,width=1500,height=600)

        img_top1=Image.open(r"college_images\Girl.jpg")
        img_top1=img_top1.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=200,height=200)

        # Devloper info
        dev_label=Label(main_frame,text="Hello my name,Shrawani",font=("times new roman",22,"bold"),bg="white")
        dev_label.place(x=0,y=5)




if __name__ == "__main__":
    root=Tk()
    obj=Devlpoer(root)
    root.mainloop()