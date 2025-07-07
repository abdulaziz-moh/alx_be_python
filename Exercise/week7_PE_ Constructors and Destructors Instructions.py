class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"The object {self.name} is deleted for memory managment")

print("--------------------------------------------------")
per_1 = Person("ABEBE", 15)
print(f"Name: {per_1.name} Age: {per_1.age}")
print("Done_1")  

# Still the object(for ABEBE while we don't use it afterward) exist because Python’s garbage collector will automatically delete it when it goes out of scope, which typically happens at the end of the program if you don’t delete it earlier.
del per_1  
# Here, the destructor is called before the program ends because we explicitly deleted the object with del per_1 
print("--------------------------------------------------")
p = Person("Sara",20)
p = Person("Ali",18)  # Previous object ("Sara") is now unreferenced
                      # Now the object for sara will be deleted and new object with name ali will be created(because it is unreferenced)
                      # Ali will be deleted at the end of the progrm
                      # See the output
print("Done_2")
print("--------------------------------------------------")
