#------------------------------------------------------------------------#
# class methods

class Person:
    count = 0  # Class variable to count instances

    def __init__(self, name):
        self.name = name
        Person.count += 1  # Increment count on instance creation

    def test(self):
        print(Person.count)

    @classmethod
    def display_count(cls):
        print(f"Total persons created: {cls.count}")

# Usage
person1 = Person("Alice")
person2 = Person("Bob")
Person.display_count()  # Output: Total persons created: 2
person1.test()
print(Person.count)


#------------------------------------------------------------------------#
# static methods(helper/utility methods)

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Usage
print(MathUtils.add(5, 3))       # Output: 8   # accesed through the class name
print(MathUtils.multiply(5, 3))  # Output: 15
