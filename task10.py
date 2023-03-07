def repeated_items(a):
    c=[]
    for i in a:
        b=a.count(i)
        if b>1 and i not in c:
            c.append(i)
    return c

a=[3,4,2,2,1,3,3,3]
r=repeated_items(a)
print(r)





