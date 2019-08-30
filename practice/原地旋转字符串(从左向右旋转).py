
def rotateString(s, offset):
    s_len = len(s)
    m = ''
    while True:
        if offset<=s_len and offset != 0:
            a = s[0:s_len-offset]
            b = s[-offset:]
            m = b+a
            break
        elif offset == 0:
            m = s
            break
        else:
            offset = offset % s_len
    return m

if __name__ == '__main__':
    n = rotateString('abcdefg',3)
    print(n)

