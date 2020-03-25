""" 
2020-3-23
yfc
计算输入数字的二进制0与1的个数，理解位运算 
"""

n=int(input('请输入一个数字：'))
print('该数字的二进制为：'+str(bin(n)))
temp =n
m = 1
result1 = 0
# 总位数
result0 = 0
i = 0

while i < 32:
    i += 1
    if m&n :
        result1 += 1              
    m = m << 1
    temp = temp>>1
    # temp右移完最后一位，值会等于0，且result0未赋值
    if (not temp) and (not result0):
        result0 = i
print('该数字二进制编码中含有1的个数为：'+str(result1))
print('该数字二进制编码中含有0的个数为：'+str(result0-result1))
