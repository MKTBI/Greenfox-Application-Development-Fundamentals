class Station:
    def __init__(self):
        self.gas_amount = 100

    def refill(self, car):
        self.gas_amount -= car.capacity
        car.gas_amount = car.capacity

class Car:
    def __init__(self):
        self.gas_amount = 0
        self.capacity = 100

station = Station()
car = Car()
print("Initial gas amount of car:", car.gas_amount)
station.refill(car)
print("Gas amount of car after refilling:", car.gas_amount)
