from Multiplayer import server
import game
import threading
import time

def main():
    # Read the server IP from the file
    server_ip = open("Multiplayer/Master_ip.txt", "r").read().strip()

    # Create a ChatServer instance and connect to the server
    chat_server = server.ChatServer(server_ip, 8080)
    chat_server_thread = threading.Thread(target=chat_server.start_server)
    chat_server_thread.start()
    G = game.Game(nb_players=3)
    GameState = {"Piles": G.getPiles(), "Joueurs": {"isReady": G.getReadyList(), "score": G.getScores(),
                                                    "cartes": G.getCartes()}}
    try:
        while True:
            # on va actualiser l'etat du jeu toute les secondes
            time.sleep(1)
            if len(chat_server.GetClients()) == len(G.getJoueurs()):
                # on peut lancer la logique du jeu tt le monde est la !
                # on va donc envoyer a chaque client le GameState ( etat du jeu)
                chat_server.broadcast(('GameState:'+str(GameState)).encode('utf-8'))
    except KeyboardInterrupt:
        chat_server.close()
        print("Server closed")


if __name__ == "__main__":
    main()
