# let's start this !
class Game:
    def __init__(self, nb_players=2):
        #self._board = Board()
        self.nbJoueurs = nb_players
        self.isGameOver = False
        self._piles = {'pile1': [], 'pile2': [], 'pile3': [], 'pile4': []}
        self._dictScore = {}
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
        return pile

    def CalculScore(self, listeCartes):
        score = 0
        for carte in listeCartes:
            score += DictScore[carte]
        return score

    def CheckReady(self):
        nb = 0
        for e in self._ReadyList:
            if e != 0:
                nb += 1
        if self.nbJoueurs * (2 / 3) <= nb:
            # plus de 2/3 des joueurs ont validé leur carte
            DisplayClock()
        elif self.nbJoueurs == nb:
            # tous les joueurs ont validé leur carte
            self.play()

    def play(self):
        # tri dans l'ordre croissant des cartes
        self._board.print()

class Player(Game):
    def __init__(self,name):
        self._cartes = []
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


G = Game(nb_players=4)
G.play()
