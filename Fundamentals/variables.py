# start variables with letter 
count = 0 
message = "hello"

# snake case - python convention
snake_color = 'red'
snake_eye_color = 'blue'

#variables by Pep conventions are lowercase 
message_two = "how are you today?"  
print(message_two)

# classes start with capitals
class Handsome:
    is_handsome = True
    def __init__(self, count):
        self.count = count 

# Code is executed top to bottom  (Order of Execution)   
x = 3
print(x)
y = 'hello'
print(y)
num = y # copies value of y into 'num'
print(num)
y = x # re-assigns value of y to 'x' which is '3'
print(y)
x = 4
print(x)

