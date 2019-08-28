
def trailingZerosx(n):
    # 样例  1:
    # 	输入: 11
    # 	输出: 2
    # 	样例解释:
    # 	11! = 39916800, 结尾的0有2个。
    point = 1
    while(n>=1):
        point *= n
        n -= 1
    count = 0
    print(point)
    while point:
        if point % 10 == 0:
            count += 1
        else:
            break
        point = int(point/10)
    return count

def trailingZeros(n):
    count = 0
    while (n>0):
        n = int(n/5)
        count += n
    return count

if __name__ == '__main__':
    s = trailingZeros(105)
    print(s)
