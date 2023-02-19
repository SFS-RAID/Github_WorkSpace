usernames = ['admin', 'user1']
passwords = ['1234', '5678']

usname = input('Username: ')
pwd = input('Password: ')
logined = False

if usname not in usernames:
        print('Invalid Username')
else:
    for username, password in zip(usernames, passwords):
        if usname == username and pwd == password:
            print('Login Success')
            logined = True

if not logined and usname in usernames:
    print('Wrong Password')