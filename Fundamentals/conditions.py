
# Comparision operator  
condition_one = 2 == 3 #expect False
print (condition_one)

# NOT equal 
x = 3.1
y = 3
cond2 = x != y # expect True
print(cond2)

# Greater Than
t = 10
z = 56
t_z = z > t # expect True
print (t_z) 

# Less Than 
a = 10 
b = 9 
a_b = a < (b + 5) # expect True 
print (a_b)

# Less Than or Equal
e = 10
f = 15
e_f = e <= f # expect True
print (e_f) 

# Greater than or equal 
c = 10
d = 15
cd = c >= d # expect False 
print (cd) 

# Compare 'int' and 'str' together
str_condition_one = 'hello' == 6
print ('result of comparing an `int` and a `string` ', str_condition_one) #Expect False 

# Compare strings - equivalence
str1 = "hello"
str2 = "hello"

str_condition = str1 == str2 # expect True
print ('Result of comparing two strings,' , str_condition)

# Compare Strings for Less Than / Greater Than
# Converst to ASCII character (an int value) then compares int values
# ord() fn gives the unicode value (int value representing ASCII code) when a char is passed
# chr() fn returns the letter when int representing the ASCII code is passed as an arg

print('the ASCII for letter `A` is', ord("A")) 
print('the ASCII for letter `B` is', ord("B"))
print('the ASCII for letter `C` is', ord("C"))
print('the ASCII for letter `Z` is', ord("Z"))
print('the ASCII for letter `a` is', ord("a")) 
print('the ASCII for letter `z` is', ord("z")) 
print("the letter for ASCI code 65 is", chr(65)) 

char_one = "A"
char_two = "B"
str_comparision = char_one < char_two
print('result of comparing two characters is, ' , str_comparision)
