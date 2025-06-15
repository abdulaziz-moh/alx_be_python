def divide(a,b):
    try:
        result = a / b
        print(f"Result: {result}")
        return result
    except TypeError:
        print("Both arguments must be numbers!")
    except ZeroDivisionError:
        print("The denominator cannot be zero!")
    else:  # this block in not reached even if there is no exception because the function returns before reaching this block
        print("Division successful!")
    finally:
        print("Execution of divide function completed.\n")
    
divide(10, 2)  # This will print the result of the division
divide(10, 0)  # This will raise a ZeroDivisionError and print the error message
divide(0, 10)  # This will print the result of the division


# alternative way to handle exceptino using----"raise"------implementation of divide function with ZeroDivisionError handling
def divide(x, y):  
  if y == 0:
    raise ZeroDivisionError("Division by zero is not allowed")
  return x / y