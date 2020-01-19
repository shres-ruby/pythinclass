# x=100
# y=20
# z=30

# if x>y:
#     if x>z:
#         print ('x is largest')
#     else:
#         pass

# else:
#     if y>x:
#         print('y is largest')

#     else:
#         print ('z is largest')

#________________________________________________________________

# subjects = {
#     'Nepali' : int(input('Enter marks for Nepali : ')),
#     'English' : int(input('Enter marks for English : '))
# }

# total = subjects['Nepali'] + subjects ['English']
# print (f'The total marks is {total}')

# for i in subjects:
#     if subjects[i] < 35:
#         print (f'The student failed in {i}')

#____________________________________________________

# num = int(input('Enter number of students : '))
# count = 0
# subjects = []

# while count < num:
#     Nepali = int(input('Enter marks for Nepali : '))
#     English = int(input('Enter marks for English : '))
#     for i in (Nepali, English):
#         subjects.append(i)
#     count+=1

# print (subjects)
# _________________________________________

# Homework 2 (Jan 19, 2020)

def my_rep(data,times):
    for i in range (1, times+1):
        result = print (data)
    return result

my_rep('Ram',10)