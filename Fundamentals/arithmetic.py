# operator is a symbol like "+" or "-"
# expression is some operator (+/-) applied to some opperands (y, x) 

# operands 
a = 2 
b = 3

# expression
c = a + b

# addition/subtraction - can add floats and integers together, result is float if adding a float w/ integer
d = -1 
e = -2.0
f  = d - (-e)
print(f)

# exponential - x to the power of y -> x ** y 

x = 10 
y = 2 


exponential_result = x ** y 
print(exponential_result)

# integer division - converts float to an integer (rounds off to whole number) 
g = 10 
h = 3
integer_division = g // h 
print(integer_division)

# modulus operator - remainder after division of operands
i = 10
j = 3
modulus_division = i % j 
print(modulus_division)

''' 
Order of Operations
1. Brackets/Parathensis
2. Exponents
3. Multiplication and Division and Modulus 
4. Addition / Substraction 
'''

k = 11
l = 2
m = 4 
result = (k + l - m ) ** (k % m)
print(result)
# (11 + 2 - 4) ^ 3 = 729

n = 11
o = 2
p = 4
result_two = (5 + n - p) ** 2 - 7 / 2 // 4 
print (result_two)
# (5 + 11 - 4) ^ (2 - (7/2) // 4)
# 12 ^ (2 - (3.5 / 4)) 
# result = 12 ^ 0 = 1 