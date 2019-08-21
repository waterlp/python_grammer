from tkinter import *

def resize(ev=None):
    label.config(font='Helvetica -%d bold' % scale.get())

top = Tk()
top.geometry('250x250')
# top.wm_geometry('150*150')

label = Label(top,text = 'hello world',font = 'Helvetica -12 bold')
label.pack(fill=Y,expand = 10)

scale = Scale(top,from_=10,to=40,orient = HORIZONTAL,command=resize)
scale.set(15)
scale.pack(fill=X,expand=1)

quit = Button(top,text = 'QUIT',command = top.quit,activebackground = 'red', activeforeground = 'white')
quit.pack()
mainloop()
