# handle = open('students.txt','w') - creates the file students.txt and writes on to it
# handle.write('hello python') - writes this message
# handle.close() - closes the file

# handle = open('students.txt','r') - to read the file
# print(handle.readline()) - to read line by line
# print(handle.readlines()) - displays all lines in a list format
# print(handle.read()) - to read the whole file at once

import os.path

if not os.path.exists('register.txt'):
    file = open('register.txt','w')
    # file.close()

def register():
    username = input ('enter username : ')
    if username in open('register.txt').read():
        print('username already exists')
        register()
        exit()
    
    password = input('enter password : ')
    confirm_password = input('enter password again : ')

    if password != confirm_password:
        print("Passwords do not match!")
        exit()
    
    handle = open('register.txt','a')
    handle.write(username)
    handle.write(' ')
    handle.write(password)
    handle.write('\n')
    handle.close()
    print('Succesfully registered')
    exit()

def login():
    username = input('Enter username : ')
    password = input('Enter password : ')
    get_user_data = open('register.txt').readlines()
    users = []
    for user in get_user_data:
        users.append(user.split())
    
    total_users = len(users)
    count = 0
    login_success = 0
    while count<total_users:
        uname = users[count][0]
        pw = users[count][1]
        if username == uname and password == pw:
            login_success =1
        
        count+=1
    
    if login_success ==1:
        print(f'Welcome {username}')
    else:
        print('username and password do not match')

message = input('Do you have an account y/n : ')
if message == 'y':
    login()

else:
    register()