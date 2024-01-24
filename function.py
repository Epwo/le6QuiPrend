import random as rd

def DicoScore():
    DicoScore = {}
    for i in range(1, 105) :
        if(i%10==0):
            DicoScore[i] = 3
        elif(i == 55) :
            DicoScore[i] = 7
        elif(i%5==0):
            DicoScore[i] = 2
        elif(i%11 == 0) :
            DicoScore[i] = 5
        else :
            DicoScore[i] = 1
    return DicoScore

def ListCards():
    listCards = []
    for i in range(1, 105):
        listCards.append(i)
    return listCards

def RandomCards():
    listCards = ListCards()
    chosenCard = rd.choice(listCards)
    listCards.remove(chosenCard)
    return chosenCard, listCards
