def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b # Update a and b for the next iteration
    print()  # for a new line after the series

fib(2000)        

print(fib(10)) # does not return anything, so it will print None

fib100 = fib(100) # This will print the Fibonacci series up to 100, but fib100 will be None



#default argument
# def ask_ok (prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)

# ask_ok('Do you really want to quit?')        

i = 5 
def f(arg=i):
    print (arg)

i= 8
f()

""""
important note: default argument values are evaluated only once when the function is defined,
 not each time the function is called.
   This can lead to unexpected behavior when using mutable default arguments like lists or dictionaries.
"""
def d(a, L=[]):
    L.append(a)
    print(L)

d(1)   
d(2)
d(3) 

#if you want to avoid this behavior, you can use None as the default value and then create a new list inside the function if needed.
def g(a,L = None):
    if L is None:
        L = []
    L.append(a)
    print(L)
g(1)
g(2)
g(3)
