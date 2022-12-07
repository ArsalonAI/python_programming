


class Person: 
    def __init__(self, name):
        self.name = name 
        self.age = None

    def say_hello(self):
        print(f"Hello, {self.name}")

    # setter - don't define new attribute in method like this (instanciate to None in constructor to avoid errors)
    def set_age (self, age):
        self.age = age

    def get_age(self):
        return self.age 


class Counter:
    def __init__(self):
        self.count = 0
        self.locked = False

    def toggle_lock(self):
        self.locked = not self.locked 

    def increment(self):
        if self.locked:
            raise Exception("Counter is locked")
        self.count += 1
    
    def decriment(self):
        if self.locked:
            raise Exception("Counter is locked")
        self.count -= 1

    def print_count(self):
        print(f"The current count is {self.count}")


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    

    def change_position(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y

    def get_area(self):
        return self.width * self.height


class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add (self, name):
        self.members += name 
    
    def delete (self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception ("Member not in group.")

    def get_members(self):
        return sorted(self.members)

    def merge(self, group):
        combined_members = self.members + group.members
        new_group = Group("Name", combined_members)
        return new_group

