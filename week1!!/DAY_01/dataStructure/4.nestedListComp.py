#Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 32, 8],
    [9, 10, 11, 12],
]

transpose = [[row[i] for row in matrix] for i in range(4)]
print(transpose)


transposed = []
for i in range(4):
    newRow = []
    for row in matrix:
        newRow.append(row[i])
    transposed.append(newRow)


print(transposed)      

#In the real world, you should prefer built-in functions to complex flow statements. The zip() function would do a great job for this use case:
print(list(zip(*matrix)))
# Transpose a matrix using zip() and unpacking.
#
# *matrix → unpacks each row of the matrix as a separate argument.
#
# zip() → takes the corresponding elements from each row
#         and groups them together.
#
# list() → converts the zip object into a list.
#
# Example:
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
#
# list(zip(*matrix))
# → [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
#
# In short:
# *      = unpack rows
# zip()  = combine corresponding elements
# list() = convert result into a list

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[2:4]
print(a)