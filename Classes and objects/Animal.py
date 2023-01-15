class Animal:
    def __init__(self):
        self.hunger = 50
        self.thirst = 50
    
    def eat(self):
        self.hunger -= 1
    
    def drink(self):
        self.thirst -= 1
        
    def play(self):
        self.hunger += 1
        self.thirst += 1

animal1 = Animal()
animal2 = Animal()


print(animal1.hunger) 
print(animal2.thirst) 


animal1.eat()


print(animal1.hunger) 


animal2.drink()


print(animal2.thirst) 


animal2.play()


print(animal2.hunger) 
print(animal2.thirst) 
