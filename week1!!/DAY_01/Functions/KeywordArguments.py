# fuction can alo be called using keyword arguments of the form kwarg = value.
def parrot(voltage, state='a stiff', action ='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)    
#parrot(volatage=1000)# it will show error because of wrong keyword argument spelling. It should be voltage instead of volatage
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')       #3 positional arguments
parrot('a thousand', state='pushing up the daisies')


def cheeseshop(kind, *arguments, **keywords): # * is used to pass a variable number of non-keyword arguments to a function. It allows you to pass any number of positional arguments to the function, which are then accessible as a tuple within the function. ** is used to pass a variable number of keyword arguments to a function. It allows you to pass any number of keyword arguments to the function, which are then accessible as a dictionary within the function.
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",    
            shopkeeper="Michael Palin",
            client="John Cleese",
            sketch="Cheese Shop Sketch")        