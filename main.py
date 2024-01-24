# let's start this !
import function


class Game:
    def __init__(self, nb_players=2):
        # self._board = Board()
        self._cards = function.ListCards()
        self.nbJoueurs = nb_players
        self.isGameOver = False
        self._piles = self.CreatePiles(self._cards)
        self._dictScore = function.MakeDict()
        self._ReadyList = []
        self._players = []
        for i in range(nb_players):
            self._players.append(Player('J' + str(i)))
            # On va mettre dans cette liste les cartes de joueurs qui ont validé leur carte
            # de telle sorte que la carte joué de Joueur 0 (-> J0): self._ReadyList[0] = *numero de la carte*
            self._ReadyList.append(0)

    def validCarte(self, carte, joueur):
        self._ReadyList[joueur - 1] = carte

    def CleanPile(self, pile, player):
        pile = pile[-1]
        self._players[player].setScore(self._players[player].getScore() + self.CalculScore(pile))
        return pile

    def CalculScore(self, listeCartes):
        score = 0
        for carte in listeCartes:
            score += self._dictScore[carte]
        return score

    def CheckReady(self):
        nb = 0
        for e in self._ReadyList:
            if e != 0:
                nb += 1
        if self.nbJoueurs * (2 / 3) <= nb:
            # plus de 2/3 des joueurs ont validé leur carte
            pass
        elif self.nbJoueurs == nb:
            # tous les joueurs ont validé leur carte
            self.play()

    def GetCards(self):
        return self._cards

    def SetCards(self, cards):
        self._cards = cards

    def CreatePiles(self, cartes):
        piles = [0,0,0,0]
        for i in range(4):
            piles[i], cards_rest = function.RandomCards(cartes)
            self.SetCards(cards_rest)
        return piles
    def getReadyList(self):
        return self._ReadyList

    def play(self):
        # tri dans l'ordre croissant des cartes
        listeCartes = self.getReadyList()
        SortListeCartes = listeCartes.copy()
        SortListeCartes.sort()
        for CarteJoueur in SortListeCartes:
            print(f"carte la plus petite : {CarteJoueur}, par le joueur {listeCartes.index(CarteJoueur)}")
            # on sait ansi que le joueur `listeCartes.index(e)` a joué la carte `e`, et ce dans le bon ordre
            # on doit donc comparer aux cartes des piles
            piles = self.getPiles()
            deltas = []
            for CartePile in piles:
                deltas.append(abs(CartePile - CarteJoueur))
            print('>',deltas)


    def getPiles(self):
        return self._piles


class Player(Game):
    def __init__(self, name):
        self._cartes = []
        for i in range(10):
            CurrentsCartes = Game.GetCards(self)
            newCarte, ResteCartes = function.RandomCards(CurrentsCartes)
            self._cartes.append(newCarte)
            Game.SetCards(self, ResteCartes)
        self._score = 0
        self._name = name
        self._isReady = False

    def setCartes(self, cartes):
        self._cartes = cartes

    def setScore(self, score):
        self._score = score

    def setName(self, name):
        self._name = name

    def setIsReady(self, isReady):
        self._isReady = isReady

    def getCartes(self):
        return self._cartes

    def getScore(self):
        return self._score

    def getName(self):
        return self._name

    def getIsReady(self):
        return self._isReady


G = Game()
print(G.CalculScore([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
G.play()
G.play()