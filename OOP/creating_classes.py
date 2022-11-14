# creating a new class - use PascalCase
# Car - a new datatype in program (attributes + behavior)
# stored in the main file of program()

class Person:
    def __init__(self, name, age, gender):
        print("this is a constructor, called each time we instantiate this class")
        self.name = name
        self.age = age
        self.gender = gender
    
John = Person("John", 25, "Male")

print(John.name,  John.age,  John.gender)





