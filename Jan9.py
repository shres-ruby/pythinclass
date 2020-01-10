# x = int(input('Enter a number : '))
# y= int(input('Enter another number : '))

# if x>y:
#     print (f'The greater number is {x}')

# else:
#     print (f'The greater number is {y}')

# x=100
# y=200
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

# age = int(input('Enter age : '))

# if age < 18:
#     print ('Sorry, you cannot enter the party.')

# elif age >= 18 and age<= 40:
#     print ('Welcome to the party!')

# else:
#     print ('Sorry, you are too old to enter')

# amount = 150000
# rate = 3.5
# year = 2.5

# if amount <= 100000:
#     interest = 0.03 * amount
#     total = year*interest
#     print (total)

# else:
#     interest = 0.035 * amount
#     total = year* interest
#     print (total)

Nepali = int(input('Enter marks for Nepali : '))
English = int(input('Enter marks for English : '))
Maths = int(input('Enter marks for Maths : '))
Science = int(input('Enter marks for Science : '))
Population = int(input('Enter marks for Population : '))
passmark = 35

total = Nepali+  English+ Maths+ Science+ Population
percentage = (total/500)*100

print (f'The total marks is {total}')
print ('The percentage is %0.2f' %percentage)

# for i in (Nepali,English,Maths,Science,Population):
#     if i<passmark:
#         print(f'The student failed in {i}')

if Nepali<passmark:
   print ('The student failed in Nepali.')
if English<passmark:
    print ('The student failed in English')
if Maths<passmark:
    print ('The student failed in Maths')
if Science<passmark:
    print ('The student failed in Science.')
if Population<passmark:
    print ('The student failed in Population')

if Nepali>=passmark and English>=passmark and Maths>=passmark and Science>=passmark and Population>=passmark:
    if percentage>= 35 and percentage<45:
        print ('The division is third division.')

    elif percentage >=45 and percentage <60:
        print ('The division is second division.')

    elif percentage >=60 and percentage <75:
        print ('The division is first division.')

    else:
        print ('The division is topper division')