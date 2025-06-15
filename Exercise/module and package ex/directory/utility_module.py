def add(a,b):
    return a+b
def subtract(a,b):
    return a-b

class user:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def get(self):
        print(f"The name is {self.name}")
        print(f"The age is {self.age}")
        self.cls_method()  # Calling the class method
        self.static_method()

        self.aaa = "This is an instance variable"
        print(self.aaa)  # Accessing the instance variable
    
#_________________________________________________________________________________________________________________________#

    name = "utility_module"
    @classmethod  # This is a class method decorator, similar to @staticmethod, but it takes the class as the first argument.
                  # We can create this below method without using the decorator
    
    def cls_method(cls): # Here cls is the class itself, similar to self in instance methods
                        # Thsi cls act as a reference to the class, so we can access class variables and methods.
        print(cls.name)

    
#_________________________________________________________________________________________________________________________#

    @staticmethod  # This is a static method decorator simmilar @classmethod (and like @override in java and so on).
                   # we can create this below method without using the decorator
    def static_method():
        print("This is a static method in utility_module")
        # Here we can not access the class or instance (like name or age) variables or methods.

#_________________________________________________________________________________________________________________________#
     
