S="All the occurrences of a specified character in a given string"
l = input("Enter letter")
result=""
for i in S:
    if i.lower() ==l.lower():
        continue
    result=result+i
print(result)