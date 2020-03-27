""" 
将testpackage标识为一个包
包导入时的初始化文件
向外部引用者暴露包内接口
__all__标识外部可引用的模块
内容可以为空
避免循环导入
非当前目录或子目录下的引用，需扩充搜索路径sys.path.append("路径")后再引用
"""
import sys
import io

__all__ = ['m1','m4']
print('This is __init__.py file.')
