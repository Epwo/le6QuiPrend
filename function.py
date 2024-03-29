import random as rd

def MakeDict():
    DictScore = {}
    for i in range(1, 105):
        if i % 10 == 0:
            DictScore[i] = 3
        elif i == 55:
            DictScore[i] = 7
        elif i % 5 == 0:
            DictScore[i] = 2
        elif i % 11 == 0:
            DictScore[i] = 5
        else:
            DictScore[i] = 1
    return DictScore


def minPositif(liste):
    # on enleve les valeurs negatives
    positive_numbers = [num for num in liste if num > 0]
    # on renvoie le min
    min_positive = min(positive_numbers)
    return min_positive



def ListCards():
    listCards = []
    for i in range(1, 105):
        listCards.append(i)
    return listCards


def RandomCards(cards):
    listCards = cards
    chosenCard = rd.choice(listCards)
    listCards.remove(chosenCard)
    return chosenCard, listCards
