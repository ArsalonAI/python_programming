
#Iterators - have an "iterator" object with "next()" method

x = [1, 2, 3]
x_iter = x.__iter__()

# Under the hood of a for loop is code like this - we get an iterator object, call next method until StopIteration exception occurs, then break
while True:
    try:
        print(x_iter.__next__())
    except StopIteration:
        break
    


