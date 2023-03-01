"""
#They are handled by if
#Every statement is taken with a boolean expression
#In python we write elif
#All if program checks all conditions, with elif program stops after one statement is true
"""
a = int(input("Enter your first number"))
b = int(input("Enter your second number"))
c = int(input("Enter your third number"))
if a > b and a > c:
    print(f"{c}is the greatest")
elif b > a and b > c:
    print(f"{b}is the greatest")
else:
    print(f"{c} is the greatest")