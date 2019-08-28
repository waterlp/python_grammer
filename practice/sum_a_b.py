
def aplusb(a, b):
    # 输入: a = 1, b = 2
    # 输出: 3
    # 样例解释: 返回a + b的结果.
    bin_a_str = bin(a)
    bin_b_str = bin(b)
    bin_a = int(bin_a_str[2:],2)
    bin_b = int(bin_b_str[2:],2)
    if a == 0:
        return b
    if b == 0:
        return a
    summery = bin_a ^ bin_b
    carry = (bin_a & bin_b) << 1
    return aplusb(summery,carry)

def aplusb1(a, b):
    if (a & b) == 0:
        return a | b
    return aplusb(a ^ b, (a & b) << 1)

if __name__ == '__main__':
    s = aplusb(2,4)
    print(s)
    m = aplusb1(2,4)
    print(m)