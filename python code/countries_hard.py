import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
score=0
run=True

while run:
    count=0
    win_count=0
    hang=Tk()

    hang.geometry('905x700')
    hang.resizable(False,False)
    hang.title('MAIN')

    '''function for random words'''
    index=random.randint(0,9)
    file=open('countries_hard.txt','r')
    l=file.readlines()
    selected_word=(l[index].strip('/n')).upper()
    #print(selected_word)

    #hints 
    hints=open('countrieshints_hard.txt','r')
    p=hints.readlines()
    selected_hint=(p[index])
    #print(selected_hint)
    word="the word is: "+str(selected_word)

    # creation of word dashes variables
    x = 250
    for i in range(0,len(selected_word)-1):
        x += 60
        exec('d{}=Label(hang,text="_",bg="#E7FFFF",font=("arial",40))'.format(i))
        exec('d{}.place(x={},y={})'.format(i,x,450))

    #letters icon
    al = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for let in al:
        exec('{}=ImageTk.PhotoImage(file="{}.png")'.format(let,let))
        # exec('{}.resize((50,60),im.ANTIALIAS)'.format(let))

    # hangman images
    h123 = ['h1','h2','h3','h4','h5','h6','h7']
    for hangman in h123:
        exec('{}=PhotoImage(file="{}.png")'.format(hangman,hangman))

    #letters placement
    button = [['b1','A',0,595],['b2','B',70,595],['b3','C',140,595],['b4','D',210,595],['b5','E',280,595],['b6','F',350,595],['b7','G',420,595],['b8','H',490,595],['b9','I',560,595],['b10','J',630,595],['b11','K',700,595],['b12','L',770,595],['b13','M',840,595],['b14','N',0,645],['b15','O',70,645],['b16','P',140,645],['b17','Q',210,645],['b18','R',280,645],['b19','S',350,645],['b20','T',420,645],['b21','U',490,645],['b22','V',560,645],['b23','W',630,645],['b24','X',700,645],['b25','Y',770,645],['b26','Z',840,645]]

    for q1 in button:
        exec('{}=Button(hang,bd=0,command=lambda:check("{}","{}"),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image={})'.format(q1[0],q1[1],q1[0],q1[1]))
        exec('{}.place(x={},y={})'.format(q1[0],q1[2],q1[3]))


    #hangman placement
    han = [['c1','h1'],['c2','h2'],['c3','h3'],['c4','h5'],['c5','h7']]
    for p1 in han:
        exec('{}=Label(hang,bg="#E7FFFF",image={})'.format(p1[0],p1[1]))    

    # placement of first hangman image
    c1.place(x = 400,y = -50)


    #hint button
    hintpic=PhotoImage(file = "Hint.png")
    df=Label(hang,text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    df.grid(row=0,column=0)
    hangbutton=Button(hang,bd=0,command=lambda:hintshow(),bg="#E7FFFF",activebackground="#E7FFFF",font=10,image=hintpic)
    hangbutton.grid(row=5,column=1)


    #hint function
    def hintshow():
        dq=Label(hang,text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        dq.grid(row=0,column=0)
        hangbutton.destroy()
        hi1=Label(hang,text=selected_hint,bg="#E7FFFF",font=("The Times New Roman",12))
        hi1.grid(row=5,column=1)

    # exit buton
    def close():
        global run
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')
        if answer == True:
            run = False
            hang.destroy()
            
    e1 = PhotoImage(file = 'exit.png')
    ex = Button(hang,bd = 0,command = close,bg="#E7FFFF",activebackground = "#E7FFFF",font = 10,image = e1)
    ex.place(x=770,y=10)
    s2 = 'SCORE:'+str(score)
    s1 = Label(hang,text = s2,bg = "#E7FFFF",font = ("arial",25))
    s1.place(x = 10,y = 10)

    def check(letter,button):
        global count,win_count,run,score
        exec('{}.destroy()'.format(button))
        if letter in selected_word:
            for i in range(0,len(selected_word)-1):
                
                if selected_word[i] == letter:
                    win_count += 1
                    
                    exec('d{}.config(text="{}")'.format(i,letter.upper()))

            
            if win_count == len(selected_word)-1:
                score += 1
                
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    hang.destroy()   
                else:
                    run = False
                    hang.destroy()
        else:
            count += 1
            exec('c{}.destroy()'.format(count))
            exec('c{}.place(x={},y={})'.format(count+1,400,-50))
            if count == 4:
                messagebox.showinfo("revealed word",word)
                answer = messagebox.askyesno('GAME OVER','YOU LOST!\nWANT TO PLAY AGAIN?')
                if answer == True:
                    run = True
                    score = 0
                    hang.destroy()
                else:
                    run = False
                    hang.destroy()
        

    hang.config(bg='#E7FFFF')
    hang=mainloop()