def basic_operations(*args): # THIS IS USED TO FOR A FUNCTION WITH NUMBER OF POTENTIAL ARGUMENTS ARE DIFFERENT
    sum, multiple = 0,1
    for num in args:
        sum+=num
    for num in args:
        multiple *= num
    
   

    print (f"The sum is {sum}")
    print (f"The multiple is {multiple}")
    return sum,multiple   #returning multiple element as a tuples


sum , multiple = basic_operations(1,2,3,4)
sum +=1
print (sum)
