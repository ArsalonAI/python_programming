
class Person:
    def __init__(self, name, age, gender):
        print("this is a constructor, called each time we instantiate this class")
        self.name = name
        self.age = age
        self.gender = gender
    

class Fruit: 
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories


class ContactInformation:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.country = None



# instantiating our classes into specific objects 

john = Person("John", 25, "Male")
print(john.name,  john.age,  john.gender)


apple = Fruit("apple", 200)
print(apple.calories)

person1 = ContactInformation("Jason", "Liu", "JasLiu@gmail.com", 343232344)
person2 = ContactInformation("Peter", "Rabit", "Peterrabit@gmail.com", 3983899232)
print(person1.first_name)