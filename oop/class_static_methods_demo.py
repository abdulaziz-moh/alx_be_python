class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method that returns the sum of two numbers.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method that returns the product of two numbers.
        It prints a class attribute before performing the multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# main.py (Provided for Testing):
# This script will test the Calculator class’s static and class methods, demonstrating their functionality and how they are called.

# from class_static_methods_demo import Calculator

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")

if __name__ == "__main__":
    main()

# Note for you:
# Understand the use of @staticmethod for functions that perform a task in isolation, without needing access to class or instance-specific data.
# Grasp the concept of @classmethod for functions that need to access class attributes or methods and understand how the cls parameter allows access to class-level attributes.
# This task underscores the distinction between class methods and static methods in Python, providing clarity on their appropriate use cases and advantages.