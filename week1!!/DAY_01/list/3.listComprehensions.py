# List comprehensions provide a concise way to create lists.
#
# They are commonly used to:
# 1. Apply an operation to each element of another sequence.
# 2. Create a new list containing only elements that satisfy a condition.
#
# Basic syntax:
# [expression for item in iterable]
#
# With a condition:
# [expression for item in iterable if condition]

square = []
for i in range(11):
    square.append(i**2)
print(square)

squares = [x**2 for x in range(11)]
print(squares)

squares = list(map(lambda x: x**2, range(11)))
print(squares)

marks = [20,30,40,50,60]
newMark = [x+2 for x in marks]
print(newMark)

# example: this listcomp combines the elements of two lists if they are not equal
lihh = [(x,y) for x in [1,2,3] for y in [2,5,3] if x !=y]
print(lihh)

comb = []
for x in [1,3,4]:
    for y in [2,3,1]:
        if x != y:
          comb.append((x,y))

print(comb)


vec = [-4,-2,0,3,4]
double=[x**2 for x in vec]
print(double) 