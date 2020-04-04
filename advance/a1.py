""" 
2020-4-4
yfc
闭包 
"""
def c():
    a = 10
    def c_v(x):
        return a*x**2
    return c_v
# 闭包：环境变量（定义在函数外部，但非全局）+函数

a = 20
f = c()
print(f.__closure__)
print(f.__closure__[0].cell_contents)
# 获取环境变量的值
print(f(3))
