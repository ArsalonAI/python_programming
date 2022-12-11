# Conditionals - conditionally run a part of your program 
# Syntax: if, elif 

number = float(input("Enter a number: "))

if number > 0 and number % 2 == 0:  # checks if number is even
    print("this number is even")
elif number > 0 and number % 2 > 0: # checks if number is odd
    print("this number is odd")


# Nested if statement
number2 = float(input("enter a number: "))

if number2 > 0 and number2 % 2 > 0: 
    print("This is an odd number ")
    
    number3 = float (input("Enter another number"))

    if number3 > 0 and number3 % 2 == 0: 
        print("this is an even number: ")
    else:
        print("This is another odd number")


# else - one line conditional statement 
# assign a variable based on a condition 
x = 5 
result = "OK" if x > 5 else "Not Ok"
print(result)

y = 6
print("Hello") if y == 6 else print("not good")







