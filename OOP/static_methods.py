

class Student: 
    grade_bump = 2.0
    
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades
      
    #instance method - takes 'self' can access grades directly from instance  
    def average (self):
        return sum(self.grades / len(self.grades))
    
    @classmethod
    def average_from_grades_plus_bump(cls, grades):
        #can use static method inside class method 
        average = cls.average_from_grades(grades)
        #takes the min value either bumped avg or 100 (doesn't allow to go over 100%)
        return min(average + cls.grade_bump, 100)
    
    @staticmethod
    def average_from_grades(grades):
        return sum(grades)/len(grades)
    
    
s1 = Student("Arsalon", [80, 99, 98, 97, 40])
s2 = Student("Arsalon's Friend", [99, 98, 78, 99, 99, 100])

# must pass the instance attribute to the method becuz it doesn't have access directly
average = s1.average_from_grades(s1.grades) 
print(average)

average_2 = Student.average_from_grades(s2.grades)
print(average_2)


class Physics: 
    
    @staticmethod
    def calculate_net_force(mass, acceleration):
        if mass < 0 or acceleration < 0: 
            return 0.0 
        return mass * acceleration
            
        
    @staticmethod
    def calculate_acceleration(mass, net_force):
        if net_force <= 0 or mass <= 0: 
            return 0.0
        return net_force / mass 
            
        
    @staticmethod
    def calculate_mass(net_force, acceleration): 
        if net_force <= 0 or acceleration <= 0:
            return 0.0
        return round(net_force / acceleration)
    
    
print(Physics.calculate_net_force(10, 2.8))
print(Physics.calculate_acceleration(10, 28))
print(Physics.calculate_mass(100, 2.8))
        

