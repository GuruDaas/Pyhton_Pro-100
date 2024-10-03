def devisible_num(room1, room2):
    if room1 == 0:
        return "devisible zero is not allowed"
    return room1 % room2 == 0

room1 = int(input("enter the first number : "))
room2 = int(input("enter the second number : "))

if devisible_num(room1, room2):
    print(f"{room1} is devisible by {room2}")
else:
    print(f"{room1} is not devisible by {room2}")
    


