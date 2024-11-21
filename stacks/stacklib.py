import queue

""" *LifeQueue in Python
    -Python queue module 
    -behaves like a stack
"""

my_book_stack = queue.LifoQueue(maxsize=0)
my_book_stack.put("The misunderstanding")
my_book_stack.put('hello world: the horror movie')
my_book_stack.put("jhal dhab")

print(f"The Size is: {my_book_stack.qsize()}")

print(my_book_stack.get())
print(my_book_stack.get())
print(my_book_stack.get())

print(f"Empty stack: {my_book_stack.empty()}")