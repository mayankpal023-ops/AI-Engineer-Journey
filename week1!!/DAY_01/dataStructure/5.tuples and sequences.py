#A tuple consists of a number of values separated by commas, for instance:
t = 12345, 56789,'hello!'
print(t[0])

# tuples may be nested
u = t , (1,2,3,4)
print(u)

# tuples are immutable
t[0] = 333
print(t)

# the reverse operation  is also possible 
x, y ,z = t