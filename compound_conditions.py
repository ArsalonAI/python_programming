# logical operators - combine or chain conditions together

a = 2
b = 4

# and - only evaluates to true if both left + right are True 
and_condition = a < b and b > 0 and True
print(and_condition)

# or - checks if either side has true, if both left/right are False, evaluates to False
c = 10
d = 5

or_condition = c < 0 or c > d or d == 5
print(or_condition)

# not - negates or swaps value of condition
e = 10
f = 3
not_condition = not(e > f) # e > f is True, not operator negates to False 
print(not_condition)

# order of operations -
# 1) Not 
# 2) And 
# 3) Or 
compound_one = True or False and not True or False 
print(compound_one)

compound_two = not(True or False) and not False or 2 < 3 or True
print(compound_two)

# False and True or 2 < 3 or True
# False 