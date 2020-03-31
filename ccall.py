from testpackage.c1 import Student

student1 = Student('YuFangchao',18,True)
student1.sethobby('swim','run')
Student.countstu()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
student2 = Student('ChenYuejun',38,False)
student2.sethobby('sleep','computer game')
Student.countstu()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
student3 = Student('ChenYuxi',8,True)
student3.sethobby('swim','make a model plane')
Student.countstu()
# 实例也可以调用类方法，但实例调用实例方法，类调用类方法比较符合逻辑
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
student1.staticfun()
Student.staticfun()
print(str(Student.dosum)+' students have finished their homework.')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(student1.__dict__)
# student1.__privatefun()私有方法无法访问
# print(student1.__isdohw)但私有变量可以通过_Student_isdohw来访问
