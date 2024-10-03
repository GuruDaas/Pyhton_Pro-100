def prime_num(postive):
    if postive <= 1:
        return False
    for i in range(2, int(postive ** 0.5)+1):
        if postive % i == 0:
         return False
        
    return True

num = int(input("Enter the value is : "))  

if  prime_num(num):
   print("Ist is the prime number: ")
else:
   print("It is not a prime number: ")   


    

    