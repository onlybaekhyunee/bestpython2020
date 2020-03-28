import f1

f1.attack = True
r = f1.multiparafun(3,4,5)
d1,d2,d3 = r
# 序列解包
print("Skill1's demage is "+str(d1))
print("Skill2's demage is "+str(d2))
print("Skill3's demage is "+str(d3))
alld = d1+d2+d3
alld = round(alld,2)
print('This is '+str(alld)+' demage in total')
