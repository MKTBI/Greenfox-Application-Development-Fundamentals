'''Mixing fruit juices


We will be mixing some tasty-tasty fruit juice. We can add some components with certain amounts. Sometimes we pour out a bit of our juice. Then we want to find out, which concentrations our fruit juice has.

Example:

You take an empty jar for your juice
Whenever the jar is empty, the concentrations are always 0
Now you add 200 units of apple juice
And then you add 200 units of banana juice
Now the concentration of apple juice is 0.5 (50%)
Then you pour out 200 units
The concentration of apple juice is still 50%
Then you add 200 units of apple juice again
Now the concentration of apple juice is 0.75, while the concentration of banana juice is only 0.25 (300 units apple juice + 100 units banana juice)
Complete the functions in order to provide this functionality.'''

class FruitJuice:
    def __init__(self):
        self.components = {}
        self.total_volume = 0

    def add_component(self, name, volume):
        if name not in self.components:
            self.components[name] = 0
        self.components[name] += volume
        self.total_volume += volume

    def pour_out(self, volume):
        self.total_volume -= volume

    def get_concentration(self, name):
        if self.total_volume == 0:
            return 0
        else:
            return self.components[name] / self.total_volume

# Test usage
juice = FruitJuice()
juice.add_component("apple", 200)
juice.add_component("banana", 200)
print(juice.get_concentration("apple")) # should print 0.5
juice.pour_out(200)
print(juice.get_concentration("apple")) # should still print 0.5
juice.add_component("apple", 200)
print(juice.get_concentration("apple")) # should print 0.75
print(juice.get_concentration("banana")) # should print 0.25

class FruitJuice:
    def __init__(self):
        self.ingredients = {}

    def add_ingredient(self, ingredient, amount):
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += amount
        else:
            self.ingredients[ingredient] = amount

    def pour_out(self, amount):
        total_amount = sum(self.ingredients.values())
        if total_amount < amount:
            self.ingredients = {}
        else:
            for ingredient in self.ingredients:
                self.ingredients[ingredient] -= amount * self.ingredients[ingredient] / total_amount

    def get_concentration(self, ingredient):
        total_amount = sum(self.ingredients.values())
        if total_amount == 0:
            return 0
        else:
            return self.ingredients[ingredient] / total_amount
