# annonymous, one line functions defined where they're used 
# use "lambda" keyword to right is parameters
# after colon ':' it's the function body (evaluated and returned) from fn

func = lambda x, y, z = 0: print(x + y + z)
func(1, 2)


# named function - selects the value from a kv pair as the sort parameter
def sort_func(x):
    return x[1] 

lst = [(1,2), (-3, 5), (0, 0), (5, 8)]
lst.sort(key=sort_func)
print(lst)


# use lambda 
lst_two = [(1,2), (-3, 5), (0, 0), (5, 8)]
lst_two.sort(key=lambda x: x[1])
print(lst_two)

# return lambda from a lambda
mul = lambda x: lambda y: x * y

result = mul(2) # we have another function in result variable (first fn returns a fn)
print(result(4)) # call the second fn and pass the final arg

result_two = mul(4)(4) # chain fn calls, whatever fn is returned w/ first arg, second arg is passed and second fn called
print(result_two)

# Excercises

add_values = lambda x, y, z: x + y + z # takes three ints/floats, returns sum

max_length = lambda string1, string2: max(len(string1), len(string2)) # takes two strings, returns max of lengths

create_set = lambda list1, list2: set(list1).union(list2) # takes two lists, returns a set of both lists 