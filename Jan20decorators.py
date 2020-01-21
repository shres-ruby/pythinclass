# def message(anyfunction):
#     def check_age(age):
#         if age<18 or age>40:
#             return 'No entry'
#         else: 
#             return 'Welcome!'
#     return check_age

# @message
# def get_age():
#     age = int(input('Enter age: '))
#     return age

# a = int(input('Enter age: '))
# print(get_age(a))
# __________________________

# HOMEWORK 1 - make a decorator to check for zero

def checkforzero(function):
    def checker(x,y):
        if x==0 or y==0:
            return 'Error! Please enter a positive number.'
        else:
            return x+y

    return checker

@checkforzero
def add(x,y):
    return x+y

print(add(0,20))
# ________________________________________

# Homework 2 : make a decorator to check for string and another one to print the documentation

# def check_string(function):
#     def inner(name):
#         if type(name)==str:
#             return name
#         else:
#             return "Error! The data type is not string."
#     return inner

# def print_doc(function):
#     def inner(name):
#         doc = print (function.__doc__)
#         return doc
#     return inner

# @check_string
# def user(name):
#     """Documentation here"""
#     return name
# print(user('Rishi'))

# @print_doc
# def user(name):
#     """Documentation here"""
#     return name

# user('Rishi')
# _____________________________


