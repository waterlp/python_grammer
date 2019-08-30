# 给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：
# #
# # 如果这个数被3整除，打印fizz.
# # 如果这个数被5整除，打印buzz.
# # 如果这个数能同时被3和5整除，打印fizz buzz.
# # 如果这个数既不能被 3 整除也不能被 5 整除，打印数字本身
def fizzBuzz(n):
    array = []
    a = 'fizz'
    b = 'buzz'
    c = 'fizz buzz'
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            array.append(c)
        elif i % 3 == 0:
            array.append(a)
        elif i % 5 == 0:
            array.append(b)
        else:
            array.append(str(i))
    return array

if __name__ == '__main__':
    s = fizzBuzz(15)
    print(s)