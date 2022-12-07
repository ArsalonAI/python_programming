

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
