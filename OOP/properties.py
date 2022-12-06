# properties 
# allow us to enforce specific behavior when accessing / modifying attributes (get / set)

# private attribute
# data (attribute) that can only be modified from within the class (using a method)
# self._salary - using an underscore denotes private (however, it's not actually enforced in the syntax) just a convention
# use a setter method to set salary 

class Employee:
    def __init__(self, name):
        self.name = name
        self._salary = 0

    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Hey, invalid salary, must be positive")
        self._salary = salary

    def get_salary(self):
        return round(self._salary)

    # property func - legacy way 
    # allow us to use dot notation syntax vs. set_salary/get_salary when working with attribute outside of class 
    # using dot notation calls the get_salary and set_salary (under the hood)
    salary = property(get_salary, set_salary)


e = Employee("Arsalon")
e.salary = 101000 
print(e.name, e.salary)


class Person:
    def __init__(self, name):
        self.name = name
        self._networth = 0
        print("constructor ran")
    
    # use property decorator (new way) as getter 
    @property
    def networth(self):
        print("getter ran")
        return round (self._networth)

    # use name of property w/ setter    
    @networth.setter 
    def networth(self, networth):
        print("setter ran")
        if networth < 0:
            raise ValueError("Hey, networth should be positive")
        self._networth = networth


p = Person ("Arsalon")
p.networth = 1000000
print(p.name, p.networth)


