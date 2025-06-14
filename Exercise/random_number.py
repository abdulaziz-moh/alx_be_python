#Exercise 3: Write a program to generate a random set of numbers between 1 and ten.
# Use set operations to remove duplicates and display the unique numbers.
import random
non_unique_list = []
for i in range(10):
    non_unique_list.append(random.randint(1,10))

print(f"The non random list is : {non_unique_list} with length {len(non_unique_list)}")
print(f"The unique list is : {list(set(non_unique_list))} with length {len(list(set(non_unique_list)))}")
#OR we can make it like this without using the list
print(f"The unique list is : {set(non_unique_list)} with length {len(set(non_unique_list))}")