def whole(a):
    b = 0
    for i in a:
        b = b * 10 + i
    return b
a=[4,5,6]
result= whole(a)
print(result)