import re


def register():
    dbase = open('Database.txt', 'r')
    email_id = input('Create Email Id : ')
    pattern_email = '^[a-z 0-9]+[@]\w+[.]\w{2,3}$'
    if not re.search(pattern_email, email_id):
        print('Email Invalid')
        register()
    temp_1 = []
    temp_2 = []
    for each in dbase:
        mail, pwd = each.split(', ')
        pwd = pwd.strip()
        temp_1.append(mail)
        temp_2.append(pwd)
        dict(zip(temp_1, temp_2))
    password = input('Create Password : ')
    pattern_password = "^.*(?=.{5,16})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@?#$%^&=+]).*$"
    if re.search(pattern_password, password):
        if email_id in temp_1:
            print('Email Id already exists')
            register()
        else:
            dbase = open('Database.txt', 'a')
            dbase.write(email_id + ', ' + password + '\n')
            print('Registered Successfully')
    else:
        print('Password Invalid')
        register()


def access():
    dbase = open('Database.txt', 'r')
    email_id = input('Enter Email Id : ')
    password = input('Enter Password : ')

    if not len(email_id or password) < 1:
        temp_1 = []
        temp_2 = []
        for each in dbase:
            mail, pwd = each.split(', ')
            pwd = pwd.strip()
            temp_1.append(mail)
            temp_2.append(pwd)
        data = dict(zip(temp_1, temp_2))

        if data[email_id]:
            if password == data[email_id]:
                print('Login Success')
            else:
                print('Email or Password Incorrect')
        else:
            print('Email does not exist')
    else:
        print('Enter the value')


def user():
    option = input('login or signup ')
    if option == 'login':
        access()
    elif option == 'signup':
        register()
    else:
        print('Enter correct option')
        user()


user()
