"""
Dictionary:
- Stores data as key:value pairs.
- Keys must be unique and immutable.
- Common keys: strings, numbers, and tuples.
- Lists cannot be used as keys because they are mutable.

Example:
    student = {"name": "Mayank", "age": 18}

Useful operations:
    d[key]          → access value
    d[key] = value  → add/update
    del d[key]      → delete
    d.get(key)      → safely access a value
    If the key doesn't exist, get() returns None
    instead of raising a KeyError.
    key in d        → check if key exists
    list(d)         → get all keys

{} creates an empty dictionary.
"""
tel = {'jack': 2345, 'sape': 3422}
tel['guido'] = 2313
print(tel)
print(tel['jack'])

print(tel.get('irv'))

# del tel ['sape']
# print(tel)

print(list(tel))

print('guido' in tel)

# dict comprehensions
dic = {x: x**2 for x in (2,3,5)}
print(dic)