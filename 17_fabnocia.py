elements =int(input("enter a range of fabnoc series : "))

pre =0
cur=1
i=1
while(i<elements):
    print(i<elements)
    next = cur+pre
    pre=cur
    cur=next
    print(next)


    i=i+1
    
