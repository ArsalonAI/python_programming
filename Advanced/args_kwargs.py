
# *args as parameter 
# allows us to pass any number of arguments to a function
# stores all args in a tuple as they appear

def sum_items(*args):
    print(sum(args))
    
sum_items(1, 2, 3)
sum_items(2, 3, 4, 5, 6, 7)


# **kwargs as parameter
# allows us to pass keyword arguments - stores in a dictionary (k-v pairs)
def print_items(*args, **kwargs):
    print(args)
    print(kwargs)
    
print_items(1, 2, a = 3, b = "string", c = 9)


# *args and **kwargs as args (unpacking operators) - splat operator - one star '*' unpacks a string, list, etc
def take_items(a, b, c):
    return a + b + c 

items = [4, 5, 6] # list 
new_items = {"a" : 10, "b" : 15, "c" : 24} # dictionary 

print(take_items(*items)) # separates the positional datastructure (collection), passing each element one at a time to the fn as parameters
print(take_items(**new_items)) # double '**' unpacks a dictionary - allows to use dictionary as arg to function 


# we can use *args and **kwargs as splat operator args (together) 
demo_list = [1, 2,]
demo_dict = {"a": 5, "b": 10, "c": 15}

def splat_demo(p1, p2, a=None, b=None, c=None):
    print(p1, p2, a, b, c)
    return a + b + c + p1 + p2

x_y = splat_demo(*demo_list, **demo_dict)
print(x_y)


#using *args and **kwargs as args to unpack and print lists/dicts easily
values = [1, 2, 4, 5, 6, 7, 8, 9]
print(*values) # splits everything into individual arguments and pass them to fn

list_values = [1, 2, 3, 4]
map_values = {'end': "|", 'sep': "*"} # unpacks to end = | and sep = * (print fn accepts these params to give separator and end of print statment)
print(*list_values, **map_values)


# Excercise - write a fn that accepts unlimited num of positional and keyword args
# Return True if there are at least 4 args and keyword arg "num" exists and is a number larger than 5
# otherwise return false 
def get_args_and_kwargs(*args, **kwargs):
    num_args = len(args) + len(kwargs)
    num = kwargs.get("num", 0)
    
    if not isinstance(num, int) and not isinstance(num, float):
       return False

    return num_args >= 4 and num > 5

print(get_args_and_kwargs("a", [2], 3, num=6))