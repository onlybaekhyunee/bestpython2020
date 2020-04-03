import re
""" 
2020-4-2
正则表达式：一组字符序列
1、快速检索
2、文本替换√
3、文本检测：是否是正确的电话号码，是否是正确的邮箱等等。
re.sub('正则表达式',被替换的内容：字符串或函数，字符串，匹配次数) 
"""
language = 'I like Python! My friend likes Python, too!'
r1 = re.sub('Python','Go',language)
r2 = re.sub('Python','Go',language,1)#count参数，能被替换的最大次数
r3 = language.replace('Python','Go',1)
print(r1)
print(r2)
print(r3)

def convert(str):
    print(str)
    m = str.group()
    return '^'+m+'^'

r4 = re.sub('Python',convert,language,2)
print(r4)

def convern(num):
    n = num.group()
    if int(n) >= 6:
        return '9'
    else:
        return '0'

s1 = 'A8C3721d86'
r5 = re.sub('\d',convern,s1)
print(r5)