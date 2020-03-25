""" 
2020-3-25
yfc
pyhton中的for与其他语言有些不同 
"""

print("Let's have some fruits!")
FRUITS = (('first','second','third','fourth','fifth'),('pineapple','watermelon','coconut','grape','pear'))

for a in FRUITS:
    for b in a:
        print('%10s'%b,end='|')
        # %10s：字符输出长度为10，不足在字符左侧填充空格；end:设置打印结束符
    else:
        # for执行完后执行
        # 不加end会换两行,end默认为\n
        print('\n',end='')
else:
    print('Yummy!')

for a in FRUITS:
    for b in a:
        if 'third'==b:
            break
            # break:强制退出当前循环代码块，包括else也不执行
            # 当a值发生变化时，是一个新的循环，可正常执行
            # continue:继续下一个循环
        print('%10s'%b,end='|')
    else:
        print('\n',end='')
else:
    for i in range(0,10,2):
        print('Oh!No!somthing is lose!')

test = [1,2,3,4,5,6,7,8,9]
for j in range(0,len(test),2):
    print(test[j],end=' | ')
t = test[0:len(test):2]
print(t)
