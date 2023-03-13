# def func(name):
#     return "Hello " + name.upper()+ '.'
# def greet(a):
#     message= a('Jane')
#     print(message)
# greet(func) #func is sent as a variable so above a is replaced by func which then calls to the first function
def greet(msg):
    def print_message():
        print(msg)
    return print_message
message=greet("Hello World")
message()

