from random import randint


def roll(*dices):
    results = []
    for dice in dices:
        result = randint(1, dice)
        results.append(result)
    return results
