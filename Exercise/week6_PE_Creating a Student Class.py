class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_all(self):
        print(f"name: {self.name} age: {self.age}")
    def set_name(self,name):
        self.name = name
        print("name updated sucessfully!")
    def set_age(self, age):
        self.age = age
        print("age updated sucessfully")

#Example usage
first_student = Student("Abebe" , "20")
  # now let's use the methods
first_student.get_name()
first_student.get_age()
first_student.get_all()
first_student.set_name("Kebede")
first_student.set_age(30)
first_student.get_name()
first_student.get_age()
first_student.get_all()