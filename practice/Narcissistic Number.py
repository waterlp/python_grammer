# Narcissistic Number是一个数字，它是各自数字的总和，每个数字都是数字的幂。见维基
#
# 例如，3位十进制数153是一个自恋数，因为153 = 1 **3 + 5 **3 + 3 **3。
#
# 并且4位十进制数1634是一个自恋数字，因为1634 = 1 4 + 6 4 + 3 4 + 4 4。
#
# 给定n，返回所有n个数字的自恋数字。


def fun(n):
    # 先判定是不是自恋数字
    max = 10**n
    min = 10**(n-1)
    Narcissistic = []
    if n == 1:
        Narcissistic.append(0)
    for num in range(min,max):
        num = str(num)
        sum = 0
        for i in range(0,n):
            sum += int(num[i])**n
        if sum == int(num):
            Narcissistic.append(num)

    return  Narcissistic

if __name__ == '__main__':
    s = fun(3)
    print(s)














