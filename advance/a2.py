""" 
2020-4-14
yfc
匿名函数
lambda 只能是表达式
lambda parameter_list: expression 
"""
def add(x,y):
    return x+y

f = lambda x,y: x+y

print(add(1,2))
print(f(1,2))
print('~~~~~~~~~~~~~~~~~~~')

t = lambda x,y: x if x>y else y
# 条件为真时返回的结果 if 条件判断 else 条件为假时返回的结果 
print(t(5,6))
print('~~~~~三元表达式~~~~~')
