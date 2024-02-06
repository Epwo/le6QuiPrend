'''this is the main file for the client side of the game, c'est celle qui va uniquement lancer l'interface graphique
et ensuite envoyer les messages de l'état de son jeu au serveur
Exemple : le joueur 1 (client 1) a validé la carte 12, il va donc envoyer au serveur :

'''
import time
import interface
from Multiplayer import client


def main():
    # Read the server IP from the file
    server_ip = open("Multiplayer/Master_ip.txt", "r").read().strip()
    # Create a ChatClient instance and connect to the server
    clientChat = client.ChatClient(server_ip, 8080)
    clientChat.connect()
    time.sleep(0.1)# on attends une réponse du serveur
    size = 1
    Player = None
    GameState = {"Piles": [[], [], [], []], "Joueurs": {"isReady": [], "score": [], "cartes": []}}
    # on fait une boucle infini pour pouvoir utiliser les threads.
    clickedTemp = 0
    endGame = False

    try:
        while True:
            time.sleep(0.1)
            msg = clientChat.GetReceivedMessages()
            # print(f"Player : {Player}")
            if msg[-1][:10] == "You:Joueur" and Player is None:
                Player = int(msg[-1][-1])
                print("I now am player " + str(Player))
                affich.SetWhoIAm(Player)
            # les and player is none et  != gamestate est pour éviter de constamment reecrire ces variables
            elif msg[-1][:10] == "GameState:" and msg[-1][10:] != str(GameState):
                GameState = eval(msg[-1][10:])
                print(f"GameState is now : {GameState}")
            elif msg[-1][:11] == "ChoosePile:" and msg[-1] != msg[-2]:
                print("POPUP")
                affich.PopUp(eval(msg[-1][11:]))
                print(f"il a choisit : {affich.GetPileChoice()}")
                clientChat.send_message("ChoixPile:"+str(affich.GetPileChoice()))

            if Player is not None and GameState != {"Piles": [[], [], [], []],
                                                    "Joueurs": {"isReady": [], "score": [], "cartes": []}}:
                affich.SetCards(GameState["Joueurs"]["cartes"][Player])
                affich.SetPiles(GameState["Piles"])
                dictJoueurs = []
                for i in range(len(GameState["Joueurs"]["isReady"])):
                    dictJoueurs.append({"name": "Joueur " + str(i), "score": GameState["Joueurs"]["score"][i],
                                        "isReady": GameState["Joueurs"]["isReady"][i]})
                affich.SetPlayers(dictJoueurs)
                clicked = affich.GetClickedCards()
                if clicked is not None and clicked != clickedTemp:
                    clickedTemp = clicked
                    clientChat.send_message(str(clicked))
                affich.displayPlayers()
                affich.runGameLoop()

                # Vérifiez si le jeu est terminé en fonction des informations du GameState
                cartes_du_joueur = GameState['Joueurs']['cartes']
                print(cartes_du_joueur)
                if all(not cartes for cartes in cartes_du_joueur) and msg[-1][:8] == "EndGame:" and not endGame:
                    endGame = True
                    affich.Winner(msg[-1][8:])




    except KeyboardInterrupt:
        clientChat.close()
        print("Client closed")
    # interface = interface.GameInterface(game)
    # interface.runGameLoop()
    # print("end")


if __name__ == "__main__":
    affich = interface.GameInterface(3)

    main()
