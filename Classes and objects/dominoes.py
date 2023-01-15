class Domino(object):
    def __init__(self, value_a, value_b):
        self.values = [value_a, value_b]
    
        

    def __repr__(self):
        return '[{}, {}]'.format(self.values[0], self.values[1])

def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes

def order_dominoes(dominoes):
    ordered_dominoes = [dominoes.pop(0)]
    while dominoes:
        for i, domino in enumerate(dominoes):
            if domino.values[0] == ordered_dominoes[-1].values[1]:
                ordered_dominoes.append(dominoes.pop(i))
                break
            elif domino.values[1] == ordered_dominoes[-1].values[1]:
                domino.values.reverse()
                ordered_dominoes.append(domino)
                dominoes.pop(i)
                break
    return ordered_dominoes

dominoes = initialize_dominoes()

ordered_dominoes = order_dominoes(dominoes)

print(ordered_dominoes)
# You have the list of Dominoes
# Order them into one snake where the adjacent dominoes have the same numbers on their adjacent sides
# eg: [2, 4], [4, 3], [3, 5] ...