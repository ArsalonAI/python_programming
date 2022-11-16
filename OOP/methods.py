
# create a function inside class 
# all methods require self as first parameter 


class Person: 
    def __init__(self, name):
        self.name = name 

    def say_hello(self):
        print(f"Hello, {self.name}")
    

person1 = Person("arsalon")
person1.say_hello()


