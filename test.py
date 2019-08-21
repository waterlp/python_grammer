import win32com.client

s = 'sdfasdf'
u = u'dsfsa'
print(type(s))
print(type(u))
a = []
s = {i for i in range(1,10)}
print(s)

from tkinter import *


def main():
    root = Tk()
    b = Button(root, text='退出', command=root.quit)
    b.pack()
    mainloop()


if __name__ == '__main__':
    main()

