class Calculator:
    @staticmethod
    def add(a,b):
        return a+b
    # or without it but recommended to put @staticmethod
    def multiply(a,b):
        return a*b
    
print(Calculator.add(1,2))