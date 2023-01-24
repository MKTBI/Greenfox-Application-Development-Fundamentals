import random

class Pirate:
    def __init__(self):
        self.intoxication = 0
        self.alive = True
        self.parrot = None
        
    def drink_some_rum(self):
        if self.alive:
            self.intoxication += 1
    
    def hows_it_going_mate(self):
        if self.intoxication < 4:
            return "Pour me anudder!"
        else:
            self.intoxication = 0
            return "Arghh, I'ma Pirate. How d'ya d'ink its goin?"
            
    def brawl(self, pirate):
        if self.alive and pirate.alive:
            outcome = random.randint(1, 3)
            if outcome == 1:
                self.die()
            elif outcome == 2:
                pirate.die()
            else:
                self.intoxication = 0
                pirate.intoxication = 0
                
    def die(self):
        self.alive = False
        
    def __str__(self):
        if self.alive:
            return "Pirate, Intoxication level: {}".format(self.intoxication)
        else:
            return "Pirate is dead"
            
class Ship:
    def __init__(self):
        self.crew = []
        self.captain = None
        
    def fill_ship(self):
        self.captain = Pirate()
        crew_size = random.randint(1, 113)
        for i in range(crew_size):
            self.crew.append(Pirate())
            
    def battle(self, other_ship):
        if self.calculate_score() > other_ship.calculate_score():
            self.party()
            other_ship.lose()
            return True
        else:
            self.lose()
            other_ship.party()
            return False
            
    def calculate_score(self):
        alive_count = sum(1 for pirate in self.crew if pirate.alive)
        return alive_count - self.captain.intoxication
        
    def party(self):
        for pirate in self.crew:
            pirate.drink_some_rum()
        self.captain.drink_some_rum()
        
    def lose(self):
        
        deaths = random.randint(1, len(self.crew))
        for i in range(deaths):
            pirate = random.choice(self.crew)
        if pirate.alive:
            pirate.die()
            
    def __str__(self):
        alive_count = sum(1 for pirate in self.crew if pirate.alive)
        return "Captain: {}\nAlive pirates: {}".format(self.captain, alive_count)
        
        
class Armada:
    def __init__(self):
        self.ships = []
        
    def fill_armada(self, count):
        for i in range(count):
            ship = Ship()
            ship.fill_ship()
            self.ships.append(ship)
            
    def war(self, other_armada):
        while len(self.ships) > 0 and len(other_armada.ships) > 0:
            my_ship = self.ships.pop(0)
            their_ship = other_armada.ships.pop(0)
            if not my_ship.battle(their_ship):
                self.ships.append(my_ship)
                
        if len(self.ships) > 0:
            return True
        else:
            return False
