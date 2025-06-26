
# To import from the parent directory, ensure that the parent directory is in the Python path.
# This can be done by running the script from the parent directory or by modifying the PYTHONPATH environment variable.
#

#Method 1: Using relative imports (Recommended for packages)
# Important: To run main_perform_operation.py using this method, you need to execute it as a module from the parent directory (alx_be_python).
# If you try to run python main.py from inside the main directory, you will likely get a ModuleNotFoundError because Python won't know the context of the parent package.
# so we will run it as a module using the -m flag. from the parent directory(fns_and_dsa)
# # we use this command "python -m main.main_perform_operation"
import arithmetic_operations # Importing the arithmetic_operations module from the parent directory

# Method 2: Using absolute imports (if the parent directory is in the Python path)

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = arithmetic_operations.perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
