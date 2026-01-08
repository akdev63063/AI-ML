username = input('Enter your user name: ')
password = input('Enter your password: ')

if username == "admin" and password == "pass":
    print('Login Successfully')
else:
    if username != "admin":
        print('Username Incorrect')
    else :
        print('Password Incorrect') 