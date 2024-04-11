from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from stud_ent import Student
from trains1 import Train
from face2 import  Face_Recognition
from attendance import Attendence_details
from developer import Developer
from help import Help
import os

class Face_Recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Reconition System")
        
        # First img
        try:
            img = Image.open(r"college_images\Stanford.jpg")
            img = img.resize((500, 130))
            self.photoimg = ImageTk.PhotoImage(img)

            f_lb1 = Label(self.root, image=self.photoimg)
            f_lb1.place(x=0, y=0, width=500, height=130)
        except Exception as e:
            print("An error occurred:", e)

        # Second img
        try:
            img1 = Image.open(r"college_images\facialrecognition.png")
            img1 = img1.resize((500, 130))
            self.photoimg1 = ImageTk.PhotoImage(img1)

            f_lb2 = Label(self.root, image=self.photoimg1)
            f_lb2.place(x=500, y=0, width=500, height=130)
        except Exception as e:
            print("An error occurred:", e)

        # Third img
        try:
            img2 = Image.open(r"college_images\u.jpg")
            img2 = img2.resize((500, 130))
            self.photoimg2 = ImageTk.PhotoImage(img2)

            f_lb3 = Label(self.root, image=self.photoimg2)
            f_lb3.place(x=1000, y=0, width=500, height=130)
        except Exception as e:
            print("An error occurred:", e)

        # bg img
        try:
            img3 = Image.open(r"college_images\bg1.jpg")
            img3 = img3.resize((1530, 710))
            self.photoimg3 = ImageTk.PhotoImage(img3)

            bg__img = Label(self.root, image=self.photoimg3)
            bg__img.place(x=0, y=130, width=1530, height=710)
        except Exception as e:
            print("An error occurred:", e)

        title_lbl=Label(bg__img,text="Face Recognition Attendance System Software",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Student button
        try:
            img4 = Image.open(r"college_images\gettyimages-1022573162.jpg")
            img4 = img4.resize((220, 220))
            self.photoimg4 = ImageTk.PhotoImage(img4)

            b1=Button(bg__img,image=self.photoimg4,command=self.student_details, cursor="hand2")
            b1.place(x=200,y=100,width=220,height=220)

            b1_1=Button(bg__img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
            b1_1.place(x=200,y=300,width=220,height=30)
        except Exception as e:
            print("An error occurred:", e)
        

    # Detect face button
        try:
            img5 = Image.open(r"college_images\face_detector1.jpg")
            img5 = img5.resize((220, 220))
            self.photoimg5 = ImageTk.PhotoImage(img5)

            b2=Button(bg__img,image=self.photoimg5,command=self.face_data,cursor="hand2")
            b2.place(x=500,y=100,width=220,height=220)

            b2_2=Button(bg__img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
            b2_2.place(x=500,y=300,width=220,height=30)
        except Exception as e:
            print("An error occurred:", e)


    # Attendance face button
        try:
            img6 = Image.open(r"college_images\report.jpg")
            img6 = img6.resize((220, 220))
            self.photoimg6 = ImageTk.PhotoImage(img6)

            b3=Button(bg__img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
            b3.place(x=800,y=100,width=220,height=220)

            b3_3=Button(bg__img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
            b3_3.place(x=800,y=300,width=220,height=30)
        except Exception as e:
            print("An error occurred:", e)


# Help button
        try:
            img7 = Image.open(r"college_images\help.jpg")
            img7 = img7.resize((220, 220))
            self.photoimg7 = ImageTk.PhotoImage(img7)

            b4=Button(bg__img,image=self.photoimg7,command=self.help_data,cursor="hand2")
            b4.place(x=1100,y=100,width=220,height=220)

            b4_4=Button(bg__img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
            b4_4.place(x=1100,y=300,width=220,height=30)
        except Exception as e:
            print("An error occurred:", e)

# Train face button
        try:
            img8 = Image.open(r"college_images\Train.jpg")
            img8 = img8.resize((220, 220))
            self.photoimg8 = ImageTk.PhotoImage(img8)

            b5=Button(bg__img,image=self.photoimg8,command=self.train_data,cursor="hand2")
            b5.place(x=200,y=350,width=220,height=220)

            b5_5=Button(bg__img,text="Train Data",cursor="hand2", command= self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
            b5_5.place(x=200,y=550,width=220,height=30)
        except Exception as e:
            print("An error occurred:", e)

# photos button
        try:
            img9= Image.open(r"college_images\opencv_face_reco_more_data.jpg")
            img9 = img9.resize((220, 220))
            self.photoimg9 = ImageTk.PhotoImage(img9)

            b6=Button(bg__img,image=self.photoimg9,command=self.open_img,cursor="hand2")
            b6.place(x=500,y=350,width=220,height=220)

            b6_6=Button(bg__img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
            b6_6.place(x=500,y=550,width=220,height=30)
        except Exception as e:
            print("An error occurred:", e)

# Developer buttom
        try:
            img10 = Image.open(r"college_images\Team-Management-Software-Development.jpg")
            img10 = img10.resize((220, 220))
            self.photoimg10 = ImageTk.PhotoImage(img10)

            b4=Button(bg__img,image=self.photoimg10,command=self.developer_data,cursor="hand2")
            b4.place(x=800,y=350,width=220,height=220)

            b4_4=Button(bg__img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
            b4_4.place(x=800,y=550,width=220,height=30)
        except Exception as e:
            print("An error occurred:", e)

# Exit button
        try:
            img11 = Image.open(r"college_images\exit.jpg")
            img11= img11.resize((220, 220))
            self.photoimg11 = ImageTk.PhotoImage(img11)

            b4=Button(bg__img,image=self.photoimg11,command=self.iExit,cursor="hand2")
            b4.place(x=1100,y=350,width=220,height=220)

            b4_4=Button(bg__img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
            b4_4.place(x=1100,y=550,width=220,height=30)
        except Exception as e:
            print("An error occurred:", e)


    def open_img(self):
        os.startfile("data")
    def iExit(self):
        self.iExit=messagebox.askyesno("Face recognition","Do you want to exit??")
        if self.iExit>0:
            self.root.destroy()
        else:
            return

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence_details(self.new_window)
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)



if __name__ == "__main__":
    root = Tk()  # Creating a tkinter instance
    obj = Face_Recognition_system(root)
    root.mainloop()
