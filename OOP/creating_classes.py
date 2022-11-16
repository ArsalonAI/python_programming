# purpose of creating classes - encapsulate common behavior between instances (access to behavior in program)
# grouping related behavior together in a class
# creating a new class - use PascalCase
# Car - a new datatype in program (attributes + behavior) stored in the main file of program()
# attributes are data associated with an instance of a class
# __init__ is constructor -> auto called upon instantiation, instance attributes set in constructor using self keyword
# PEP-8 (python style guide) says use PascalCase when naming classes in python programs


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


# excercise below - create the following contact information class 

class ContactInformation:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.country = None

person1 = ContactInformation("Jason", "Liu", "JasLiu@gmail.com", 343232344)
person2 = ContactInformation("Peter", "Rabit", "Peterrabit@gmail.com", 3983899232)