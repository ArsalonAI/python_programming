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
# 1) parenthesis 
# 1) conditional / comparision operators (greater than / less than)
# 1) Not 
# 2) And 
# 3) Or 
compound_one = True or False and not True or False 
print(compound_one)

compound_two = not(True or False) and not False or 2 < 3 or True
print(compound_two)

# False and True or True or True
# False or True or True
# True 


#What is DeMorgan's Law? 
# swap the sign in the parenthesis and apply the not to both operands 
# ex. not (x and y) == not (x) or not(y)
# ex. not (x or y) == not (x) and not (y)

# Ex. not (w and z or (not w))
# not ((w and z) or (not w)) ->  Apply DeMorgan's law 
# (not (w and z)) and (not (not (w))) -> two nots cancel out
# (not (w and z)) and (w) -> Apply DeMorgan's law x 2
# not (w) or not (z) and (w)

# truth tables - what values of w and z make it true

'''
1) create one column for every variable
2) column one go down adding F, T, F, T
3) second column alternative every 2x (2^3)

W Z 
...
F F -> True or True and False -> True
T F -> False or True and True -> True 
F T -> True or False and False -> True 
T T -> False or False and True -> False 
...
'''

# excercises 
# (False and True) or True 
# False or True -> True 

# not ((True and True) or True)
# not (True) and not (True)
# False 

# not (x and not (y and z))
# not (x) or not (not (y and z))

# not (x and not (y and z))
# not (x and (not(y) or not (z))) 
# not (x) or not(not(y) or not (z))
# not (x) or not(not(y)) and not(not(z))
# not (x) or (y) and (z)
#



# example - x, y, z are always True or False, respectively. There are 8 combinations in the truth table. 
# construct a truth table and determine how many possibilities lead to True for the below expression

# x and y or z

'''
X Y Z 
F F F -> F and F or F = False 
T F F -> T and F or F = False
F T F -> F and T or F = False
T T F -> T and T or F = True
F F T -> F and F or T = True
T F T -> T and F or T = True 
F T T -> F and T or T = True 
T T T -> T and T or T = True
'''

# the answer is 5 combinations lead to 'True' 