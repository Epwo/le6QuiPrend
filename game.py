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
            cartesJoueur = []
            for j in range(10):
                CurrentsCartes = self.GetCards()
                newCarte, ResteCartes = function.RandomCards(CurrentsCartes)
                cartesJoueur.append(newCarte)
                self.SetCards(ResteCartes)
                # Joueur {i} a pioché la carte {newCarte}

            self._players.append(Player('J' + str(i), cartesJoueur))
            # On va mettre dans cette liste les cartes de joueurs qui ont validé leur carte
            # de telle sorte que la carte joué de Joueur 0 (-> J0): self._ReadyList[0] = *numero de la carte*
            self._ReadyList.append(0)

    def validCarte(self, carte, NbJoueur):
        self._ReadyList[NbJoueur] = carte
        joueur = self.getJoueurs()[NbJoueur]
        joueur.setCartes(joueur.removeCarte(carte))

    def GetWinner(self):
        scores = self.getScores()
        return scores.index(min(scores))

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
        if self.nbJoueurs == nb:
            # tous les joueurs ont validé leur carte
            self.play()
            # une fois qu'on a fini de jouer on remet la liste Ready a 0 pour chaque joueur
            self._ReadyList = [0] * len(self._ReadyList)
        elif self.nbJoueurs * (2 / 3) <= nb:
            # plus de 2/3 des joueurs ont validé leur carte
            # on lance le TIMER
            print("ATTENTION : plus de 2/3 des joueurs ont validé leur carte, le jeu va commencer !")


    def GetCards(self):
        return self._cards

    def SetCards(self, cards):
        self._cards = cards

    def getJoueurs(self):
        return self._players

    def getCartes(self):
        cartes = []
        for joueur in self.getJoueurs():
            cartes.append(joueur.getCartes())
        return cartes

    def CreatePiles(self, cartes):
        piles = [[], [], [], []]
        for i in range(4):
            carteChoisie, cartes_rest = function.RandomCards(cartes)
            piles[i].append(carteChoisie)
            self.SetCards(cartes_rest)
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
            # FAIRE cas ou la carte est plus petite que la plus petite carte de la pile
            print(piles)
            for pile in piles:
                deltas.append(CarteJoueur - pile[-1])
            print('deltas >', deltas)
            # on va check si tt les deltas sont negatifs, ce qui signifie que la carte est plus petite que toutes les
            # cartes des piles
            if all(delta < 0 for delta in deltas):
                # on va donc demander au joueur de choisir la pile qu'il va remplacer
                # on va donc afficher les piles
                for pile in piles:
                    print(f"    la pile {piles.index(pile)} :{pile} qui vaut : {self.CalculScore(pile)}")
                print("veuillez choisir une des piles que vous allez remplacer, vous récupereez les vachettes de la "
                      "pile choisie")
                choice = input("veuillez choisir une pile : 0,1,2,3 :")
                while deltas[int(choice)] > 0:
                    print("vous ne pouvez que prendre une pile qui est plus petite que votre carte")
                    choice = input("veuillez choisir une pile : 0,1,2,3 :")
                # on va donc remplacer la pile choisie par la carte du joueur
                Joueur = self.getJoueurs()[listeCartes.index(CarteJoueur)]
                print(
                    f"Joueur {listeCartes.index(CarteJoueur)} a récupéré les vachettes de la pile {choice}, la pile "
                    f"était {piles[int(choice)]} et valais {self.CalculScore(piles[int(choice)])}")
                Joueur.setNewScore(self.CalculScore(piles[int(choice)]))
                self.SetPile(int(choice), [CarteJoueur])

            else:
                print(
                    f"la carte de Joueur {listeCartes.index(CarteJoueur)} est la plus proche"
                    f" de la pile {deltas.index(function.minPositif(deltas))}")
                # on va donc ajouter la carte du joueur à la pile la plus proche
                # il faut aussi verifier que ce soit le min mais qu'il soit positif
                self.AddCarteToPile(CarteJoueur, deltas.index(function.minPositif(deltas)))
            # on va vérifier si on arrive a une fin de pile ( >6)
            for pile in piles:
                if len(pile) > 5:
                    print(
                        f"la pile {piles.index(pile)} est pleine{pile}, le joueur {listeCartes.index(CarteJoueur)} récup"
                        f"ère les vachettes")
                    Joueur = self.getJoueurs()[listeCartes.index(CarteJoueur)]
                    Joueur.setNewScore(self.CalculScore(pile[:-1]))
                    self.SetPile(piles.index(pile), [pile[-1]])

    def getPiles(self):
        return self._piles

    def AddCarteToPile(self, carte, nbPile):
        self._piles[nbPile].append(carte)

    def SetPile(self, nbPile, DataPile):
        self._piles[nbPile] = DataPile

    def getScores(self):
        scores = []
        for joueur in self.getJoueurs():
            scores.append(joueur.getScore())
        return scores


class Player:
    def __init__(self, name, cartes, score=0, isReady=False):
        self._cartes = cartes
        self._score = score
        self._name = name
        self._isReady = isReady

    def setCartes(self, cartes):
        self._cartes = cartes

    def setScore(self, score):
        self._score = score

    def setNewScore(self, score):
        self._score += score

    def setName(self, name):
        self._name = name

    def setIsReady(self, isReady):
        self._isReady = isReady

    def getCartes(self):
        return self._cartes

    def removeCarte(self, carte):
        self._cartes.remove(carte)
        return self._cartes

    def getScore(self):
        return self._score

    def getName(self):
        return self._name

    def getIsReady(self):
        return self._isReady


if __name__ == "__main__":
    G = Game()
    # comme on n'a pas précisé le nombre de joueurs, on a automatiquement 2 joueurs
    # on va regarder les cartes du Joueur 0
    for i in range(8):
        print(f"--------tour {i}---------------")
        cartesJ0 = G.getJoueurs()[0].getCartes()
        print(f"cartes de J0> {cartesJ0}")
        # on va regarder les cartes du Joueur 1
        cartesJ1 = G.getJoueurs()[1].getCartes()
        print(f"cartes de J1> {cartesJ1}")
        # on va regarder les cartes des piles
        print(f"cartes des piles> {G.getPiles()}")
        # on va faire jouer le Joueur 0 artificielement. il jouera automatiquement sa premiere carte.
        print(f"J0 joue la carte {cartesJ0[0]}")
        G.validCarte(cartesJ0[0], 0)
        print(f"J1 joue la carte {cartesJ1[0]}")
        G.validCarte(cartesJ1[0], 1)
        # on teste pour jouer
        G.CheckReady()
        # on re affiche la pile
        print(f"cartes des piles> {G.getPiles()}")
        print("scores des joueurs :", G.getScores())
    print("")
    print(f"le gagnant est le joueur {G.GetWinner()}")