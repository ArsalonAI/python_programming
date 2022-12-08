

class Student: 
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades
        
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

