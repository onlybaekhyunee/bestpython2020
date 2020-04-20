""" 
2020-4-20
yfc
对象存在不一定返回True 
内置函数__len __ 和__bool __决定了一个对象的bool值，优先选择__bool __判断，没有__bool __函数则用__len __
"""
class A():
    def __bool__(self):
        # 只能返回bool型
        print('bool called')
        return True

    def __len__(self):
        # 可以返回数字和bool型
        print('len called')
        return False

a = A()
print(bool(a))
