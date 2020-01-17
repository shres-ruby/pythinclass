# users = {'name': 'Ram', 'address':'Ktm', 'phone':987678877}

# for i in users:
#     print (users[i])

# info = {
#     'name' : input('Enter name : '),
#     'gender' : input ('Enter gender : ')
# }

# nameoutput = info['name']
# genderoutput = info.get('gender')

# print (nameoutput, genderoutput)

# users = [
#     {
#         'name' : 'ram',
#         'address' : 'ktm',
#         'phone' : 98678,
#         'parent': ['hari']
#     }
# ]

# #write a command to get output as 'hari'

# print (users[0]['parent'][0])

# users = {
#         'name' : 'ram',
#         'address' : 'ktm',
#         'phone' : 98678,
#         'parent': ['hari']
#     }

# users['address'] = 'Lalitpur'

# print (users)

#Go to jsonplaceholder.typicode.com to fetch the API

students= [
    {'name':'hari', 'address':'ktm'},
    {'name':'sita', 'address':'ltp'},
    {'name':'gita', 'address':'bkt'}
]

for i in students:
    name = i['name']
    print (f'Your name is {name}')