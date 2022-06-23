# indexing string
from operator import is_


str = "Hello Sir"
print(str[0]) # H
print(str[-1]) # gives element at the last index "r"

# get count of an element in a string
count = str.count('l')
print(count)

# change to uppercase
str_uppercase = str.upper()
print(str_uppercase)

# change to lowercase
str_lowercase = str.lower()
print(str_lowercase)

# validate user input by converting to all lowercase 


user_input = input("What is my name? ")

if user_input.lower() == "arsalon":
    print("correct")
else: 
    print("nope, not correct")



# Capitalize first letter
str2 = "arsalon"
print(str2.capitalize())

# IN operator - see if the string contains a specific character
is_present = "a" in str2
print(is_present)

# check if a string contains integer digits - False if has characters or floats 

str3 = "2009"
is_integer = str3.isdigit()
print(is_integer)

# convert user input into integer 

num = input("Enter a number: ")

if num.isdigit():
    print("It's a number")
    num = int(num) # cast to integer
    print(num + 10)
else: 
    print("it's not a digit")


# split method - split string into individual elements based on deliminator, deliminator is removed (default it's a space)

s = "Hello I am Arsalon"
words = s.split()

print(words)

# comma is a deliminer 
s2 = "This,is,a,string"
words2 = s2.split(",")
print(words2)

# replace - replace method takes two args - arg1 character in current string to replace, arg2 with new character

s3 = "Hello,this,is,an,example"
new_str3 = s3.replace(",", "|") 
print(new_str3)


# f string - python 3.6 feature (new) - embed variables inside strings (complex output that contains variables)

name = input("Enter your name: ")
output = f" Hello, {name}!, {name}, {10 + 5} Thanks! " 
print(output)
    

# string multiplication - multiple strings - repeats string by multiplier

s = "hello"
s3 = s * 3
print(s3)

# multi line strings 

multi_line_string = """
Hello
this is a multi
line string
not a comment
"""

print(multi_line_string)

# JOIN - combine list into a long string

str_list = ["A", "R", "S", "A", "L", "o", "n"]

combined_str = "-".join(str_list)
print(combined_str)


# excercise - remember strings are imutable, each operation must create a new string
num = input("Enter an integer: ")

if num.isdigit():
    name = input("What is your name? ")
    upper_name = name.upper()
    print(f"Hello, {upper_name}")
else: 
    capital_input = num.capitalize()
    print(capital_input)

# excercise - 
word_one = input("Enter a word: ")
word_two = input("Enter another word: ")


if word_one in word_two:
    print("The first word is contained in the second one")
else: 
    print("The first word isn't contained in the second one")