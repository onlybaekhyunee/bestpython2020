""" 
2020-4-1
yfc
类的继承性学习 
"""
class Human():
    name = ''
    age = 0
    __hobby = ()
    __sum = 0
    # 人总数
    def __init__(he,name,age):
        # self为实例对象本身，可以任意命名，此处把self命名为he，推荐self
        he.name = name
        he.age = age
        he.__class__.__sum += 1 
        # 双下划线为私有变量
    
    def sethobby(self,*hob):
        self.__hobby = hob


    def printinfo(self):
        print("This is a parent class!")
        print("My name is " + self.name +".I am " + str(self.age) +" years old.")
        print("I like " + str(self.__hobby) + ".") 
        print("There are " + str(self .__class__.__sum) + " people in total.")

    
