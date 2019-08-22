import time
# for i in range(10):
#     print("离程序退出还剩%s秒\t" % (9-i), end="")
#     # print("离程序退出还剩%s秒" % (9-i), end="")
#     time.sleep(1)

import re

# print("file_path------>","./html/"+re.match(r"[^/]+/{[^\s]*}",request_header_lines[0]).group(1))
s = ' GET /js/jquery.flexslider.js HTTP/1.1'
# m = re.search(r'[^/]+/([^\s]*)',s).group()
m = re.search(r'[^/]+',s).group()

# m = re.search(r'[/]*?[\b]',s).group()
print(m)
# m1 = re.findall()