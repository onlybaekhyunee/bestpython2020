n=int(input('请输入一个数字：'))
print('该数字的二进制为：'+str(bin(n)))
temp =n
m = 1
result1 = 0
result0 = 0
i = 0

while i < 32:
    i += 1
    if m&n :
        result1 += 1              
    m = m << 1
    temp = temp>>1
    if (not temp) and (not result0):
        result0 = i
print('该数字二进制编码中含有1的个数为：'+str(result1))
print('该数字二进制编码中含有0的个数为：'+str(result0-result1))

""" 12234
44656
fggdg """