import re
""" 
2020-4-2
正则表达式：一组字符序列
1、快速检索√
2、文本替换
3、文本检测：√是否是正确的电话号码，是否是正确的邮箱等等。
re.findall('正则表达式',字符串) 
"""
a = '1C\n|2C++\t|3C#\a|4Java\b|5Python\f|6Script\r|7Php\v|8Pythonn&|9VB____'
print(a)
print(re.findall('Python',a))
#普通字符
print(re.findall('\d',a))#数字
print(re.findall('\D',a))#非数字
print(re.findall('\w',a))#单词字符
print(re.findall('\W',a))#非单词字符
print(re.findall('\s',a))#空白字符
print(re.findall('\S',a))#非空白字符
print(re.findall('.',a))#除换行符以外的其它字符
print(re.findall('c.[^a-z]',a,re.I|re.S))#匹配模式参数，re.I忽略大小写re.S概括字符.可以匹配换行符
#概括字符
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')
print(re.findall('[A-Za-z]{1,6}',a))# 贪婪原则，{}数量词,1至6个
print(re.findall('[a-z]{3,6}?',a))# 非贪婪原则
# *匹配0次或无限次
# +匹配1次或无限次
# ?匹配0次或1次
# 只对前面的字符生效
print(re.findall('Python?',a))
print(re.findall('Python{0,2}?',a))
# 两个?含义不一样
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`')

b = 'abc,adc,a2c,afc,avc,bcc,cde,agc,afb,afg'
print(re.findall('a[df]c',b))
print(re.findall('a[^cf]c',b))
print(re.findall('a[a-d]c',b))
print(re.findall('a[^a-d]c',b))
# 字符集，[]中为或的关系
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

qq = '247053554'
qq1 = '2470535544'
qq2 = '101'
r = re.findall('^\d{4,9}$',qq2)
print(r)
# ^表示开始 $表示结尾，为边界匹配符
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

t = 'sabsabab,asabsabc,deefsss,fsseg,lsmsab,nsmsasab'
print(re.findall('(sab){2}',t))
# ()组，组内为且的关系，分组只会显示括号括起来的内容


