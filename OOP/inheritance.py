
# Base Class (super class)
class Person:
    def __init__(self, first_name, last_name):
         self.first_name = first_name
         self.last_name = last_name
         
    def say_hello(self):
        print(f"Hi my name is {self.first_name} {self.last_name}")

# Employee (child class, derived class) - inherits from Person (parent class, super class)
class Employee (Person):
    #over-ride constructor of super class 
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary
        
    def test(self):
        print("test")
        
    #polymorphism - over-ride super class method definition    
    def say_hello(self):
        print("-----")
        super().say_hello() #access base class method (use it here)
        print(f"and my annual salary is {self.salary}")
        print("-----")
        
        
e = Employee("Arsalon", "Amini", 101000)
e.say_hello()

   