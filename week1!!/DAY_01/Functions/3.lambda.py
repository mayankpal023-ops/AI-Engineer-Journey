# its is anonymous function which can take any number of arguments but can only have one expression
numbers = [1,2,3,4,5]
def even(x):
    return x % 2 == 0
evens = list(filter(even, numbers))
print(evens)

# instead of defining a function, we can use lambda function to achieve the same result
numbers = [1,2,3,4,5]
evens = list(filter(lambda x : x % 2 == 0, numbers))
print(evens)

#another example of lambda function
city = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
def length(city):
    return len(city)
sort = sorted(city, key = length)    
print(sort)

# instead of defining a function, we can use lambda function to achieve the same result
city = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
sort = sorted(city, key=lambda city: len(city))
print(sort)