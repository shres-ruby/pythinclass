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
#     name = input('Enter your name')
#     Nepali = int(input('Enter marks for Nepali : '))
#     English = int(input('Enter marks for English : '))
#     x =[name,Nepali,English]
#     subjects.append(x)
#     count+=1

# for i in subjects:
#     print (i)
# _________________________________________

# Homework 2 (Jan 19, 2020)

# def my_rep(data,times):
#     for i in range (1, times+1):
#         result = print (data)
#     return result

# my_rep('Ram',10)

# Alternate method:
# def rep(data, times):
#     return data*(int(times))

# print(rep('Ram',10))
# _______________________________
# Alternate method for simple interest:

# def take_value():
#     p = int(input('Enter p: '))
#     t = int(input('Enter t: '))
#     r = int(input('Enter r: '))
#     return [p,t,r]

# def calculate():
#     smp = take_value()
#     a=smp[0]
#     b=smp[1]
#     c=smp[2]
#     return a*b*c/100

# def display():
#     print(calculate())

# display()
# # _________________________________

# def message(anyfunction):
#     def check_age():
#         age=anyfunction()
#         if age<18 or age>40:
#             return 'No entry'
#         else: 
#             return 'Welcome!'
#     return check_age

# @message
# def get_age():
#     age = int(input('Enter age: '))
#     return age

# print(get_age())
# _________________________________

# Modules (Jan 21 class) : 

# def add(x,y):
#     return x+y

# def sub(x,y):
#     return x-y
# ________________________________
import tkinter as tk

open_tk = tk.Tk()
open_tk.title('My GUI Application')

my_can = tk.Canvas(width=600,height=400,bg='red')
my_can.pack()

open_tk.mainloop()