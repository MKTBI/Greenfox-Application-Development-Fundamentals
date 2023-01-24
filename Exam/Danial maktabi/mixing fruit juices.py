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

# Test
juice = FruitJuice()
juice.add_ingredient("apple", 200)
juice.add_ingredient("banana", 200)
print(juice.get_concentration("apple")) # 0.5
juice.pour_out(200)
print(juice.get_concentration("apple")) # 0.5
juice.add_ingredient("apple", 200)
print(juice.get_concentration("apple")) # 0.75
print(juice.get_concentration("banana")) # 0.25
