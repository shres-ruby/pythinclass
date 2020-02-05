# class News:

#     def __init__(self):
#         pass
    
#     @staticmethod
#     def test(title):
#         print(title)
    
# News.test('hello news')
# ________________________________________________
# class News:

#     age = 0 #this is called property (when a variable is declared in a class)

#     def __init__(self):
#         pass

#     @property #for returning the set variable
#     def get_age(self):
#         return self.age
    
#     @get_age.setter  #only for assigning. has no return type
#     def get_age(self,age):
#         self.age = age
    
# ob = News()
# ob.get_age = 20
# print(ob.get_age)
# _______________________________________________________________

# class News:
#     total = 0

#     def __init__(self,title):
#         print(title)
#         News.total += 1

#     def total_news(self):
#         print(News.total)

# obj1 = News ('title')
# obj2 = News ('title')
# obj3 = News ('title')
# obj4 = News ('title')

# obj1.total_news()
# _____________________________-

class News:
    total = 0

    def __init__(self,title):
        print(title)
        News.total += 1

    def total_news(self):
        print(News.total)
    
    @classmethod
    def add_total(cls,tot):
        cls.total = tot

obj1 = News ('title')
obj2 = News ('title')
obj3 = News ('title')
obj4 = News ('title')

obj1.add_total(10)
obj4.total_news()