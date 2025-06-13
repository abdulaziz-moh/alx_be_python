def sayhelloto(name = None):
    print("hello world")
    if name:
        print(f"hello {name}!")
    
    def innerfunction():
        # nonname = name + "Moh"
        # print(f"this is befor using nonlocal. name: {name}")
        
        nonlocal name
        name = name + "Mohammed"
        print(f"this is after using nonlocal. name: {name}")

# sayhelloto()
sayhelloto("Abdulaziz")
# innerfunction()