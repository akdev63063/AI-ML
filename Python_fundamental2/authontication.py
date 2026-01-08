username = input('Enter your user name: ')
password = input('Enter your password: ')

if username == "admin" and password == "pass":
    print('Login Successfully')
elif username != "admin" and password != "pass" :
    print('Incorrect Id Password')
elif username != "admin":
    print('Username Incorrect')
elif password != "pass":
    print('Password Incorrect') 

