import re

s = '233311547573545'
print(re.match('^233',s).group())
print(re.match('2',s).group())
# m = re.match('2333115475735452','[0-9]{1}') 错误的写法，前面写表达式，后面写内容
m = re.match('2|3',s)    # 匹配正则表达式 re1 或者 re2
print(m)
print(m.group())
m = re.search('4757',s)
print(m)
print(m.group())
m = re.match('[a-z0-9]{3,5}','s3011547573545')      #匹配 M～N 次前面出现的正则表达式
print(m.group())
anyend = '.end'
a = re.search(anyend, '\nend')
print(a)
patt314 = '3.14'
pa = '3014'
pa1 = '3114'
print(re.match(patt314,pa).group())
print(re.match(patt314,pa1).group())
#匹配字符串的起始和结尾以及单词边界
n = re.search(r'\bthe', 'bite the1 dog')  # 在边界
print(n.group())
n = re.search(r'\Bthe', 'bite 1the1 dog')  # 在边界
print(n.group())

s =  'This is one Test, another TEST, and another test.'
print(re.findall('(?i)test',s))
# print(re.findall('test',s,re.i))
print(re.findall('test',s,re.IGNORECASE))

m, n = '111'
print(m)
print(n)