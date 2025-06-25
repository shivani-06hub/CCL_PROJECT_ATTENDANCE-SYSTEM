import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3


import show_attendance
import takeImage
import trainImage
import automaticAttedance

engine = pyttsx3.init()
engine.say("Welcome! to  smartcheck")
engine.say("Please Mark you attendance")
engine.runAndWait()


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "./TrainingImageLabel/Trainner.yml"
)
trainimage_path = "Project/TrainingImage"
if not os.path.exists(trainimage_path):
    os.makedirs(trainimage_path)

employeedetails_path = (
    "Employee_Details/Employee_Details.csv"
)
attendance_path = "Attendance"

window = Tk()
window.title("SMARTcheck")
window.geometry("1920x1080")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background="#3c82c8")  



def del_sc1():
    sc1.destroy()



def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="#1c1c1c")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="white",
        bg="#1c1c1c",  
        font=("Verdana", 16, "bold"),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="white",
        bg="#333333", 
        width=9,
        height=1,
        activebackground="red",
        font=("Verdana", 16, "bold"),
    ).place(x=110, y=50)

def testVal(inStr, acttyp):
    if acttyp == "1":  
        if not inStr.isdigit():
            return False
    return True


logo = Image.open("UI_Image/0001.png")
logo = logo.resize((45, 42), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="#1c1c1c", relief=RIDGE, bd=10, font=("Verdana", 30, "bold"))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="#1c1c1c",)
l1.place(x=570, y=11)


titl = tk.Label(
    window, text="SMARTcheck", bg="#1c1c1c", fg="white", font=("Verdana", 27, "bold"),
)
titl.place(x=630, y=10)

a = tk.Label(
    window,
    text="MARK YOUR ATTENDANCE",
    bg="#3c82c8", 
    fg="black", 
    bd=50,
    font=("Verdana", 35, "bold"),
)
a.pack()


ri = Image.open("UI_Image/reg.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=150, y=270)

ai = Image.open("UI_Image/ATTENDANCE.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=1150, y=270)

vi = Image.open("UI_Image/VERIFY.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=650, y=270)


def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image..")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="#1c1c1c")  
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="#1c1c1c", relief=RIDGE, bd=10, font=("Verdana", 30, "bold"))
    titl.pack(fill=X)
   
    titl = tk.Label(
        ImageUI, text="REGISTER YOUR FACE", bg="#1c1c1c", fg="light blue", font=("Verdana", 24, "bold"),
    )
    titl.place(x=165, y=10)

   
    a = tk.Label(
        ImageUI,
        
        bg="#1c1c1c",  
        fg="white",  
        bd=10,
        font=("Verdana", 24, "bold"),
    )
    a.place(x=280, y=75)


    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=12,
        height=2,
        bg="#1c1c1c",
        fg="white",
        bd=5,
        relief=RIDGE,
        font=("Verdana", 14,"bold"),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=13,
        validate="key",
        bg="#333333", 
        fg="white", 
        relief=RIDGE,
        font=("Verdana", 18, "bold"),
    )
    txt1.place(x=300, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=12,
        height=2,
        bg="#1c1c1c",
        fg="white",
        bd=5,
        relief=RIDGE,
        font=("Verdana", 14, "bold"),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=13,
        bg="#333333",  
        fg="white", 
        relief=RIDGE,
        font=("Verdana", 18, "bold"),
    )
    txt2.place(x=300, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=12,
        height=2,
        bg="#1c1c1c",
        fg="white",
        bd=5,
        relief=RIDGE,
        font=("Verdana", 14, "bold"),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=23,
        height=2,
        bd=5,
        bg="#333333",  
        fg="white",  
        relief=RIDGE,
        font=("Verdana", 14, "bold"),
    )
    message.place(x=300, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    
    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("Verdana", 18, "bold"),
        bg="#333333",  
        fg="white",  
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=120, y=350)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    
    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("Verdana", 18, "bold"),
        bg="#333333",  
        fg="white", 
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=380, y=350)


r = tk.Button(
    window,
    text="Register a new Employee",
    command=TakeImageUI,
    bd=10,
    font=("Verdana", 16,"bold"),
    bg="black",
    fg="white",
    height=2,
    width=20,
)
r.place(x=100, y=520)


def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)


r = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attedance,
    bd=10,
    font=("Verdana", 16,"bold"),
    bg="black",
    fg="white",
    height=2,
    width=20,
)
r.place(x=600, y=520)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech)


r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("Verdana", 16,"bold"),
    bg="black",
    fg="white",
    height=2,
    width=20,
)
r.place(x=1100, y=520)
r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("Verdana", 16,"bold"),
    bg="black",
    fg="white",
    height=2,
    width=20,
)
r.place(x=600, y=660)


window.mainloop()
