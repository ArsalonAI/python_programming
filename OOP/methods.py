
# instance methods are functions defined inside a class that act on a specific instance (self) 
# all instance methods require self as first parameter 
# define all attributes in constructor, if not using yet, set to None vs. having "setter" method in class


class Person: 
    def __init__(self, name):
        self.name = name 
        self.age = None

    def say_hello(self):
        print(f"Hello, {self.name}")

    # don't set attributes this way, instanciate to none in constructor to avoid error
    def set_age (self, age):
        self.age = age
    

    def get_age(self):
        return self.age 


person1 = Person("arsalon")
person1.say_hello()
person1.set_age(25)
print(person1.get_age())


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

counter1 = Counter()


x = 0 
while x < 10: 
    counter1.increment()
    counter1.print_count()
    x+=1

counter1.toggle_lock()
counter1.increment()


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

        