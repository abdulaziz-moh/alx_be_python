# Class Methods in Python: Key Points
# What they are: Special methods inside a class that operate on the class itself, not on individual instances.
# Why use them? Great for tasks like tracking data shared across all instances (e.g., a counter for how many objects have been created) or for class-wide operations.
# The magic decorator: The @classmethod decorator is the standard and best practice for defining them.
# How @classmethod works: It automatically passes the class itself as the first argument to your method (we usually name this cls). This cls argument lets you easily access and modify class-level attributes.
# Calling them: You can call class methods from anywhere within your class, even from the __init__ constructor. Just use the class's name (e.g., MyClass.my_class_method()) or self.__class__.my_class_method().
# Skipping the decorator? Not recommended! While you might technically find a workaround without @classmethod, it's a recipe for confusing code and TypeError issues. Your method won't automatically receive the crucial class reference it needs.
# The takeaway: Stick with @classmethod for clear, reliable, and Pythonic code when you want a method to interact with the class itself.






class Product:
    total_value = 0  # Class variable to keep track of the total value of all products
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.product_x_total = self.calc_product_x_total()
        Product.get_total()  # Call the class method to update the total value when a new product is create
        Product.calculate_total(Product,self.product_x_total)  # Update the total value of all products


    def calc_product_x_total(self):
        print(f"The total value of {self.name} is {self.price * self.quantity}")
        print("The total before adding this product is: ",end=" ")
        return self.price * self.quantity

    
    #here because we aren't using the decorator @classmethod, we need to pass the class(that is class name when you pass is as argument. And cls when you put it as a parameter) as the first argument, when we call this method each time.
    #not recommended to use this method without the decorator, as it can lead to confusion and errors.
    def calculate_total(cls,product_x_total):
        cls.total_value += product_x_total

    @classmethod  # Here the @classmethod decorator automatically passes(injects) the class as the first argument to the method.
    def get_total(cls):
        print(cls.total_value)

#Example 

first_product = Product("banana",5,10)

print(f"now after adding {first_product.name} we get the total {first_product.get_total()}")
second_product = Product("apple",3,20)
print(f"now after adding {second_product.name} we get the total {second_product.get_total()}")
