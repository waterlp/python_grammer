import tkinter

top = tkinter.Tk()
hello = tkinter.Label(top,text = 'hello world')
hello.pack()
quit = tkinter.Button(top,text = 'QUIT',command = top.quit,bg = 'red', fg = 'white')
quit.pack(fill = tkinter.X,expand = 1)
# top.quit()
tkinter.mainloop()
