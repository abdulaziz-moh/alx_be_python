path = input("Enter the path: ")
# use this path for test 
#C:\Users\Administrator\Desktop\files ohter than scool\ALX\text.txt
try:
    with open(path,'a+') as my_file:
        my_file.write("This is a new line\n")
        my_file.seek(0)
        print(my_file.read())
     
except FileNotFoundError:
    print(f"Can't find the file in {path} location")