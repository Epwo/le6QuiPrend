'''this is the main file for the client side of the game, c'est celle qui va uniquement lancer l'interface graphique
et ensuite envoyer les messages de l'état de son jeu au serveur
Exemple : le joueur 1 (client 1) a validé la carte 12, il va donc envoyer au serveur :

'''
import interface
from Multiplayer import client

if __name__ == "__main__":
    # Read the server IP from the file
    server_ip = open("Multiplayer/Master_ip.txt", "r").read().strip()

    # Create a ChatClient instance and connect to the server
    client = client.ChatClient(server_ip, 8080)
    client.connect()
    client.send_message("Hello, server!")
    # Keep the main thread alive to allow background threads to run
    try:
        while True:
            pass
    except KeyboardInterrupt:
        client.close()
        print("Client closed")
    # interface = interface.GameInterface(game)
    # interface.runGameLoop()
    # print("end")