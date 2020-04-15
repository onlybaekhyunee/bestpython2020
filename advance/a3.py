""" 
2020-4-16
yfc
map and lambda
map 内置高阶函数，根据提供的函数对指定序列做映射 
"""
list_x = [1,2,3,4,5,6,7,8]
list_y = [8,7,6,5,4,3,2,1]
r = map(lambda x,y: x**2+y,list_x,list_y)
print("Map result's type is "+str(type(r)))
print(list(r))
