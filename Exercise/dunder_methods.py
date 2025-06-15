#In Python, using double underscores before and after a function name (like __init__, __str__, etc.) defines special methods (also called "dunder" methods, for "double underscore").

# Purpose:

# These methods enable built-in behavior for your objects, such as object creation, string representation, operator overloading, etc.
# Python automatically calls these methods in certain situations.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): # This method is called when we use print() on an instance of the class.
        # It should return a string representation of the object.
        return f"Student(name={self.name}, age={self.age})"

    def __repr__(self): # This method is called when we use repr() on an instance of the class.
        # It should return a string that can be used to recreate the object.
        return f"Student(name={self.name}, age={self.age})"

    def __eq__(self, other): # This method is called when we use == to compare two instances of the class.
        # It should return True if the instances are considered equal, otherwise False.
        if isinstance(other, Student):
            return self.name == other.name and self.age == other.age
        return False

    def __hash__(self): # This method is called to get the hash value of the object.
        # It should return an integer that is used to compare objects in sets and dictionaries.
        return hash((self.name, self.age))
    
# Example usage:
student1 = Student("Alice", 20)
print(str(student1))
print(student1)  # Output: Student(name=Alice, age=20) here __str__ is called implicitly
print(repr(student1))  # Output: Student(name=Alice, age=20) here __repr__ is called implicitly