# def test():
#     print ('Hello')

# test()

# def add(x,y):
#     print (x+y)

# a= int(input('Enter a number : '))
# b = int(input('Enter a number : '))

# add(a,b)

# def add(x,y):
#     return x+y

# print(add(10,20))

# def add_sub(x,y):
#    sum = x+y
#    subtract = x-y
#    return [sum, subtract]

# # print (add_sub(10,20))

# result = add_sub(1,11)
# print (f'The sum is {result[0]}')
# print (f'The difference is {result[1]}')

# _______________________________

# Endless parmeters:

# (i) Array argument:

# def user(*name):
#     print (name)

# user ('Ruby','Rishi', 'nom')
# _____________
# (ii) Keyword argument:

# def students (**data):
#     print(data)

# students(name = 'Ram', age = 20)
# _____________________________

# Function Scopes:

# Global= can be used anywhere within the program
# Local = can be used only within the function

# x=10
# def test():
#     print(x)

# test()  #prints 10
# _____________________

# x=10
# def test():
#     global x
#     x = x+20
#     print(x)

# test()
# ________________

# def test():
#     pass

# print(test) #returns the memory location of the function

# HOMEWORK 1:

def take_value():
    def calculate():
        def display():
            print("The simple interest is", si)
        si = (p*t*r)/100
        display()
    p = int(input('Enter principal amount : '))
    t = int(input('Enter number of years : '))
    r = int(input('Enter interest rate : '))
    calculate()

take_value()