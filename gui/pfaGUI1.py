from functools import partial  # 使用偏函数
from tkinter import Tk, X, Button  # 仅仅导入tkinter模块中用到的属性
from tkinter.messagebox import showinfo, showwarning, showerror  # python 3.xb版本中对tkMessageBox重命名。这里仅仅导入三个对话框

# python2.x中使用from tkMessageBox import showinfo,showwarning,showerror

# 定义了三个标志 警告、严重、通知
WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'
SIGNS = {
    '严谨驶入': CRIT,
    '火车交汇': WARN,
    '限速': REGU,
    '错误路线': CRIT,
    '交通拥堵': WARN,
    '单行线': REGU,
    'do not': CRIT
}

# 对话框用作按钮的回调函数，将在创建每个按钮时使用他们
critCB = lambda: showerror('Error', '按下错误按钮')
warnCB = lambda: showwarning('Warning', '按下警告按钮')
infoCB = lambda: showinfo('Info', '按下通知按钮')
# 启动Tk，设置标题、位置
top = Tk()
top.title('路标')
top.geometry('250x250+700+500')  # 设置顶层窗口的属性，250x250是指窗口大小，1000+500是指窗口在屏幕上的位置
Button(top, text='退出', command=top.quit, bg='red', fg='white').pack()  # 创建一个退出按钮。设置前景色、背景色，并用Packer管理

MyButton = partial(Button, top)  # 创建了一个一阶偏函数，模板化Button类和根窗口top。MyButton效果相当于tkinter.Button() 并将top作为他的第一个参数
# 下面是三个二阶偏函数。二阶偏函数是对一阶偏函数的再次模板化。最终效果相当于使用top、回调函数和颜色这几个参数去调用Button。
CritButton = partial(MyButton, command=critCB, bg='white', fg='red')
WarnButton = partial(MyButton, command=warnCB, bg='yellow')
ReguButton = partial(MyButton, command=infoCB, bg='white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    # 构建一个可求值字符串cmd，该字符串包含按钮名、传给按钮标签的文本参数 和 pack()操作组成。如果是严重级别，会把字符大写，否则按照标题格式输出。这里还使用了三元操作符。格式化字符串的时候要注意%s和%r的区别.
    # 标题化函数title(),即所有单词的首字母都大写，其他的字母都小写
    cmd = '%sButton(text = %r%s).pack(fill = X,expand = True)' % \
          (signType.title(), eachSign, '.upper()' if signType == CRIT else '.title()')  #
    eval(cmd)  # 该函数用于执行一个字符串表达式，这里是实例化按钮

top.mainloop()  # 主循环，用于启动GUI程序