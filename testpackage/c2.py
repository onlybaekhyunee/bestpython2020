from testpackage.c1 import Human
""" 
2020-3-31
yfc
类的学习 
推荐实例调用实例方法，类调用类方法，比较符合逻辑
"""
class Student(Human):
    stusum = 0
    # 学生总数
    dosum = 0
    # 做作业总数
    def __init__(self,name,age,school,isdohomework):
        self.school = school
        self.__isdohw = isdohomework
        super(Student,self).__init__(name,age)
        # 调用父类的另一种方法，不推荐：Human.__init__(self,name,age)
        # 双下划线为私有变量
        if isdohomework:
            self.__class__.dosum += 1
            self.__privatefun()

    @classmethod
    # 装饰器，用于表明类方法
    def countstu(cls):
        cls.stusum += 1
        # cls为类本身，可任意命名，推荐cls

    @staticmethod
    # 静态方法，不需要传类本身变量与实例本身变量，与其它语言的static的含义不同
    # 一般用于与类对象、实例对象无关的代码。
    def staticfun():
        print("This is a staticmethod!There are "+str(Student.stusum)+" students in total.")

    def __privatefun(self):
        # 双下划线开头为私有方法
        print('This is a private function.')

    def printinfo(self):
        print("My name is " + self.name +".I am " + str(self.age) +" years old.")
        print("I study in " + self.school + ".") 
        print("There are "+str(Student.stusum)+" students in total.")

    
