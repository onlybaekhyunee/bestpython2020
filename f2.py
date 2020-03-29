import f1

f1.attack = True

f1.skillinfofun(SkillV='Ice Magic,AOE',SkillE='Single Target Damage，can not move for 3 minutes',skillF='High Ice Magic AOE,can be breaked')
# 可变关键字参数传参方法
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

f1.attack = True
r1 = f1.multiparafun(skill1=6,skill2=7,skill3=8)
d1,d2,d3 = r1
# 序列解包
print("returnpama's type is "+str(type(r1)))
# tuple
print(d1,d2,d3)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

f1.variparafun(True,20,300.698,1256,31,istotal = True)