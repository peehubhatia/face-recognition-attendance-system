from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Panel")

        # Header image
        img = Image.open(r"college_images/1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img = img.resize((1366, 130))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # Background image
        bg1 = Image.open(r"college_images/1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        bg1 = bg1.resize((1366, 768))
        self.photobg1 = ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # Title section
        title_lb1 = Label(bg_img, text="Welcome to Face Recognition Panel", font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Training button
        std_img_btn = Image.open(r"college_images/1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        std_img_btn = std_img_btn.resize((180, 180))
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)
        std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
        std_b1.place(x=600, y=170, width=180, height=180)
        std_b1_1 = Button(bg_img, command=self.face_recog, text="Face Detector", cursor="hand2", font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=600, y=350, width=180, height=45)

    # Function to mark attendance
    def mark_attendance(self, i, r, n):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split(",")
                name_list.append(entry[0])

            if (i not in name_list) and (r not in name_list) and (n not in name_list):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")

    # Function for face recognition
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            try:
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

                coord = []

                for (x, y, w, h) in features:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    id, predict = clf.predict(gray_image[y:y + h, x:x + w])

                    confidence = int((100 * (1 - predict / 300)))

                    conn = mysql.connector.connect(username='root', password='Peehubhatia@123', host='localhost', database='face_recognizer')
                    cursor = conn.cursor()

                    cursor.execute("select Name from student where Student_ID=" + str(id))
                    n = cursor.fetchone()
                    if n is not None:
                        n = n[0]
                    else:
                        n = "Unknown"

                    cursor.execute("select Rollno from student where Student_ID=" + str(id))
                    r = cursor.fetchone()
                    if r is not None:
                        r = r[0]
                    else:
                        r = "Unknown"

                    cursor.execute("select Student_ID from student where Student_ID=" + str(id))
                    i = cursor.fetchone()
                    if i is not None:
                        i = i[0]
                    else:
                        i = "Unknown"

                    if confidence > 77:
                        cv2.putText(img, f"Student_ID:{i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                        cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                        cv2.putText(img, f"Roll-No:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                        self.mark_attendance(i, r, n)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                    coord = [x, y, w, y]
                return coord
            except cv2.error as e:
                print(f"OpenCV Error: {e}")
                return []

        # Function for face recognition (continued)
        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        cascade_path = os.path.abspath("haarcascade_frontalface_default.xml")
        faceCascade = cv2.CascadeClassifier(cascade_path)

        recognizer_path = os.path.abspath("classifier.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(recognizer_path)

        videoCap = cv2.VideoCapture(0)

        while True:
            ret, img = videoCap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Detector", img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

