
# Base Class (super class)
class Person:
    def __init__(self, first_name, last_name):
         self.first_name = first_name
         self.last_name = last_name
         
    def say_hello(self):
        print(f"Hi my name is {self.first_name} {self.last_name}")

# Employee - child class, derived class, inherits from Person class
class Employee (Person):
    #over-ride constructor of super class 
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary
        
    #polymorphism - over-ride super class method definition    
    def say_hello(self):
        super().say_hello() #access base class method (use it here)
        print(f"and my annual salary is {self.salary}")
        
         
# Employee - parent class, super class .super() on the employee class
# Managager - child class, derived class
class Manager(Employee):
    def __init__(self, first_name, last_name, salary, department):
        super().__init__(first_name, last_name, salary)
        self.department = department
        
    def say_hello(self):
        super().say_hello()
        print(f" and my department is {self.department}")
        
# Person - super class (parent class)
# Owner - derived class (child class)
class Owner(Person):
    def __init__(self, first_name, last_name, net_worth):
        super().__init__(first_name, last_name)
        self.net_worth = net_worth
    
    def say_hello(self):
        super().say_hello()
        print(f"My net worth is {self.net_worth}")
 

e = Employee("Arsalon", "Employee", 50000)
e.say_hello()
 
m = Manager("Arsalon", "Manager", 101000, "IoT")
m.say_hello()

o = Owner("Arsalon", "Owner", "100000000")   
o.say_hello()


#multiple inheritance
class A:
    pass
    
class B:
    def __init__(self):
        print("B")
    
# Both A, B - parent, super classes however the order of init () called depends on first listed 
# method resolution order - start in main class, look at first super class, second superclass 
# super () - references all classes inherited from but start looking from first listed, if not present, go to next class
class C(A, B):
    def __init__(self):
        super().__init__()
        print("C")
    
c = C()


class Animal:
    def __init__(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height 
    
    
class Mammal(Animal):
    def __init__(self, age, weight, height, sex):
        super().__init__(age, weight, height)
        self.sex = sex 
    
    
class Reptile(Animal): 
    def __init__(self, age, weight, height, legs=4):
        super().__init__(age, weight, height)
        self.legs = legs 
    
class Monkey(Mammal):
    fingers = 5
    
    def __init__(self, age, weight, height, sex, color, fingers):
        super().__init__(age, weight, height, sex)
        self.color = color 
     

class Lizard(Reptile):
    tail = True 
    def __init__(self, age, weight, height, legs, color):
        super().__init__(age, weight, height, legs)
        self.color = color
    