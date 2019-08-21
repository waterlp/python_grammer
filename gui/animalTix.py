from tkinter import Label,Button,END,Tk

top = Tk()
top.tk.eval('package require Tix')

lb = Label(top,text='Animals (in pairs;min:pair,max:dozen)')
lb.pack()

ct = Con