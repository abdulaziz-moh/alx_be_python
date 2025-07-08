# inheritance(with multiple inheritance) and MRO(method resolution order)
class A:
    def speak(self):
        print("A speaks")

class B(A):
    def speak(self):
        print("B speaks")

class C(A):
    def speak(self):
        print("C speaks")

class D(B, C):
    pass

d = D()
d.speak()
print(D.__mro__)  # Shows the Method Resolution Order 
                  # It follows a depth-first left-to-right search pattern to maintain the order of inheritance and resolve method conflicts effectively.


# polimorphism with ducktyping
# 🧠 What is Duck Typing in Python?
# Duck typing is a concept in programming (especially in Python) where the type or class of an object is less important than the methods or behaviors it supports.

# The name comes from the saying:

# "If it walks like a duck and quacks like a duck, it’s probably a duck."

# In Python, this means:

# If an object has the methods or attributes you're using, Python will allow it — regardless of its actual class.

class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm pretending to be a duck!")

def make_it_quack(entity):   # This shows if an entity have method quack() it's accepted whether it's a Duck or Person regardless of class type
                             # But if we were in languages like c++ or java we can't pass an entity because it only has the method, we need entity to have data type simmilar to the one stated in the function definition
    entity.quack()  # No type checking — we trust it can quack                          
                    # What Happens if the Object Doesn’t Have the Method?   # Python will only raise an runtime error ( AttributeError: 'int' object has no attribute 'quack')

duck = Duck()
person = Person()

make_it_quack(duck)    # Output: Quack!
make_it_quack(person)  # Output: I'm pretending to be a duck!
