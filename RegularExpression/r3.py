import re
""" 
2020-4-2
正则表达式：一组字符序列
1、快速检索
2、文本替换
3、文本检测：是否是正确的电话号码，是否是正确的邮箱等等。
4、信息提取√
"""
t = 'Life is short,I use Python.I love Python.'
print(re.findall('s',t))
# ()组，组内为且的关系，不会显示匹配的全部字符，只按匹配字数显示括号内的字符
m1 = re.match('s',t)
# 从字符串首字符开始匹配，如果没有结果将返回None
s1 = re.search('s',t)
# 在整个字符串中搜索，一旦找到结果立刻返回
print(m1)
print(s1)
print(s1.span())
print(s1.group())
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
s2 = re.search('Life(?P<n1>.*)Python.(.*)Python',t)#?P<name>定义组别名
print(s2.group('n1'))
print(s2.group(2))
print(s2.group(0,'n1',2))
print(s2.group(0,1,2))
print(s2.groups())
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# 提取标签信息
h = "<span class='t'>标题</span><a href=''>查看</a><span>正文</span><table></table>"
s3 = re.findall('<span.*>(.*)</span>',h)
print(s3)
# 贪婪原则，只能找到最后一个
s4 = re.findall('<span.*?>(.*?)</span>',h)
print(s4)
# 非贪婪原则，可以找到全部
