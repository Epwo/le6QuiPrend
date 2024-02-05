from Multiplayer import server
import game
import threading
import time


def main():
    # Read the server IP from the file
    server_ip = open("Multiplayer/Master_ip.txt", "r").read().strip()
    nbPlayer = 1
    flagChangePile = False
    # Create a ChatServer instance and connect to the server
    chat_server = server.ChatServer(server_ip, 8080)
    chat_server_thread = threading.Thread(target=chat_server.start_server)
    chat_server_thread.start()
    G = game.Game(nb_players=nbPlayer)
    GameState = {"Piles": G.getPiles(), "Joueurs": {"isReady": G.getReadyList(), "score": G.getScores(),
                                                    "cartes": G.getCartes()}}
    try:
        while True:
            # on va actualiser l'etat du jeu toute les 0.4 secondes, pour eviter que les messages ne se melangent
            time.sleep(0.4)
            if len(chat_server.GetClients()) == len(G.getJoueurs()):
                # on peut lancer la logique du jeu tt le monde est la !
                # on va donc envoyer a chaque client le GameState ( etat du jeu)
                GameState = {"Piles": G.getPiles(), "Joueurs": {"isReady": G.getReadyList(), "score": G.getScores(),
                                                                "cartes": G.getCartes()}}
                chat_server.broadcast(('GameState:' + str(GameState)).encode('utf-8'))
                # on va maintenant regarder si on a recu des messages de la part des clients
                # messages qui sont forcément la carte que l'on a tiré.
                msg = chat_server.GetReceivedMessages()

                if msg[-1][1] == 'GetGameState':
                    chat_server.broadcast(('GameState:' + str(GameState)).encode('utf-8'))
                elif msg[-1][1][:10] == 'ChoixPile:':
                    if not flagChangePile:
                        flagChangePile = True
                        print(f"Joueur {msg[-1][0][-1]} a choisi la pile {msg[-1][1][10:]}")
                        G.replacePile(int(msg[-1][1][10:]), int(msg[-1][0][-1]))
                        print("---Pile changée---")
                        print(chat_server.GetReceivedMessages())
                        chat_server.EmptyMessages(nbPlayer)
                        print(chat_server.GetReceivedMessages())
                        time.sleep(1)
                        flagChangePile = False
                    flagChangePile = True
                    print(msg[-1][0][-1]+" a choisi la pile : " + msg[-1][1][10:])
                    G.replacePile(int(msg[-1][1][10:]), int(msg[-1][0][-1]))
                    time.sleep(1)
                elif msg[-1] is not None:
                    IsReady = G.getReadyList()[int(msg[-1][0][-1])]
                    # on va verifier si on a pas deja validé la carte
                    if IsReady == 0:
                        # c'est un peu moche mais si on traduit ca :
                        # msg[-1] = ['Joueur0', '2']
                        # donc msg[-1][1] = '2'
                        print(f"carte {int(msg[-1][1])} validée pour {msg[-1][0]}")
                        G.validCarte(int(msg[-1][1]), int(msg[-1][0][-1]))
                        # on va supprimer les derniers messages (nb Players) recu (= les cartes validees) maitenant
                        # qu'elles ont été jouées.
                        if all(value != 0 for value in G.getReadyList()):
                            chat_server.EmptyMessages(nbPlayer)
                if G.CheckReady():
                    etat = G.play()
                    if etat != "continue":
                        joueur, cartes, score = etat
                        # on a un probleme, il faut remplacer une pile
                        # on va demaner au joueur en question de choisir la pile qu'il veut.
                        print(f"Joueur {joueur} a joué la carte {cartes}, et doit choisir une pile")
                        for i in range(len(score)):
                            print(f"pile {i} : {score[i]}")
                        chat_server.send_to_client(joueur, f"ChoosePile:{score}")


    except KeyboardInterrupt:
        chat_server.close()
        print("Server closed")


if __name__ == "__main__":
    main()
