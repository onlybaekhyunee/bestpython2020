""" 
2020-4-16
yfc
filter：过滤器
lambda表达式返回值可以判断真和假，True or False，1 or 0 
"""
list_n = [1,0,0,1,0,1]
list_s = ['H','e','l','l','o','W','o','R','L','D']
fn = filter(lambda x: x,list_n)
print(list(fn))
fs = filter(lambda x: True if ord(x)<=90 else False,list_s)
print(list(fs))
f = filter(lambda x: x.isupper(),list_s)
print(list(f))
