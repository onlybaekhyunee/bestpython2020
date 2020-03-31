""" 
2020-3-31
yfc
类的学习 
推荐实例调用实例方法，类调用类方法，比较符合逻辑
"""
class Student():
    name = ''
    age = 0
    __hobby = ()
    stusum = 0
    # 学生总数
    dosum = 0
    # 做作业总数
    def __init__(he,name,age,isdohomework):
        # self为实例对象本身，可以任意命名，此处把self命名为he，推荐self
        he.name = name
        he.age = age
        print("Student's name is "+name+".")
        print("age is "+str(age)+".")
        he.__isdohw = isdohomework
        # 双下划线为私有变量
        if isdohomework:
            he.__class__.dosum += 1
            he.__privatefun()
    
    def sethobby(self,*hob):
        self.__hobby = hob
        print("hobby:",end="")
        print(hob)


    @classmethod
    # 装饰器，用于表明类方法
    def countstu(cls):
        cls.stusum += 1
        # cls为类本身，可任意命名，推荐cls

    @staticmethod
    # 静态方法，不需要传类本身变量与实例本身变量，与其它语言的static的含义不同
    def staticfun():
        print("This is a staticmethod!There are "+str(Student.stusum)+" students in total.")

    def __privatefun(self):
        # 双下划线开头为私有方法
        print('This is a private function.')
        print(self.__isdohw)
    
