

class Car:
    number_of_wheels = 4
    number_of_seats = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @classmethod 
    def update_number_of_seats(cls, number_of_seats):
        cls.number_of_seats = number_of_seats


print(Car.number_of_seats)
Car.update_number_of_seats(2)
print(Car.number_of_seats)


class Circle: 
    pi = 3.14
    
    @classmethod
    def area (cls, radius):
        return cls.pi * (radius ** 2)
    
    @classmethod
    def circumference (cls, radius):
        return 2 * cls.pi * radius

    @classmethod
    def get_area_and_circumference(cls, radius):
        return cls.area(radius), cls.circumference(radius)
    
print(Circle.get_area_and_circumference(4))



class Person:
    population = 0
  
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.population = 1
        Person.population += 1
      
    @classmethod
    def reduce_population(cls, reduction):
        cls.population -= reduction
    

p1 = Person("RC", 100)
p2 = Person("RC's Friend", 54)

x = Person.population
print(x)



class Employee:
    number_of_employees = 0
    average_age = 0
    average_salary = 0
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary 
        
        
        total_age = Employee.average_age * Employee.number_of_employees
        total_salary = Employee.average_salary * Employee.number_of_employees
        Employee.average_age = (total_age + age) / (Employee.number_of_employees + 1)
        Employee.average_salary = (total_salary + salary) / (Employee.number_of_employees + 1)
        Employee.number_of_employees += 1
 
 
class Temperature:
    min_temperature = 0
    max_temperature = 1000
     
    def __init__(self, kelvin):
        if kelvin > self.max_temperature or kelvin < self.min_temperature:
            raise Exception("Invalid temperature")
        self.kelvin = kelvin 
        
    @classmethod 
    def update_min_temperature(cls, kelvin):
        if kelvin > cls.max_temperature:
            raise Exception("Invalid Temp")
        
        cls.min_temperature = kelvin
        
        
    @classmethod
    def update_max_temperature(cls, kelvin):
        if kelvin < cls.min_temperature:
            raise Exception("Invalid temperature.")

        cls.max_temperature = kelvin