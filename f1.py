""" 
2020-3-29
yfc
function learning
"""
import testpackage.m2

testpackage.sys.setrecursionlimit(1000)
# 设置系统最大循环次数。

attack = False

def skillinfofun(**skinfo):
    # 可变关键字参数
    print("Skinfo's type is "+str(type(skinfo)))
    for key,value in skinfo.items():
        print(key+': '+value)
    
def multiparafun(skill1=0,skill2=0,skill3=0):
    # 关键字参数，增加可读性
    print('Attack is '+str(attack))
    demage1=demage2=demage3=0
    #链式赋值，一次性给三个变量赋相同的值
    if attack:
        demage1 = skill1*5
        demage2 = skill1*2+skill2
        demage3 = skill3*88/3  
    print("Skill1's demage is "+str(demage1))
    print("Skill2's demage is "+str(demage2))
    print("Skill3's demage is "+str(demage3))
    totald = round(demage1+demage2+demage3,2)
    print('This is '+str(totald)+' demage in total')
    return demage1,demage2,demage3
    
def variparafun(isattack,*demage,istotal=True):
    # 必须形参，可变参数，关键字参数
    # 可变参数要在必须参数的后面，一个*为可变普通参数，两个*为关键字可变参数
    # 有多种参数时，关键字参数调用时必须明确指出关键字
    i = totald = 0
    print('Attack is '+str(attack))
    print("Demage's type is "+str(type(demage)))
    # tuple
    if isattack:
        for s in demage: 
            i += 1
            totald += s
            print("Skill"+str(i)+"'s demage is "+str(s))

    totald = round(totald,2)
    if istotal:
        print('This is '+str(totald)+' demage in total')
    return

