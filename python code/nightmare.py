import time
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
score=0
play=True
hello=0
bye=0
end=0

while play:
    count=0
    win_count=0
    hang=Tk()

    hang.attributes('-fullscreen', True)
    hang.resizable(False,False)

    #45
    hour=StringVar()
    minute=StringVar()
    second=StringVar()

    hour.set("00")
    minute.set("00")
    second.set("15")
    secondEntry= Label(hang, width=3,bg="black", fg="white",font=("Arial",80),
                    textvariable=second)
    secondEntry.place(x=600,y=250)
    def submit():
        
        global play,bye,end
        
        try:
        
            temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
            print("Please input the right value")
        while temp >-1:
            
            mins,secs = divmod(temp,60)
            second.set("{0:2d}".format(secs))
            hang.update()
            time.sleep(1)
            try:
                
                if (temp == 0 and 'normal'==hang.state()):
                    
                    messagebox.showinfo("Time Countdown", "Time's up ")
                    messagebox.showinfo("YOU LOST","ENDING THE NIGHTMARE MODE")
                    os.startfile(r'hangman.py')
                    play=False
                    end=1
                    hang.destroy()
                    return None
                elif(hello==-1 and bye==0):
                    os.startfile(r'hangman.py')
                    bye=1
                    
            except:
                print("")
            temp -= 1
    

    '''word selection'''
    selected_word="pneumonoultramicroscopicsilicovolcanoconiosis".upper()
    
    selected_hint="Refering to lung desease cause by silica dust"
    #heading
    l2=Label(hang,text="NIGHTMARE MODE ACTIVATED, TRY TO WIN!!!!",font=('chiller 65 bold'),background="black",foreground="red").pack()

    x = -20
    for i in range(0,44):
        x += 34
        exec('d{}=Label(hang,text="_",bg="black",fg="white",font=("arial",35))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,450))

    #letters icon
    al = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for let in al:
        exec('{}=ImageTk.PhotoImage(file="{}.png")'.format(let,let))
    button = [['b1','A',280,735],['b2','B',350,735],['b3','C',420,735],['b4','D',490,735],['b5','E',560,735],['b6','F',630,735],['b7','G',700,735],['b8','H',770,735],['b9','I',840,735],['b10','J',910,735],['b11','K',980,735],['b12','L',1050,735],['b13','M',1120,735],['b14','N',280,800],['b15','O',350,800],['b16','P',420,800],['b17','Q',490,800],['b18','R',560,800],['b19','S',630,800],['b20','T',700,800],['b21','U',770,800],['b22','V',840,800],['b23','W',910,800],['b24','X',980,800],['b25','Y',1050,800],['b26','Z',1120,800]]

    for q1 in button:
        exec('{}=Button(hang,bd=0,command=lambda:check("{}","{}"),bg="black",fg="white",activebackground="black",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))
    def close():
        global play
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            play = False
            hang.destroy()
        
    e1 = PhotoImage(file = 'exit.png')
    ex = Button(hang,bd = 0,command =lambda: close(),bg="black",activebackground = "black",font = 10,image = e1)
    ex.place(x=1400,y=130)
    s2 = 'SCORE:'+str(score)
    s1 = Label(hang,text = s2,bg = "black",fg="white",font = ("arial",25))
    s1.place(x = 10,y = 130)
    

    def check(letter,button):
        
        global count,win_count,play,score,hello
        exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(0,44):
                
                
                if selected_word[i] == letter:
                    win_count += 1
                    
                    exec('d{}.config(text="{}",fg="white")'.format(i,letter.upper()))

            
            if win_count == 44:
                score += 1
                
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    hello=0
                    play = True
                    hang.destroy()   
                else:
                    hello=-1
                    play = False
                    hang.destroy()
        else:
            count += 1
            if count == 2:
                # messagebox.showinfo("revealed word",word)
                answer = messagebox.askyesno('GAME OVER','YOU LOST!\nWANT TO PLAY AGAIN?')
                
                if answer == True:
                    hello=0
                    play = True
                    score = 0
                    hang.destroy()
                else:
                    hello=-1
                    play = False
                    hang.destroy()
    hang.config(bg='black')
    btn = Button(hang, text='Set Time Countdown', bd='5',
                command= submit)
    btn.place(x = 1700,y = 200)
    print(end)
    if hello==0 and end==0:
        result=messagebox.askyesno("READY","ARE YOU READY \n COUNTDOWN GOING TO START")
        if result==True:
            btn.invoke()
            
            play=True
        else:
            os.startfile(r'hangman.py')
            play=False
            hang.destroy()
    else:
        play=False
        
        hang.destroy()
    
    hang.mainloop()
