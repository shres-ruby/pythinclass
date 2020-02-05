# class Mobile:
    
#     # brand = '' #we only need this line if we have not declared 'brand' while defining __init__
    
#     def __init__(self,brand):
#         self.brand = brand
    
#     def get_brand(self):
#         return self.brand

# class Mi:
    
#     def __init__(self):
#         print("hello")


# class Nokia(Mobile, Mi):
#     def __init__(self,brand,model):
#         super().__init__(brand)
#         Mi.__init__(self)
#         self.model = model
    
#     def get_model(self):
#         return self.model


# obj = Nokia('mi','xyz')
# # print(obj.model)
# print(obj.brand)
# _____________________________________

class Mobile:
        
    def __init__(self,brand):
        self.brand = brand
    
    def get_brand(self):
        return self.brand
    
class Nokia(Mobile):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model

class Mi(Nokia):
    def __init__(self,brand,model):
        super().__init__(brand,model)

obj = Mi('abc','a2')
print (obj.brand)
print(obj.model)