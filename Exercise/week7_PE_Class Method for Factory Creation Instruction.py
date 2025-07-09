class Person:
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.count += 1

    @classmethod
    def create_child(cls):
        print(f"Child {cls.count} created succesfully")
        return Person("John doe",0)
Person.create_child()
Person.create_child()