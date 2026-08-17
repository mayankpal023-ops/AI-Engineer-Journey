users = {'rahul': 'active', 
         'tarzan': 'inactive',
         'loser': 'active'}

# Strategy:  Iterate over a copy
for user,status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
activeUser = {}
for user,status in users.items():
    if status == 'active':
        activeUser[user] = status

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])     

print(sum(range(4)))
