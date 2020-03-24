account = 'yfc'
password = '123456'
isOk = False

print('Hello,welcome!')

while not isOk:
    print('Please input account:')
    user_account = input()
    print('Please input password:')
    user_password = input()

    if user_account == 'exit' or user_password =='exit':
        break
    if user_account == account and user_password == password:
        isOk = True
        print('Success!')
    else:
        print('Account or password is error,Please input again.')
        print('Or please input"exit" to exit.')