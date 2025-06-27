######## To import a module from a parent directory, you can use one of the following methods:

#================ Method 1: Relative Import (Recommended for packages) ========================================================================================================================================================================================================================#

# Run this script as a module using the -m flag. from the parent directory (fns_and_dsa):
#     python -m main.main_arithmetic_operations
# This allows Python to find the `arithmetic_operations` module correctly.(because python is capable of only serching for modules in the same or sublevel directories) when we run it from the parent directory now arithmetic_operations is in the same level as main_arithmetic_operations.py
# Note: This method requires the script to be run as a module, not directly.

# ⚠️ Running it directly (e.g., `python main_arithmetic_operations.py`) may raise ModuleNotFoundError
# because Python doesn't search parent directories by default.
# Also make sure that both the fns_and_dsa and main directories are packages (i.e., they contain an __init__.py file).

# import arithmetic_operations  # Importing from the parent directory
#===========================================================================================================================================================================================================================================================================================#


#================ Method 2: Absolute Import (Alternative if PYTHONPATH is configured) =========================================================================================================================================================================================================#

# Modifying the sys.path (A bit less clean, but works)
# This method allows you to run main.py directly from the main directory using python main_arithmetic_operations.py.
# This method involves programmatically adding the parent directory to Python's search path. 
# It's useful when you can't run your script as a module or for quick scripts.

import sys
import os
                                                                           
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    # Get the path to the parent directory (fns_and_dsa)
                                                                            # os.path.abspath(__file__) gives you the absolute path to main_arithmetic_operations.py.
                                                                            # os.path.dirname() gets the directory name from a path. We use it twice to go up two levels: first from main_arithmetic_operations.py to main/, then from main/ to fns_and_dsa/.
sys.path.append(parent_dir)     # sys.path.append() adds the fns_and_dsa directory to the list of places where Python looks for modules.
import arithmetic_operations    # Now you can import arithmetic.py directly because its directory is in the search path.

#===========================================================================================================================================================================================================================================================================================#

# Use the function

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = arithmetic_operations.perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
# When a Python file is run:
        # Python sets the built-in variable __name__ to "__main__".
        # If the file is run directly (e.g., python main_arithmetic_operations.py), the main() function will execute.

# When a Python file is imported into another script:
        # Python sets __name__ to the module’s name (e.g., main.main_arithmetic_operations).
        # This is useful when file is imported elsewhere (like for testing or reuse), the main() function won’t run automatically, preventing unintended execution.
