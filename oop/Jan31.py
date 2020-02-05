# class students:
#     name = 'admin'

#     def get_name(self):
#         print(self.name)
    
# obj1 = students()
# obj1.get_name()
# ________________________________________________

# class calculator:
#     p = 10
#     t=10
#     r=10
#     def take_value(self):
#         pass

#     def calculate(self):
#         result = (self.p*self.t*self.r)/100
#         return result

#     def display(self):
#         return self.calculate()

# obj = calculator()
# print(obj.display())
# ____________________________-

#Constructors

# class students:
#     def __init__(self):
#         print('hello class')

# students()

# ____________________
class students:

    def __init__(self,name):
        print('hello',name)

students('ram')
# ___________________________________________
# class students:
    
#     def get_name(self):
#         name = input('Enter a name : ')
#         return name
    
#     def __init__(self):
#         print(f'your name is {self.get_name()}')

# students()
# _____________________________________________
# class Students:
#     name = ''
    
#     def __init__(self,name):
#         self.name = name
    
#     def get_name(self):
#         print (f'Your name is {self.name}')
    
# obj = Students('Ram')
# obj.get_name()