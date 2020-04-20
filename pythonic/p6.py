""" 
2020-4-20
yfc
装饰器的副作用：如改变函数name 
"""
import time
from functools import wraps

def decrator(func):
    def wrapper():
        """ 
        This is wrapper 
        """
        print(time.time())
        func()
    return wrapper

def decrator2(func):
    @wraps(func)
    def wrapper():
        """ 
        This is wrapper
        after adding the wraps decrator,function's name doesn't changed
        """
        print(time.time())
        func()
    return wrapper

def f1():
    """ 
    This is f1 
    """
    print(f1.__name__)

@decrator
def f2():
    """ 
    This is f2 
    """
    print(f2.__name__)

@decrator2
def f3():
    """ 
    This is f3
    """
    print(f3.__name__)

f1()
print(f1.__doc__)
f2()
print(f2.__doc__)
f3()
print(f3.__doc__)
