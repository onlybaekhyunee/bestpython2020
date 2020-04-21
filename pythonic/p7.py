""" 
2020-4-21
yfc
walrus海象运算符:= 
python3.8新特性，简化代码，提高速度
在表达式中赋值
"""
import re
# 例1：一般应用
a = 'I like Python'
if (b:=len(a))>5:
    print(a+'.The length of this sentence is '+str(b))

# 例2：正则表达式应用
c = 'The mall is having a sale. The discount for books is 70%,the discount for shoes is 50% '
if (d:=re.findall('(\d+)%',c)):
    discount = map(lambda x: float(x)/100.0,d)
    print(list(discount))
    
# 例3:列表推导式应用
def f(key,value):
    if int(value) >= 18:
        return key+"'s age is "+str(value)
    else:
        return False

e = {'yfc':36,'cyj':33,'cyx':8}
g = [y for key,value in e.items() if (y:=f(key,value))]
print(g)
