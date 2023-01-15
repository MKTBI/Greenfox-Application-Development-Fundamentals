class Car:
   def __init__(self, consumption, fuel = 0):
       self.consumption = consumption
       self.fuel = fuel
 
   def ride(self, km):
       required_fuel = km * (self.consumption / 100)
       kms_left = km - (self.fuel / required_fuel) * km
       self.fuel = max(self.fuel - required_fuel, 0)
       return kms_left
 
class PetrolCar(Car):
   def __init__(self, consumption, fuel):
       super().__init__(consumption, fuel)
 
class PetrolElectricHybridCar(Car):
   def __init__(self, consumption, fuel, kms_with_electric_engine):
       super().__init__(consumption, fuel)
       self.kms_with_electric_engine = kms_with_electric_engine
 
   def ride(self, km):
       kms_left_with_petrol = super().ride(km)
       kms_left = max(kms_left_with_petrol - self.kms_with_electric_engine, 0)
       return kms_left
 
petrol_car = PetrolCar(10, 50)
hybrid_car = PetrolElectricHybridCar(10, 50, 100)
 
print(petrol_car.ride(550))
print(hybrid_car.ride(550))
