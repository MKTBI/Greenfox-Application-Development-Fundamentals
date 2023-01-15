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

class Farm:
    def __init__(self, limit):
        self.listOfAnimals = []
        self.limit = limit
        
    def breed(self):
        if len(self.listOfAnimals) < self.limit:
            self.listOfAnimals.append(Animal())
            
    def sell(self):
        if len(self.listOfAnimals) > 0:
            least_hungry = self.listOfAnimals[0]
            for animal in self.listOfAnimals:
                if animal.hunger < least_hungry.hunger:
                    least_hungry = animal
            self.listOfAnimals.remove(least_hungry)


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

print("\n")

farm = Farm(10)

farm.breed()
farm.breed()
farm.breed()

farm.sell()

print(len(farm.listOfAnimals)) 
