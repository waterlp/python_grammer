def nthUglyNumber_t(m):
        # write your code here.
        # 找出m的下一个丑数
        while True:
            m += 1
            n = m
            while True:
                if n == 1:
                    break
                elif n % 2 == 0 :
                    n = int(n/2)
                    continue
                elif n % 3 == 0 :
                    n = int(n/3)
                    continue
                elif n % 5 == 0:
                    n = int(n/5)
                    continue
                else:
                    break
            if n == 1:
                break
        return m


def nthUglyNumber(k):
    # write your code here.
    # 输入m，找出第m个丑数
    all_num = []
    m = 0
    while True:
        m += 1
        n = m
        while True:
            if n == 1:
                break
            elif n % 2 == 0:
                n = int(n / 2)
                continue
            elif n % 3 == 0:
                n = int(n / 3)
                continue
            elif n % 5 == 0:
                n = int(n / 5)
                continue
            else:
                break
        if n == 1:
            all_num.append(m)
            if len(all_num) == k:
                break
    return m

if __name__ == '__main__':
    s = nthUglyNumber(599)
    print(s)