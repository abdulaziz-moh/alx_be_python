# Create a list to store names of your favorite fruits
favorite_fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

# Access the second element (lists are zero-indexed, so the second element is at index 1)
second_fruit = favorite_fruits[1]

# Print the second element
print(f"My second favorite fruit is: {second_fruit}")

# You can also directly print it without storing it in a variable first:
print(f"The fruit at the second position is: {favorite_fruits[1]}")

print (f"the sliced list from index 1 to 4 with gap 2: {favorite_fruits[0:4:2]} which doesn't include the 4th index")

newtuple = (1,2,3)
newtuple[0]+=1 # this line couses error. because tuple object cann't be changed(immutable).
print(newtuple[0]) 
