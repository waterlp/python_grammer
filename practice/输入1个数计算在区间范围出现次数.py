
def digitCounts(k,n):
    # k = 1, n = 12
    # 输出：
    # 5
    # 解释：
    # 在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 中，我们发现 1 出现了 5 次 (1, 10, 11, 12)(注意11中有两个1)
    m = [i for i in  range(0,n+1)]
    count = 0
    for num in m:
        while num>0:

        if (num%10=k):
            count += 1

if __name__ == '__main__':
    s = digitCounts(12)
    print(s)
