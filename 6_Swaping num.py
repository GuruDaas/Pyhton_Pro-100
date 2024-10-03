# swapping numbers 

def swapNum(a, b):
    num = a
    a = b
    b = num
    return a, b

x = 5
y = 10

x, y = swapNum(x, y)
print(f"After swapping: x = {x}, y = {y}")
