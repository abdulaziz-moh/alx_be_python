my_list = ["a","b","c"] 
inventory = {"Orange":10,"Mango":20,"Banana":100}

print(x+1) # NameError
print("abebe" + 5) # TypeError
print(my_list[3]) # IndexError
print(5/0) # ZeroDivisionError
int("ab")  # ValueError
inventory["Apple"] # KeyError

def process_string(data):
    if not isinstance(data, str):    # use isinstance() functioin To ensure a Python function only accepts a single data type for a particular argument
        raise TypeError("Argument 'data' must be a string.")
