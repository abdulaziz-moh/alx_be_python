class OutOfStockError(Exception):                            # DEFINITON OF THE CUSTOME EXCEPTIONS
    def __init_(self,name):
        self.name = name
    def __str__(self):
        print(f"{self.name} is empty")

class InsufficientAmountExcepiton(Exception):
    def __init_(self,name):
        self.name = name
    def __str__(self):
        print(f"amount you ordered for {self.name} is insuficient in our stock")

#======================================================================================#

my_stock = {"Orange":10,"Mango":20,"Banana":100,"Apple":0}  # HASH TO STORE THE INVENTORIES

#======================================================================================#

def use_custom_exception(item,amount_needed):               # A FUNCTION THAT USES THE CUSTOM EXCEPTIONS
    
    try:

        if my_stock[item] == 0:
            raise OutOfStockError
        elif amount_needed - my_stock["item"] < 0:
            raise InsufficientAmountExcepiton            
    except KeyError:
        print(f"Their is no {item} in the store")

#======================================================================================#
            
try:                                                        # THIS IS WHERE WE USE THE EXCEPTIONS FOR HANDLING ERRORS
    use_custom_exception("Mango", 3)  # Purchase successful
    use_custom_exception("Apple", 1)  # Raises OutOfStockError
    use_custom_exception("Orange", 20)  # Raises InsufficientAmountExcepiton  
    use_custom_exception("watermelon", 3)  # Raises KeyError
except OutOfStockError as e:
    print(e)
except InsufficientAmountExcepiton as e:
    print(e)
else:
    print("order sucussfully submitted")
finally:
    print("This is finally block")

#======================================================================================#
