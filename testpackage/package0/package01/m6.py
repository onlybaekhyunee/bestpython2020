from ..m5 import a5
from ...package1.m7 import a7
# 相对路径的引入，.表示当前目录，..表示上一级目录，...表示上上级目录，以此类推

print('This is m6.py,my package is '+str(__package__))