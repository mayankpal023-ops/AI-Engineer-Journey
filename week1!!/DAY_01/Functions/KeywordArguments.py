# fuction can alo be called using keyword arguments of the form kwarg = value.
def parrot(voltage, state='a stiff', action ='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)    