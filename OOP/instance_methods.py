# Instances Methods
# functions defined inside a class, that act on instances of the class
# can access attributes associated with specific instance
# ex. constructor def __init__(self)
# always need "self" (hidden parameter) as first parameter in instance method func definition


class Person: 
    def __init__(self, name):
        self.name = name 
        self.age = None

    def say_hello(self):
        print(f"Hello, {self.name}")

    # setter - don't define new attribute in method like this (instanciate to None in constructor to avoid errors)
    def set_age (self, age):
        self.age = age

    def get_age(self):
        return self.age 


class Counter:
    def __init__(self):
        self.count = 0
        self.locked = False

    def toggle_lock(self):
        self.locked = not self.locked 

    def increment(self):
        if self.locked:
            raise Exception("Counter is locked")
        self.count += 1
    
    def decriment(self):
        if self.locked:
            raise Exception("Counter is locked")
        self.count -= 1

    def print_count(self):
        print(f"The current count is {self.count}")


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    

    def change_position(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y

    def get_area(self):
        return self.width * self.height
