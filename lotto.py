#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
from random import *
import time
import pygame
import tkinter.font
from tkinter import ttk
from tkinter.ttk import Combobox



history=[]

incs = 0
bloop = 0
appname = 'Lotto'

def game(event=''):

    global incs
    global bloop

    pygame.mixer.init()
    pygame.mixer.music.load('marbles-daniel_simon.wav')
    pygame.mixer.music.play()
    global hI
    bloop += 1
    for i in range(1,40):



        root.update()
        time.sleep(0.1)



        a = randint(1,99)
        b = randint(1,99)
        c = randint(1,99)
        d = randint(1,99)
        e = randint(1,99)
        f = randint(1,99)

        ent1.set(a)
        ent2.set(b)
        ent3.set(c)

#        history.append(entry1)
#        print(history)

        for stet in frame1.winfo_children():
            stet.config(fg=choice(colrs),font=('','100','bold'),bg='black',image='')

        for stlb in frame0.winfo_children():

            stlb.config(fg='white',bg='red')

        frame2.config(bg='red')


    def hist_wind():
        global window
        window=Toplevel()

        def hist():
            global hI
            global history
            global htlb
            htlb = Label(window)
            if len(history) > 0:
                del history[:]

            history.append(ent1.get())
            history.append(ent2.get())
            history.append(ent3.get())

            htlb.config(text=("{0} : {1} \n".format(hI,' '.join(map(str, history)))))
            htlb.pack()
            hI += 1
    return 0

hI = 1
colrs = ['red','blue','steelblue','brown','yellow','white']

#---root window-----

root = Tk()

def rootWindow(main):


    root.title(appname)
    root.minsize(width=1000,height=600)
    root.iconify()
    root.update()
    root.deiconify()



#helv36 = tkinter.font(family="Helvetica",size=36,weight="bold")



#---widgets packed-----

def pcks():
    #global variables
    #global entries
    global ent1,ent2,ent3

    #global frames
    global frame0,frame1,frame2

    #other vars


    #---pics-----

    incs = 0



    pic1 = PhotoImage(file='bun4.png')
    pic1 = pic1.zoom(50)  #with 250, I ended up running out of memory
    pic1 = pic1.subsample(32) #mechanically, here it is adjusted to 32 instead of 320


    #---frames----

    frame0 = Frame(root,bg='yellow',relief='groove',borderwidth=20)

    frame1 = Frame(root)



    frame2 = Frame(root,bg='steelblue')


    #---label-----

    labtitle = Label(frame0, text = appname,font=('TImes new Roman','40','bold'),bg='steelblue',fg='yellow')

    #---entry widgets-----

    ent1 = StringVar()

    entry1 = Label(frame1,textvariable = ent1,image=pic1)

    ent2 = StringVar()
    entry2 = Label(frame1,textvariable = ent2)

    ent3 = StringVar()
    entry3 = Label(frame1,textvariable = ent3)
    button=Button(frame2,text='Generate Numbers',bg='black',fg='yellow',relief='groove',borderwidth=10,font=('times','30','bold'),command = game)


    frame0.pack(side=TOP,expand=YES,fill=BOTH)
    frame1.pack(expand=YES,fill=BOTH)
    frame2.pack(side=BOTTOM,expand=YES,fill=BOTH)
    labtitle.pack(side = TOP, expand=YES , fill=BOTH)
    entry1.pack(side=LEFT)
    entry2.pack(side=LEFT)
    entry3.pack(side=LEFT)
    button.pack(side = BOTTOM)


    for stet in frame1.winfo_children():
        stet.config(width=2,relief = 'ridge',borderwidth=10,font=('','30','bold'),justify='center',state='normal',bg='red',image=pic1)
        stet.image = pic1
        stet.pack(expand=YES,fill=BOTH,ipady=20,pady=(0 ,0))
        stet.bind("<Key>", lambda e: "break")


    def anmt():
        global incs
        incs = 1
        while True:
            for stlb in frame0.winfo_children():
                if incs == 1:



                    stlb.config(bg='steelblue')
                    incs-=1

                elif incs == 0:


                    stlb.config(bg='black')
                    incs+=1





            root.update()
            time.sleep(1)
        return 0

    anmt()






def shutdownTkinter():

    try:
        global incs
        s = tkinter.messagebox.askyesno("Quit","Are you sure?")
        if s > 0:
            root.update()
            root.destroy()
    except:
        pass


#---main----

def main():

    rootWindow(root)
    pcks()

    return 0

def get_token(token_name):
    token_handler = Tokens(token_name)
    try:
        token = token_handler.get()
    except TokenException  as e:
        # write to some log file if needed
        raise e

    return token

if __name__ == '__main__':

    root.protocol("WM_DELETE_WINDOW", shutdownTkinter)

    main()





root.mainloop()
