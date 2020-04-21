""" 
2020-2-21
yfc
dataclass
轻松生成__init__ repr固定格式等。
无私有变量
"""
from dataclasses import dataclass
@dataclass
class Student():
    name:str
    age:int
    school:str
    hobby:str
    def getname(self):
        return self.name

studentA = Student('YuFangchao',18,'UESTC','paint')
studentB = Student('ChenYuejun',32,'UESTC','games')
print(studentA.getname())
# repr将对象转化为供解释器读取的形式
print(repr(studentA))
print(studentB.getname())
print(repr(studentB))
