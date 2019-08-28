# Narcissistic Number是一个数字，它是各自数字的总和，每个数字都是数字的幂。见维基
#
# 例如，3位十进制数153是一个自恋数，因为153 = 1 3 + 5 3 + 3 3。
#
# 并且4位十进制数1634是一个自恋数字，因为1634 = 1 4 + 6 4 + 3 4 + 4 4。
#
# 给定n，返回所有n个数字的自恋数字。


def fun(n):
    # 先判定是不是自恋数字
    if isinstance(n,int):
        all = []
        for k in range(1,n+1):
            num = []
            sum = 0
            while(True):
                m = k%10
                num.append(m)
                n = int(k/10)
                if n == 0 :
                    break
            for i in num:
                 sum += i**2
            if k == sum & k!= 0:
                all.append(n)
        return all
    else:
        print("n is not int,please input again")




if __name__ == '__main__':
    print(fun(153))