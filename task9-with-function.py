def custom_sort(a):
    b=len(a)
    for i in range(b-1):
        for j in range(i+1, b):
            if a[i]>a[j]:
                a[i],a[j]= a[j],a[i]
    return a

a=[54,1,12,99,20,13,5,100]
result= custom_sort(a)
print(result)