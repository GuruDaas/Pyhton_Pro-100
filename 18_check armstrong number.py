num = int(input("Enter a number : "))
convert=str(num)
i=0
cur=0
sum=0
while(i<len(convert)):
    cur=int(convert[i])
    sum=((cur**3)+sum)

    i=i+1
print(sum)

if sum==num:
    print("your number is armstrong")
else:
    print("your number is not armstrong")    