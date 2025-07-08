class Bird:
    def __init__(self):
        pass
    def fly(self):
        print("Bird is flying...")

class Mammal:
    def __init__(self):
        pass
    def run(self):
        print("Mammal is running...")

class Bat(Bird,Mammal):

    def fly(self):
        print("Bat is flying...")

    def run(self):
        print("Bat is running...")

new_bat = Bat()
new_bat.fly()
new_bat.run()