# class Students:
#     name = ''
#     total = 0 #thisis a property

#     def __init__(self,name):
#         self.name = name
#         Students.total+=1
    
#     def get_name(self):
#         print(f'your name is {self.name}')

#     def total_students(self):
#         print(f'The total is {self.total}')

# obj1 = Students('Ram')
# obj2 = Students('Sita')
# obj1.total_students()
# __________________________________________________

# class User:
#     def __init__(self,name):  #double underscore is private, single undrescore is protected
#         self.__name = name
    
#     def test(self):
#         return self.__name

# obj = User('ram')
# print(obj.test())
# _______________________________________

# class User:
#     """We are learning OOP"""
#     title = 'Hello title'

#     def __init__(self, name):
#         self.name = name
    
#     def test(self):
#         """test methods"""
#         return self.name
    
#     # def __str__(self):
#     #     return self.title

# obj = User('ram') #when we do this and then print(obj), it prints the title
# print(obj)
# print(obj.__doc__) #to get the User's documentation
# print(obj.test.__doc__) #to get test's documentation
# ____________________________________

class User:
    def __init__(self):
        print("I am init method \n")

    def __call__(self):
        print('I am calling.. \n')

# obj = User()
# obj.__call__()
# # obj()