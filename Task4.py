n=int(input("Enter a number"))
i=int(input("Number of times"))
c=1
j=0
summ=0
while c<i:
    j=j*10+n
    print(j)
    summ =summ+j
    c=c+1
print(f"the sum is {summ}")


