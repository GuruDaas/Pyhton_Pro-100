import math

facto = int(input("Enter the value: "))

if facto < 0:
    print("It is not defiend the nagtive fectorial number")
else:
    tom = math.factorial(facto)

    print(f"the factorial {facto} is: {tom}")