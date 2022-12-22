import math
# Map -> map all values in an iterable object (collection) to a new value
# Filter -> filter for specific values in an iterable object

lst = [1, 2, 3, 4, 5, 6, 7]

new_lst = map(lambda x: x**2, lst)  # map -> takes a fn (lambda) and iterable obj -> return iterable obj

for value in new_lst:
    print(value)
    
lst_two = [1, 2, 3, 4, 5, 6, 7]
new_lst_two = list(map(lambda x: math.sqrt(x), lst_two)) # type conversion - convert iterable obj to list w/ list() fn
print(new_lst_two)

# Map fn for nested lists 
nested_list = [[1, 2, 6] , [3, 4, 8, 9] , [5, 6, 7]] 
nested_sum = list(map(lambda x: sum(x), nested_list)) # each arg is a list, returns a list of sum of elements
print(nested_sum)

