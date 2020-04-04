""" 
2020-4-4
yfc
旅行距离叠加
非闭包方法，闭包方法 
"""
def trip(origin):
    def go(step):
        result = origin + step
        return result
    return go

t = trip(0)
print(t(3))
t = trip(t(3))
print(t(5))
t = trip(t(5))
print(t(8))
print('~~~~~~~~~~~~~~~~最初的思路~~~~~~~~~~~~~~~~~')

def trip1(origin):
    def go(step):
        nonlocal origin
        origin = origin + step
        return origin
    return go
t1 = trip1(0)
print(t1(3))
print(t1.__closure__[0].cell_contents)
print(t1(5))
print(t1.__closure__[0].cell_contents)
print(t1(8))
print(t1.__closure__[0].cell_contents)
print('~~~~~~~~~~~~~~~~~~闭包~~~~~~~~~~~~~~~~~~~')

origin = 0
def go(step):
    global origin
    origin = origin + step
    return origin
print(go(3))
print(go(5))
print(go(8))
print('~~~~~~~~~~~非闭包：全局变量会被改变~~~~~~~~~~~')
