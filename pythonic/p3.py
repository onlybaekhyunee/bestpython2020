""" 
2020-4-20
yfc
把类设置为迭代器iterator，可用for in 遍历 
类中有 __iter__(self)，__next__(self)两个函数，则该类具有了迭代器的属性
"""
class A():
    def __init__(self):
        self.cur = 0
        self.data = ['<Python>','<C++>','<Java>','<C#>']

    def __iter__(self): 
        """ 
        向系统说明这是一个可迭代对象   
        """    
        return self

    def __next__(self):
        """ 
        提供迭代算法 
        """
        if self.cur >= len(self.data):
            # raise显示引发异常，执行后，后续语句不再执行;StopIteration迭代不再执行
            raise StopIteration()
        r = self.data[self.cur]
        self.cur +=1
        return r

language = A()
# 迭代器的使用具有一次性，不能多次使用for in遍历
for i in language:
    print(i)

