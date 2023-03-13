# import time
#
#
# def decorate_me(func):
#     def inner_func(*args, **kwargs):
#         print("It is a decorated function")
#         return func(*args, **kwargs)
#     return inner_func
#
#
# @decorate_me
# def addition(a, b):
#     return a + b
#
#
# # r = decorate_me(addition)
# start= time.time()
# print(addition(3, 4))
# end= time.time()
# print(f"Time is {end-start} ")
# print(r())

# import time
#
#
# def execution_time(func):
#     def inner_func(*args, **kwargs):
#         start = time.time()
#         r = func(*args, **kwargs)
#         end = time.time()
#         print(f"Execution time is {end - start}")
#         return r
#
#     return inner_func
#
#
# @execution_time
# def message_print():
#     for i in range(1000000000):
#         pass
#     print("Hello World")
#
#
# message_print()

def password_required(func):
    def inner_func(*args, **kwargs):
        a = input("Enter your password")
        if a == '1234':
            return func(*args, **kwargs)
        else:
            return "You have no access"

    return inner_func


@password_required
def message_print():
    return "hello world"


#  message_print = password_required(message_print)
print(message_print())

