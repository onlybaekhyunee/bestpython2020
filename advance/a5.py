""" 
2020-4-16
yfc
装饰器 
对修改是封闭的，对扩展是开放的
"""
import time

def decorater(func):
    def wrapper():
        print(time.time())
        # unix时间戳：格式威治时间超至现在的总秒数
        func()
    return wrapper

@decorater
# 语法糖：一种技巧
# 像装饰物一样的引用
def f1():
    print('This is a function.')

@decorater
def f2():
    print('This is anthor function.')

f1()
f2()
