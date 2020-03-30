""" 
2020-3-30
yfc
游戏中六级五行石合成成本（金）计算
一级->三级->四级->六级 
"""
diamond_value = 0.05
vit_value = 1
# 全局变量，钻石、体力与金的换算
mvalue = 750
# 市场价

def l1_value(gold=0.75,diamond=8):
    # 获取1级石头需要消耗金和钻石
    l1v = gold + diamond*diamond_value
    print("The level-1 five elements's value is "+str(l1v)+" gold.")
    return l1v

def l3_value(gold=0.39,stone1=12,vit=10):
    # 获取3级石头需要消耗金、1级石头、体力
    l1v = l1_value()
    l3v = l1v + gold + l1v*stone1 + vit*vit_value
    print("The level-3 five elements's value is "+str(l3v)+" gold.")
    return l3v

def l4_value(gold=0.897,stone1=16,vit=10,probability=0.4878):
    # 获取4级石头需要消耗金、1级石头、3级石头、体力，以及一定概率的成功率。
    l1v = l1_value()
    l3v = l3_value()
    time = 1/probability  #获取成功需操作合成的总次数
    l4v = 1*(l3v + gold + l1v*stone1 + vit*vit_value) + (time-1)*(gold + l1v*stone1)
    print("The level-4 five elements's value is "+str(l4v)+" gold.")
    return l4v

def l6_value(stone4=12,gold=19.75,vit=10):
    # 获取6级石头需要消耗4级石头、金、体力
    l4v = l4_value()
    l6v = l4v + stone4*l4v + gold +vit*vit_value
    print("The level-6 five elements's value is "+str(l6v)+" gold.")
    return l6v

value = l6_value()
if value < mvalue:
    print("It's better to synthesis!")
else:   
    print("It's better to buy directly!")