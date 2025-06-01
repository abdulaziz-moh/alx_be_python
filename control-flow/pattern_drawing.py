# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Use while loop to draw rows
row = 0
while row < size:
    # Use for loop to draw columns in each row
    for col in range(size):
        print("*", end="")
    print()  # Newline after each row
    row += 1
