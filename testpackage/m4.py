""" 
2020-3-27
yfc 
"""
print('This is m4.py file.')

infos = dir()
# dir返回当前文件的所有变量，可以看到内置变量
print(infos)

if __name__=='__main__':
    print('This is app')
else:
    print('This is module')
# Make s script both importable and executable 
print('name is '+str(__name__))
print('package is '+str(__package__))
print('doc is '+str(__doc__))
print('file is '+str(__file__))
# file值不固定，与命令执行时输入的文件路径有关
# 入口文件与模块的内置变量不同