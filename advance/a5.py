""" 
2020-4-16
yfc
装饰器 
对修改是封闭的，对扩展是开放的
AOP思想，千面
"""
import time

def decorater(func):
    def wrapper():
        print(time.time())
        # unix时间戳：格式威治时间超至现在的总秒数
        func()
    return wrapper

# 带参数的装饰器
def openword(func):
    def wrapper(*args,**kw):
        # 可变参数，可变关键字参数
        print('Now is '+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        func(*args,**kw)
    return wrapper

@decorater
# 语法糖：一种技巧
# 像装饰物一样的引用
def f1():
    print('This is a function.')

@openword
@decorater
def f2():
    print('This is anthor function.')
# 可以加多个装饰器，注意参数。

f1()
f2()

@openword
def f3(name):
    print('My name is '+name)

@openword
def f4(name , *hobby):
    print('My name is '+name)
    print('I like '+ str(hobby))

@openword
def f5(name , **grade):
    print('My name is '+name)
    for key,value in grade.items():
        print(key+"'s grade is "+value)

f3('Vicky')
f4('Shirley','swim','make a modle')
f5('Pete',English = 'A',Science = 'B',Math = 'F')
