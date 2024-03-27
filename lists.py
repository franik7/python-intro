list_name = ['animals', 'fruits']

print(list_name[0])

list_name[0] = 'cat'

print(list_name[0])
print(list_name[-1])


list_name.append('cow')
print(list_name)

list_name.extend(['duck', 'dog'])
print(list_name)


list_name.insert(2, 'horse')
print(list_name)


some_names = list_name[1:4] #4 not included
print('{}'.format(some_names))

some_names2 = list_name[:2] #4 first two
print('{}'.format(some_names2))

last_one = list_name[-1:] # last one
print('{}'.format(last_one))

##slices can also be used with strings


##find an item in the list

animals = ['man', 'bear', 'pig']
try:
    bear_index = animals.index('chicken')
except:
    print('There is no chicken')


##loops
for animal in animals:
    print(animal.upper())

## while loops
    
n = 0   
while n<5:
    print(n)
    n = n+1

##sorting and ranges
sorted_animals = sorted(animals)
print(sorted_animals)

more_animals = ['elephant', 'rhino']
print(animals + more_animals)

##range
for num in range(1, 10, 2):
    print(num)
