from enum import Enum
from enum import IntEnum,unique
# IntEnum数值只能是数字，unique是装饰器，不允许出现别名
""" 
2020-4-3
枚举是一个类
枚举的意义在于标识，不在于数值 
设计模式是单例模式
"""
class QQVIP(Enum):
    YELLOW = '1'
    YELLOW_ALIAS = '1' #这种情况可以存在实际上是YELLOW的别名
    RED = '2'
    GREEN = '3'
    BLACK = '4'
    # 推荐大写
    # 不可变，防止相同值

class ALIVIP(IntEnum):
    YELLOW = 1
    RED = 2
    GREEN = 3
    BLACK = 4
    # 推荐大写
    # 不可变，防止相同值

print(type(QQVIP.GREEN))       #枚举类型
print(type(QQVIP.GREEN.name))  #枚举名称
print(type(QQVIP.GREEN.value)) #枚举值
print(QQVIP['YELLOW'].value)
print('~~~~~~~~~~~~~~~~')

for v in QQVIP:
    # 遍历时别名不会遍历
    print(type(v))
    print(v)
    print(v.name)
    print(v.value)
    print('~~~~~~~~~~~~~~~~')

for v1 in QQVIP.__members__:
    print(v1)

for v2 in QQVIP.__members__.items():
    print(v2)
print('~~~~~~~~~~~~~~~~~~~~~~')

a = 2
ea = ALIVIP(a)
for v3 in ALIVIP:
    if v3 == ea:
        print(ea)
    else:
        print('error')