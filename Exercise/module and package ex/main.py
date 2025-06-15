from directory import utility_module # shows how to import a module from a package 
                                     # (recommended way to import modules) This is the recommended way to import modules from a package.
                                     # Now we can use the functions and classes defined in utility_module.py using utility_module plus dot notation.
import directory.utility_module  # (similar task to the above method ) Importing the module directly from the package.
                                 # (less recommended than the above method) but it is less recommended than the above method. because it is less readable and can lead to confusion if there are multiple modules with the same name in different packages.

from directory.utility_module import add, subtract, user  # Importing specific functions and classes from the module
                                                          # (good practice) This is a good practice as it makes the code more readable and avoids name conflicts.

from directory.utility_module import user as User # Importing the module with an alias
                                                  # (good practice) This is a good practice as it makes the code more readable and avoids name conflicts.
import directory.utility_module as util # Importing the module with an alias (name of the utility_module module used here as util)
                                        # (good practice) This is a good practice as it makes the code more readable and avoids name conflicts.
from directory.utility_module import *  # (not recommended) This will import all the functions and classes from the module, but not recommended. 
                                        # It can lead to name conflicts and makes the code less readable.
                                        # It is better to import only the required functions and classes or use an alias for the module.

my_user = util.user("John", 30)  # Creating an instance of the user class
x = utility_module.add(1,2)  
print (x)
y = utility_module.subtract(2,1) # Using the add and subtract functions from the utility_module
print (y)