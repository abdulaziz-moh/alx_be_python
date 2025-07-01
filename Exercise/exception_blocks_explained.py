try:
    x = int(input())
    y = int(input())
    print(x/y)
except ZeroDivisionError:
    print("The denominator can't be zero") # This executed if the try block not executed sucessfully
# We can have multiple except blocks here. 
else:
    print("Succesfull division")  # This executed if the try block executes sucessfully
finally:    # Always executed
    print("if succesfull continue..\n else try again")