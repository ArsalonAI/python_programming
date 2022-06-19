# converting one data type into another data type
# sometimes we are given a value in a particular data type but cannot use it unless we convert the value to a different type

# convert string to integer - must be a valid integer in the string
x = "4"
y = int(x) # this function will convert the argument into an int 
print (type(y), y)

# convert string to a float
a = "4.54"
b = float(a)
print(type(b), b)

# convert string to bool - if string has any content, evaluates to true
c = bool(" hell")
print(type(c), c)

# convert integer to a string
d = str(12) 
e = "hello"
print(type(d), e + d)

# example
number = input("please enter your favorite number: ")
result = int(number) + 25
print("The result it", result)