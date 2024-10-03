def prime_num(postive):
    if postive <= 1:
        return False
    for i in range(2,int(postive ** 0.5)+1):
        if postive % i == 0:
            return False
        return True

def PrintAllNum(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if PrintAllNum(num):
            print(num, end=" ")
    print()    

start = int(input("Enter the start of the invalid : "))   
end = int(input("Enter the end of the invalid: ")) 

PrintAllNum(start ,end)



