class Plant():
    def __init__(self, name, water_amount=0):
        self.name = name
        self.water_amount = water_amount

    def needs_water(self):
        pass

    def absorb_water(self, water):
        pass

class Flower(Plant):
    def __init__(self, name, water_amount=0):
        super().__init__(name, water_amount)

    def needs_water(self):
        return self.water_amount < 5

    def absorb_water(self, water):
        self.water_amount += 0.75 * water

class Tree(Plant):
    def __init__(self, name, water_amount=0):
        super().__init__(name, water_amount)

    def needs_water(self):
        return self.water_amount < 10

    def absorb_water(self, water):
        self.water_amount += 0.4 * water

class Garden:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def water_plants(self, water):
        plants_needing_water = [plant for plant in self.plants if plant.needs_water()]
        for plant in plants_needing_water:
            plant.absorb_water(water / len(plants_needing_water))

    def show_garden(self):
        for plant in self.plants:
            if plant.needs_water():
                print(f"The {plant.name} needs water")
            else:
                print(f"The {plant.name} doesn't need water")

garden = Garden()

yellow_flower = Flower("yellow", 4)
blue_flower = Flower("blue", 4)
purple_tree = Tree("purple", 9)
orange_tree = Tree("orange", 9)

garden.add_plant(yellow_flower)
garden.add_plant(blue_flower)
garden.add_plant(purple_tree)
garden.add_plant(orange_tree)

garden.show_garden()
garden.water_plants(40)
garden.show_garden()
garden.water_plants(70)
garden.show_garden()
