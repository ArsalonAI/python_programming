# conditions

# equal to comparision 
cond = 2 == 3 # assign value of condit to condition
print (cond)

# not equal to 
x = 3.1
y = 3
cond2 = x != y # expect value to be False
print(cond2)

# greater than 

t = 10
z = 56
tz = z > t # expect True
print (tz) 


# less than 
a = 10 
b = 9 

cond3 = a < b + 5 # expect True - can add to the expression with more operands 
print (cond3)

# less than or equal

e = 10
f = 15
ef = e <= f # expect True
print (ef) 



# greater than or equal 
c = 10
d = 15
cd = c >= d # expect False 
print (cd) 

# compare int and str together, can do equivalents but not > < 
condstr = 'hello' == 6
print ('the answer is ', condstr)

# compare strings
str1 = "hello"
str2 = "Hello"

str_condition = str1 == str2 # expect false
print (str_condition)

# comparing strings > less or greater than (compares ASCII characters)
print (ord("A")) # gives the unicode value for the letter (ASCII code)
print(ord("B"))
print("the letter for ASCI code 65 is", chr(65)) #chr() function returns the letter given the ASCII code as an arg

str3 = "A"
str4 = "B"
str_condition2 = str3 > str4 
print(str_condition2)

print(ord("m"))
print(ord("l"))
print(ord("z"))
