
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

    salary = property(get_salary, set_salary)

    # property func - legacy way 
    # allow us to use dot notation syntax vs. set_salary/get_salary when working with attribute outside of class 
    # using dot notation calls the get_salary and set_salary (under the hood)
    

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


#using getter/setter functions 

class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    def get_balance(self):
        return round(self._balance) 
    
    def set_balance(self, balance):
        if type(balance) not in [int, float]:
            raise TypeError("Should be a number")
        elif balance < 0:
            raise ValueError("Hey, invalid salary")
        elif balance >= 100000:
            raise ValueError("Hey, cannot exceed 100000")

        self._balance = balance 

# using properties 
class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    @property
    def balance(self):
        return round (self._balance)

    @balance.setter
    def balance(self, balance):
        if type(balance) not in [int, float]:
            return
        elif balance < 0:
            return
        elif balance >= 100000:
            return

        self._balance = balance 