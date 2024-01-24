# let's start this !
class Game:
    def __init__(self, nb_players=2):
        self._board = Board()
        self.nbJoueurs = nb_players
        self._player = Player()
        self.isGameOver = False
        self._piles = {'pile1': [], 'pile2': [], 'pile3': [], 'pile4': []}
        self._dictScore = {}
        self._ReadyList = []
        for i in range(nb_players):
            self._dictScore['J' + str(i)] = 0
            # On va mettre dans cette liste les cartes de joueurs qui ont validé leur carte
            # de telle sorte que la carte joué de Joueur 1 (-> J1-1): self._ReadyList[0] = *numero de la carte*
            self._ReadyList.append(0)

    def validCarte(self, carte, joueur):
        self._ReadyList[joueur - 1] = carte

    def CleanPile(self, pile,player):
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
        if self.nbJoueurs * (2/3) <= nb:
            # plus de 2/3 des joueurs ont validé leur carte
            DisplayClock()
        elif self.nbJoueurs == nb:
            # tous les joueurs ont validé leur carte
            self.play()

    def play(self):
        # tri dans l'ordre croissant des cartes

        self._board.print()
