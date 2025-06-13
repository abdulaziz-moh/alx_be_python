users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

for  ids in users.keys():
    value = users[ids]
    print(f"id: {ids}, value: {value}")

print(list(range(5, 10)))
print(list(range(-10, -100, -30)))

print(range(10))  # This line has a typo and will raise an error
print(list(range(10)))  # Corrected the typo from 'pritn' to 'print'

# while True:
#     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
# # The above code will run indefinitely until interrupted
# # The following code will run indefinitely until interrupted
# for i in range(10):
#     print(i)
#     if i == 5:
#         break  # Exit the loop when i is 5