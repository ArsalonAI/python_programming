#take user input 

#integer will be inputted as a string, need to convert it to integer later
value = input("Number: ")
print(value)
print(type(value))


#no matter what is typed in, it's a string
name = input("Enter your name :")
print("Hello,", name)

#use string concatination inside input function for multiple strings
age = input("hello " + name + " what is your age: ")
print(age, type(age))
