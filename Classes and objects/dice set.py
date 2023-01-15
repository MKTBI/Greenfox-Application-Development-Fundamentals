import random

class DiceSet(object):

    def __init__(self):
        self.dices = [0, 0, 0, 0, 0, 0]

    def roll(self):
        for i in range(len(self.dices)):
            self.dices[i] = random.randint(1, 6)
        return self.dices

    def get_current(self, index = None):
        if index != None:
            return self.dices[index]
        else:
            return self.dices

    def reroll(self, index = None):
        if index != None:
            self.dices[index] = random.randint(1, 6)
        else:
            self.roll()

    def roll_till_all_six(self):
        while not all(x == 6 for x in self.dices):
            self.roll()

dice_set = DiceSet()
print(dice_set.get_current())
dice_set.roll_till_all_six()
print(dice_set.get_current())
