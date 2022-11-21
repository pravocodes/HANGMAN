import os
from tkinter import *
from tkinter import messagebox
from turtle import left
def easyflower():
    os.startfile(r'flower_easy.py')
    level.destroy()
def mediumflower():
    os.startfile(r'flower_medium.py')
    level.destroy()
def hardflower():
    os.startfile(r'flower_hard.py')
    level.destroy()
def easyinfo():
    messagebox.showinfo("easy rules","You have 6 Chances to win the game othwise your man will be hanged")
def mediuminfo():
    messagebox.showinfo("medium rules","You have 5 Chances to win the game othwise your man will be hanged")
def hardinfo():
    global b
    b+=1
    if(b<3):
        messagebox.showinfo("hard rules","You have 4 Chances to win the game othwise your man will be hanged")
    else:
        os.startfile(r'nightmare.py')
        level.destroy()
level=Tk()
level.title('LEVELS')
b=0
level.geometry('300x350')
level.resizable(False,False)
head = Label(level, text ="Choose the level\nof difficulty.",fg='#D0312D',bg='#C2DFFF',font=("arial",30)).pack()
p1=PhotoImage(file="desc.png")
photo1=PhotoImage(file = r"easy.png")
photo2=PhotoImage(file = r"medium.png")
photo3=PhotoImage(file = r"hard.png")
Button(level, text = 'Easy', image = photo1,command=lambda:easyflower()).place(x=90,y=120)
Button(level, text = 'Medium', image = photo2,command=lambda:mediumflower()).place(x=80,y=200)
Button(level, text = 'Hard', image = photo3,command=lambda:hardflower()).place(x=90,y=280)
Button(level,image=p1,command=lambda:easyinfo()).place(x=210,y=120)
Button(level,image=p1,command=lambda:mediuminfo()).place(x=230,y=200)
Button(level,image=p1,command=lambda:hardinfo()).place(x=213,y=280)
level.config(bg='#C2DFFF')
level.mainloop()
