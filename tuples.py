# immutable collection data type (can included embedded tuples, etc)
# methods - can access elements by index (like a list or string)
# constraints - cannot directly update / modify 

tup = (1, 2, 2, (1, 3), True, [], 3)
print(tup)
print(tup[1]) # access element at index 1, the number 2 

# tup[1] = 3  results in an error because doesn't suport item assignment 

num_elements = tup.count(2)
print(num_elements)

index = tup.index(2)
print(index)

# in operator 
contains = 3 in tup
print(contains)

# get nested elements 
print(tup[3][0]) # expect element 1 in the nested tuple (1, 3)

# multiple + add tuples

tup_x = (1,3)
mult_tup = tup_x * 3 # extends the tuple by repeating the elements * n 
print(mult_tup)

tup_y = (2, 5)
add_tup = tup_x + tup_y
print(add_tup)
