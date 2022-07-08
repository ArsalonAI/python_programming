
import enum

# iterate a list 

for i in range (20):
    print(i)

# using a start and stop range (arg1 = start, arg2 = stop)
for x in range (5, 20):
    print (x)

# adding a step - (start, stop, step) - how many times i is incremented on each loop
# expect y to print 3, 6, 8, 12, 15 ... 
for y in range (3, 27, 3):
    print (y)


# iterate by index - set the stop to the length of the list 
lst = [1, 2, 3, 4, 5, True, False, 1, 4]
for idx in range(len(lst)):
    print(lst[idx])

# iterate by item - loop directly through list without index (no index access)
for element in lst: 
    print(element)

# iterate by both using enumerate - access to index + element (using enumerate keyword)
for i, element in enumerate(lst):
    print(i, element)


# iterate a tuple 

# using range function
tup = (2, 3, 4, "hello world", "yes, I'm cool", True)
for i in range(len(tup)):
    element = tup[i]
    print(element)

# using element
for element in tup:
    print(element)

# using enumerate keyword
for i, element in enumerate(tup):
    print(i, element)


# iterate a string 

s = "this is my string"
for i in range(len(s)):
    print(s[i])

# iterate the string with a step of 2
for i in range(0, len(s), 2): 
    print(s[i])

# break keyword - stops the loop 

lst_2 = [1, 2, 3, 4, 5, 6, 7]
for num in lst_2:
    if num == 4:
        break

    print(num)

print("done")   

# continue keyword - jumps to next loop

lst_3 = [10, 11, 12, 13, 14, 15]
for num in lst_3:
    if num == 11:
        continue
    print(num)

print("done")


# nested for loops

# expect 100 values to be printed in O(n^2) time 
# nested look runs
for i in range (10):
    for j in range(10):
        print(j)


# loop a nested list 
nested_lst = [[1,2], [3,4], [5, 6], [7,8]]

for i in range (len(nested_lst)):
    element_lst = nested_lst[i]
    for j in range(len(element_lst)):
        print(element_lst[j])


# find index of a letter in string 
hello_str = "hello world"

for i, character in enumerate(hello_str):
    if character == "w":
        print("the letter is at index", i)


# ask user for input n number of times and put numbers into a list
numbers = [] # if this is defined inside the for loop, it's re-defined on ever iteration 

for i in range(10):
    num = input("Enter a number: ")
    numbers.append(int(num))

print(numbers)

 # for else keyword - check if an element exists in a tuple

words = ("hello", "this", "is", "my", "string")
target = "string"

# not good way 
for word in words: 
    if word == target:
        print("I found the target word")
    else:
        print("I didn't find the word")

# a better way - 
found = False

for word in words: 
    if word == target:
        print("I found the target")
        found = True 
        break

if not found: 
    print("I didn't find the word")

# for - else - else block is evaluated if not break from look 

for word in words: 
    if word == target:
        print("I found the target")
        break
else:
    print("I didn't find the word")