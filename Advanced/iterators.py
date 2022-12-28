
#Iterators - have an "iterator" object with "next()" method

x = [1, 2, 3]
x_iter = x.__iter__()

# Under the hood of a for loop is code like this - we get an iterator object, call next method until StopIteration exception occurs, then break
while True:
    try:
        print(x_iter.__next__())
    except StopIteration:
        break

# Make any class iterable - include the "__iter__" method, define iterator class 
 
class Numbers:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def __iter__(self):
        return NumberIterator(self.num1, self.num2, self.num3)
    
    
# We must define our iterator class (how to iterate)  
class NumberIterator:
    def __init__(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three 
        self.current = 0
        
    def __next__(self):
        self.current += 1
        if self.current == 1:
            return self.one
        if self.current == 2:
            return self.two
        if self.current == 3:
            return self.three 
        else:
            raise StopIteration

nums = Numbers(1, 2, 3)
itr = iter(nums)
print(itr)
print(itr.__next__())

# For loop can work because we have __iter__() method that returns an iterator w/ the __next__() method 
for num in nums:
    print(num)
    
       
# Write a custom class that contains an iterator    
class Range:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.current_value = self.start
        return self 

    def __next__(self):
        if self.step > 0 and self.current_value >= self.stop:
            raise StopIteration
        elif self.step < 0 and self.current_value <= self.stop:
            raise StopIteration

        self.current_value += self.step 

        return self.current_value - self.step 

range_enumerator = Range(1, 30, 2)

for val in range_enumerator:
    print(val)
    

