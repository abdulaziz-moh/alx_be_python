def count_function_one(countedstring):
    count = 0
    for val in countedstring:
        count+=1
    print(f"count variable in count_function_one is: {count}")

def count_function_two(countedstring):
    count = 0
    for val in countedstring:
        count+=1
    print(f"count variable in count_function_two is: {count}")

# here the result shows us each of a count variable in this code are different.
count_function_one("12345")
count_function_two("1234567890")   