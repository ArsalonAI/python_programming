# name abstract class with abstract prefix 
# abstract method - must be implemented by all classes inheriting from abstract classes 

import random


class AbstractGame: 
    
    def start (self):
        while True:
            start = input("Would you like to play?")
            if start.lower() == "yes":
                break 
        self.play()
    
    def end(self):
        print("The game has ended")
        self.reset()

    def play(self):
        raise NotImplementedError("You must provide an implementation for play()")
    
    def reset(self):
        raise NotImplementedError("You must provide an implementation for reset()")
    
class RandomGuesser(AbstractGame):
    def __init__(self, rounds):
        self.rounds = rounds
        self.round = 0
    
    #over rides parent method (throws an error) with this play method implementation (valid implementation)
    def play(self):
        while self.round < self.rounds:
            self.round +=1 
            
            print(f"Welcome to round {self.round}. Let's begin")
            random_num = random.randint(0,10)
            while True:
                guess = input ("Enter a number between 1-10: ")
                if int(guess) == random_num:
                    print("You got it")
                    break
                
        self.end()
      
    def reset(self, rounds): 
        self.round = 0
        
    
game = RandomGuesser(2)
game.start()


class AbstractAnimal: 
    def sleep(self):
        print('ZzzZzz')
        
    def animal_sound(self):
        raise NotImplementedError("You must provide an implementation for animal sound")
    
    def wake_up(self):
        self.animal_sound()
        print('I am awake!')

class Lion(AbstractAnimal):
    def animal_sound(self):
        print('Roar!')
        
lion = Lion()
lion.animal_sound()
