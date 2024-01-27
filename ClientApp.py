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
    clientChat.send_message("Hello, server!")
    # Keep the main thread alive to allow background threads to run
    # Interface Vars
    size = 1
    Player = None
    GameState = {"Piles": [[], [], [], []], "Joueurs": {"isReady": [], "score": [], "cartes": []}}
    try:
        while True:
            msg = clientChat.GetReceivedMessages()
            # print(f"Player : {Player}")
            if msg[-1][:10] == "You:Joueur" and Player is None:
                Player = int(msg[-1][-1])
                print("I now am player " + str(Player))
            # les and player is none et  != gamestate est pour éviter de constamment reecrire ces variables
            elif msg[-1][:10] == "GameState:" and eval(msg[-1][10:]) != GameState:
                GameState = eval(msg[-1][10:])
                print(f"GameState is now : {GameState}")

            if Player is not None and GameState != {"Piles": [[], [], [], []], "Joueurs": {"isReady": [], "score": [], "cartes": []}}:
                affich.SetCards(GameState["Joueurs"]["cartes"][Player])
                affich.SetPiles(GameState["Piles"])
                dictJoueurs = []
                for i in range(len(GameState["Joueurs"]["isReady"])):
                    dictJoueurs.append({"name": "Joueur " + str(i), "score": GameState["Joueurs"]["score"][i],
                                        "isReady": GameState["Joueurs"]["isReady"][i]})
                affich.SetPlayers(dictJoueurs)
                affich.runGameLoop()



    except KeyboardInterrupt:
        clientChat.close()
        print("Client closed")
    # interface = interface.GameInterface(game)
    # interface.runGameLoop()
    # print("end")


if __name__ == "__main__":
    affich = interface.GameInterface(3)

    main()
