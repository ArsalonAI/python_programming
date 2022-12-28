# Special type of iterator - newer syntax 
# yield keyword - pause execution of func, maintains internal state, next time next() method called, continues

def gen():
    yield 1
    yield 2
    yield 3
    
print(gen())

itr = gen()
print(next(itr)) # can call next method on iterator 

# For loop calls the next() method under hood 
for el in itr:
    print('looping', el)
    
# Traditional approach - inefficient to store infinity in a list - We just need previous two numbers to cal fib sequence - Generator can help 
fib_numbers = [1, 1]

for i in range(2, 10):
    last = fib_numbers[i - 1]
    second_last = fib_numbers[i - 2]
    num = last + second_last
    fib_numbers.append(num)
    
print(fib_numbers)

# Use generator 
def fib(n):
    last = 1
    second_last = 1
    current = 3
    
    while current <= n:
        num = last + second_last
        yield num # create num, return it (yield it), continues execution
        
        second_last = num
        last = num
        current += 1
        
for val in fib(10):
    print(val)
    
    
        
        
