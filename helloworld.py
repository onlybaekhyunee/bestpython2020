a='我是str1'
b=a
print('游戏1：\na='+a,'clone_a='+b)
temp = input('请输入任意内容，改变a的值')
a=temp
print('a='+a,'clone_a='+b)
c=['我','是','str2']
d=c
print('游戏2：\nc=')
print(c)
print('clone_c=')
print(d)
temp = input('请输入任意内容，改变c的值')
c[-1]=temp
print('c=')
print(c)
print('clone_c=')
print(d)
