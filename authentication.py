""" 
2020-3-24
yfc
理解流程控制语句
"""

# 全大写为形式意义上的常量
ACCOUNT = 'yfc'
PASSWORD = '123456'
EXITSTR = 'exit'

isOk = False

print('Hello,welcome!')

while not isOk:
    print('Please input account:')
    user_account = input()
    print('Please input password:')
    user_password = input()

    if user_account == EXITSTR or user_password == EXITSTR:
        break
    if user_account == ACCOUNT and user_password == PASSWORD:
        isOk = True
    else:
        print('Account or password is error,Please input again.')
        print('Or please input"exit" to exit.')
else:
    # pass 空语句，占位语句
    print('Success!')
    