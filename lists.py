# collection of multiple elements - data types do not need to be the same
# elements in the list are "ordered" meaning they're in order (indices)
# index is the position of the element in the list 

x = [1, 2, 3, True, 2.4, "Hello"]
print(x[3]) # gives us the x[n] element in the list 

# replace an element in the list at a specific index
x [3] = False # cannot add an element to a spot that doesn't exist yet or get "list assignment index out of rang error"
print(x)

# add element in the list at the end 
x.append("Goodbye") 
print(x)

# get length of the list 
print(len(x))

# remove last element in list + return it
last_element = x.pop() 
print(last_element)
print(x)

# count how many times an element occures in a list
x.append(1)
x.append(1)
x.append(1)
print(x)
num_frequency = x.count(1)
print(num_frequency)

# get index of first occurance of element searching (element must exist or get an error)
boolean_index = x.index(False)
print(boolean_index)

# remove the first occurance of element in list - get error if doesn't exist 
x.remove(False)
print(x)

# in operartor - check if the list contains an element
is_present = 1 in x 
print(is_present)

# negative index access last elements
y = [0 , 1 , 2, 3]
print(y[-1])
print(y[-2])

# combine list using + or using "extend" method
z = [ 1 , 2, 3]
t = [ 4, 5, 6]
combine = z + t
print(combine)

v = [1, 2, 3]
b = [4, 5, 6]
v.extend(b)
print(v)

b.extend([1, 1, 1])
print(b)


# nested lists - multidimensional lists 
lst = [[1, 2, 3], [ 4, 5, [False]], [7, 8, True]]
print(lst[-1]) # gives us list at this index
print(lst[-1][-1]) # gives us last element in the last list "True" 
print(lst[1][-1][0])
