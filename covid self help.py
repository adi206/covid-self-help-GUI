import datetime
from tkinter import  *
from tkinter import filedialog, Text
import os
from plyer import notification
import time

def notifyme():
   notification.notify(
        title = "Hey user",
        message = "Dont forget to take medication according to prescription",
        timeout = 8,
        )
def enter():
    screen2 = Toplevel(screen)
    screen2.title("PRESCRIPTION")
    screen2.configure(background="blue")
    Label(screen2,text="tablets\n 1.paracetamol-1-0-1\n 2.azithromycin-1-0-1\n 3.doxycycline-1-0-0\n 4.zinc-1-0-0\n 5.vitamin C-0-1-0\n 6.steam-twice a day",bg="blue",font="Bold").pack()
    screen2.geometry("300x250")
    Button(screen2, text = "Notify Me", height="2",width="30",bg="red",command=lambda: notifyme() ).pack()
    Button(screen2, text="Quit", height="2", width="30", bg="red",command=lambda: screen2.quit()).pack()
def register():
    screen1 = Toplevel(screen)
    screen1.title("COVID SELF HELP" )
    screen1.configure(background="yellow")
    screen1.geometry("300x250" )

    Name = StringVar()
    Mobile_number = StringVar()

    Label(screen1, text ="Name * ", bg = "green",font="Bold").pack()
    Name=Entry(screen1, textvariable = Name).pack()
    Label(screen1, text ="Mobile_number * ",bg="green",font="Bold").pack()
    Mobile_number=Entry(screen1, textvariable = Mobile_number).pack()
    Button(screen1, text="Enter", height="2", width="30",bg="red", command = enter).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x200")
    screen.title("page2")
    Label(text = "COVID SELF HELP", bg = "green",fg="black", width = "300", height ="2", font = ("Calibri", 131)).pack()
    Label(text="GET WELL SOON",bg ="green",width="500",height="1", font="Bold").pack()

    Label(text="").pack()
    Button(text = "Register",height="2",width="30",bg="red",font="bold",command = register,).pack()

    screen.mainloop()

if __name__ == '__main__':
    main_screen()





