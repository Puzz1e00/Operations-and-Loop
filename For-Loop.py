"""for i in range(10): #it ranges from 0 to 9
    print(i)

for i in range(1,10):#from 1 to 9
        print(i)"""

"""for i in range(1,31):

    if i%3==0 and i%5==0:
        print("FizzBuzz", end=" ")
        
    elif i%3 == 0:
        print("Fizz", end=" ")
    elif i%5==0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")"""
     #Looping in List
#for x in [1,2,'a']:
 #   print(x)
     #Looping in tupple
#for x in "hey":
 #   print(x)
#for x in range(1,30):
 #   print(x, end=" ") if x%3==0 else print("n", end= " ")

     #Looping in dictionary
# d= {
#     "name": "ABC",
#     "age" : 24,
#     "address" :"XYZ"
# }
#print(list(d.keys()))
#for key in d.keys():
 #   print(key)
#for values in d.values():
 #   print(values)

#for i in d: #same as d.keys() but only in the loop
 #   print(i)
# print(d.items())
#
# for key,value in d.items():#unpacking
#     print(key,value)

a= [1,2,3,4]
for i in a:
    print(i)
print(list(enumerate(a)))#output-[(0, 1), (1, 2), (2, 3), (3, 4)], first value is index.
for i in enumerate(a):
    print(i)
for index,value in enumerate(a):#tupple unpacking
    print(index,value)
for index,value in enumerate(a,start=1):
    print(index,value)
    



