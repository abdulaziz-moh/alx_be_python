class Animal:
    def __init__(self,name):
        self.name =  name
    def eat(self):
        print("🍽️ The animal is eating.")
    def sleep(self):
        print("😴 The animal is sleeping.")

class Dog(Animal):
    def __init__(self,name,type):
        super().__init__(name)
        self.type = type
    def bark(self):
        print("🐶 Woof! Woof!")

# Creating an instance of Animal
animal = Animal("ZEBRA")
print("Animal instance:")
animal.eat()
animal.sleep()
print()

# Creating an instance of Dog

dog1 = Dog("Bobe","Germen sheepherd")
dog1.eat()       # Inherited from Animal
dog1.sleep()     # Inherited from Animal
dog1.bark()      # Unique to Dog
