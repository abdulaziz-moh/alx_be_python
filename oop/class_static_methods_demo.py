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