# check the number postive and nagetive

def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."

number = float(input("Enter a number: "))
result = check_number(number)
print(result)
