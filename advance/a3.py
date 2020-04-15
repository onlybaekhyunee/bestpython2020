""" 
2020-4-16
yfc
map/lambda
map 内置高阶函数，根据提供的函数对指定序列做映射 
map/reduce
映射/归约，并行计算
"""
from functools import reduce

list_x = [1,2,3,4,5,6,7,8]
list_y = [8,7,6,5,4,3,2,1]
m = map(lambda x,y: x**2+y,list_x,list_y)
print("Map result's type is "+str(type(m)))
print(list(m))

list_s = ['1','2','3','4','5','6','7','8']
r = reduce(lambda x,y: x+y,list_s,'aaa')
# 函数、列表，初始值，进行连续计算
print(r)

# 旅行者问题，初始位置原点0,0，然后移动，求最终到达的位置
list_step = [(1,3),(2,-2),(-2,3),(5,4)]
p = reduce(lambda x,y: (x[0]+y[0],x[1]+y[1]),list_step,(0,0))
print(p)
