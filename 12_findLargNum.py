value_1 = int(input("Enter the first number : "))
value_2 = int(input("Enter the second number : "))
value_3 = int(input("Enter the third number : "))

if value_1 > value_2 and value_1 > value_3:
    print("The first number is largest : ", value_3)
elif value_2 > value_1 and value_2 > value_3:
    print("The second number is largest : ",value_2)  
else:
    print("The third number is largest : ",value_3)     