class Shape:
    def __init__(self):
        pass
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
    def calculate_area(self):
        print(f"Area: {self.x*self.y} unit square")

rec = Rectangle(4,5)
rec.calculate_area()