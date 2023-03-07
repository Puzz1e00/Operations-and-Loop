# names = ["Jon","Jane"]
# name = iter(names)
# print(next(name))
# print(next(name))
# print(next(name))
"""For loop in while loop"""
names = ['jon','jane']
name_iter = iter(names) # iterable into iterator object
while True:
    try:
        name=next(name_iter)
        print(name)
    except StopIteration:
        break