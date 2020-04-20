""" 
2020-4-20
yfc
列表推导式 
集合推导式
"""

a = [1,2,3,4,5,6,7,8]
# 列表推导式也可以用集合实现
b = [i**3 for i in a]
c = map(lambda x :x**3,a)
print(b)
print(list(c))
# 有条件的推导式
d = [i*2 for i in a if i <5]
e = map(lambda x: x*2,filter(lambda x :True if x <5 else False,a))
print(d)
print(list(e))
# 集合推导式,集合是无序的
f = {8,7,6,5,4,3,2,1}
g = {i*2 for i in f}
print(g)
# 字典推导式
h = {1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday'}
i = {value:key for key,value in h.items()}
print(i)
j = [value for key,value in h.items()]
print(j)
