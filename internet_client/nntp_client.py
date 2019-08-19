import nntplib
import socket
import re

GRNM = 'comp.lang.python'
USER = 'wesley'
PASS = 'youllNeverGuess'


def main():
    try:
        """连接目标服务器"""
        host = input("Please input your host,else backspace\n")
        if host != "":
            HOST = host
        else:
            HOST = 'nntp.aioe.org'
        n = nntplib.NNTP(HOST)
    # ,user=USER,password=PASS
    except socket.gaierror as e:
        print('ERROR:cannot reach host "%s"' % HOST)
        print('   ("%s")' % str(e))
        return
    except nntplib.NNTPTemporaryError as e:
        print('ERROR:access denied on "%s"' % HOST)
        print('    ("%s")' % str(e))
        return
    print('*** Connected to host "%s"' % HOST)

    try:
        rsp, ct, fst, lst, grp = n.group(GRNM)  # 返回服务器响应信息、文章数量、第一个和最后一个文章的编号、组名
    except nntplib.NNTPTemporaryError as e:
        print('ERROR: cannot load group "%s"' % GRNM)
        print('    ("%s")' % str(e))
        print('    Server may require authentication')
        print('    Uncomment/edit login line above')
        n.quit()
        return
    except nntplib.NNTPTemporaryError as e:
        print('ERROR: group "%s" unavailable' % GRNM)
        print('    ("%s")' % str(e))
        n.quit()
        return
    print('*** Found newsgroup "%s"' % GRNM)

    search_next(fst, lst, n)


def search_next(fst, lst, n):
    """查找符合关键字的文章标题"""
    dic_1 = {}
    key_word = input("Please input your key word\n")
    patt = r'AND|OR'
    key_word = re.sub(patt, "|", key_word)
    rng = '%s-%s' % (fst, lst)
    rsp, sub = n.xhdr('subject', rng)
    if key_word != "":
        for art in sub:
            if re.search(r'%s' % key_word, art[1]):
                dic_1[art[0]] = art[1]
            else:
                rsp, text = n.body(art[0])
                for line in text.lines:
                    if re.search(key_word, str(line)):
                        dic_1[art[0]] = art[1]
                        break
    else:
        for art in sub:
            dic_1[art[0]] = art[1]
    for key, value in dic_1.items():
        try:
            print(key + " " + value)
        except UnicodeEncodeError:
            print("UnicodeEncodeError")
    art_num = input("Please input the article number\n")
    time, data = n.body(int(art_num))
    displayFirst20(data)
    n.quit()


def displayFirst20(data):
    """显示目标文章"""
    print('*** First (<= 20) meaningful lines:\n')
    lines = [str(line).rstrip() for line in data]
    lastBlank = True
    patt = r'(b\'?\"?>?)'
    m = re.sub(patt, "", lines[2])
    print(m)


if __name__ == '__main__':
    main()

