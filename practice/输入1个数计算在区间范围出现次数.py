
def digitCounts(k,n):
    # k = 1, n = 12
    # 输出：
    # 5
    # 解释：
    # 在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 中，我们发现 1 出现了 5 次 (1, 10, 11, 12)(注意11中有两个1)
    m = [i for i in  range(0,n+1)]
    count = 0
    k = str(k)
    len_k = len(k)
    for j in m:
        tmp = str(j)
        len_tmp = len(tmp)
        if k in tmp:
            sum = []
            for a in range(0, len_tmp - len_k + 1):
                q = ''
                for b in range(a, a + len_k):
                    q += (tmp[b])
                if q == k:
                    count += 1
    return count


if __name__ == '__main__':
    s = digitCounts(11,1010)
    print(s)

    #获取数组
    # s = 'addsd'
    # s_n = len(s)
    # n = 2
    # sum = []
    # for j in range(0,s_n-n+1):
    #     q = ''
    #     for i in range(j,j+n):
    #         q += (s[i])
    #     sum.append(q)
    # print(sum)

