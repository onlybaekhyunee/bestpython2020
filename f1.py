""" 
2020-3-29
yfc
function learning
"""
import testpackage.m2

testpackage.sys.setrecursionlimit(1000)
# 设置系统最大循环次数。

attack = False

def multiparafun(skill1,skill2,skill3):
    print(attack)
    if attack:
        demage1 = skill1*5
        demage2 = skill1*2+skill2
        demage3 = skill3*88/3
    else:
        demage1=demage2=demage3=0
        # 一次性给三个变量赋相同的值
    return demage1,demage2,demage3

    