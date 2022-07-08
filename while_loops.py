
# Use case - do not know how many times you want to loop 
x = 0
while x < 5: 
    print(x)
    x += 1

# ask user to enter a value, if not an integer, keep asking
num = input("Enter a number: ")

while not num.isdigit():
    num = input("Enter a number: ")

# using "True" and a break statment to enter a while loop

while True:
    num = input("Enter a number: ")
    if num.isdigit():
        break; 


# loop through list and stop when sum of items in list exceed n
lst = [2, 3, 3, 4, 5]

result = 0
idx = 0

while result < 9:
    num = lst[idx]
    result += num 

# loop through list and stop when sum of items in list exceed n
lst = [2, 3, 3, 4, 5]

result = 0
idx = 0

while result < 9:
    num = lst[idx]
    result += num 
    idx += 1
    print('next item in list is', num)
    print('the current sum is', result)

# ensure while loop doesn't go out of bounds
lst = [2, 3, 3, -2, -2, -2]

result_two = 0
idx = 0

while result_two < 9 and idx < len(lst):
    num = lst[idx]
    result_two += num 
    idx += 1
    print('next item in list is', num)
    print('the current sum is', result_two)


# while-else
lst = [2, 3, 3, -2, -2, -2]
idx = 0

while idx < len(lst):
    if lst[idx] == -12:
        print ("found the target")
        break
    idx +=1
else:
    print("didn't find it")
    