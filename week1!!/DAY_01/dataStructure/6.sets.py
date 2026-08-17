"""
Sets in Python:

- A set is an unordered collection of unique elements.
- Sets automatically remove duplicate values.
- They are useful for:
    1. Checking whether an element exists (membership testing).
    2. Removing duplicate values.
    3. Performing mathematical set operations.

Set operations include:
    - Union (|)
    - Intersection (&)
    - Difference (-)
    - Symmetric Difference (^)

Creating a set:
    numbers = {1, 2, 3, 4}
    numbers = set([1, 2, 3, 4])

Important:
    - To create an empty set, use set().
    - {} creates an empty dictionary, NOT an empty set.

Example:
    numbers = {1, 2, 2, 3, 3}
    print(numbers)
    # {1, 2, 3}

Sets are unordered, so the order of elements may be
different when printing or iterating over a set.
"""

basket = {'apple', 'orange', 'apple', ' pear', 'orange','banana'}
print(basket)

print('orange' in basket)
print('crabgrass' in basket)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

print(a)# unique letters in a
print(a-b) # letters in a but not in b
print(a | b) # letters in a or b or both
print (a&b)# letters in both a and b
print(a^b)# letters in a or b but not both


# set comprehension are also supported
a = {x for x in 'abracdabra' if x not in 'abc'}
print(a)