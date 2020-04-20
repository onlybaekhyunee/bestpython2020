""" 
2020-4-20
yfc
用字典映射代替switch case 语句 
"""
switch = {
    1:'Monday',
    2:'Tuesday',
    3:'Wednesday',
    4:'Thursday',
    5:'Friday',
    6:'Saturday',
    7:'Sunday'
}

day = 1
anthorday = 8
# 字典一般的获值方法
day_name = switch[day]
print(day_name)
# 增加了default的设置，具有容错性
day_name = switch.get(anthorday,'unknown')
print(day_name)

""" 
带函数的switch case语句转换 
"""
def get_monday():
    return 'Monday'

def get_tuesday():
    return 'Tuesday'

def get_default():
    return 'unkonwn'

switch_f = {
    1:get_monday,
    2:get_tuesday
}

day_name = switch_f.get(day,get_default)()
print(day_name)
day_name = switch_f.get(anthorday,get_default)()
print(day_name)
