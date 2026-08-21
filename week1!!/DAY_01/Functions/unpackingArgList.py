print(list(range(3,6)))

arg = [3,6]
print(list(range(*arg))) # unpacking the list into positional arguments

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")    

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)     