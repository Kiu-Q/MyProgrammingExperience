# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 10:39:32 2022

@author: user
"""
def onPress():
    global count
    count+=1
    buttonText.set('pressed '+str(count)+' time(s)')
import tkinter as t
win=t.Tk()
count=0
buttonText=t.StringVar()
win.title('siufa')
button1=t.Button(win, textvariable=buttonText, command=onPress)
buttonText.set('press me')
button1.pack()
win.mainloop()