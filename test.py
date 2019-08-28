import win32com.client
import random

s = 'sdfasdf'
u = u'dsfsa'
print(type(s))
print(type(u))
a = []
s = {i*2 for i in range(1,10)}
m = [i*2 for i in range(1,10)]
print(s)
print(m)
n = set()
print(n)
print('\n')
print(type(n))
x = None
print(type(x))
q = random.choice(range(1,10))
for i in range(1,10):
    print(i)

print(q)
aa = int(253/10);
print(aa)

from tkinter import *


def main():
    root = Tk()
    b = Button(root, text='退出', command=root.quit)
    b.pack()
    # mainloop()




if __name__ == '__main__':
    main()

