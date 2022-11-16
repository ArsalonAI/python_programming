
# create a function inside class 
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


