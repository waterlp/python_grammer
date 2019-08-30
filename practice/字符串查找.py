
def strStr(source, target):
    len_s = len(source)
    len_t = len(target)
    if len_s < len_t:
        return -1
    elif len_s == len_t:
        if source == target :
            return 0
        else:
            return -1
    else:
        j = 0
        for i in range(0,len_s-len_t+1):
            tmp = source[i:i+len_t]
            if target == tmp:
                j += 1
                return i
        if j==0:
            return -1



if __name__ == '__main__':
    source = ''
    target = ''
    s = strStr(source,target)
    print(s)