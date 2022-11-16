# creating a new class - use PascalCase
# Car - a new datatype in program (attributes + behavior) stored in the main file of program()
# attributes are data associated with an instance of a class
# __init__ is constructor -> auto called upon instantiation, instance attributes set in constructor using self keyword


class Person:
    def __init__(self, name, age, gender):
        print("this is a constructor, called each time we instantiate this class")
        self.name = name
        self.age = age
        self.gender = gender
    
john = Person("John", 25, "Male")

print(john.name,  john.age,  john.gender)





class Fruit: 
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

apple = Fruit("apple", 200)
print(apple.calories)
