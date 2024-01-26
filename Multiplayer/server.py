import socket
import threading

clients = []


def broadcast(message, sender_socket, sender_name):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(f"{sender_name} : {message.decode('utf-8')}".encode('utf-8'))
            except socket.error:
                # Remove the client if unable to send a message to it
                clients.remove(client)


def handle_client(client_socket):
    while True:
        try:
            # on recupere l'objet socket du client dans client_socket
            # on va recuperer les donnees
            data = client_socket.recv(1024)
            if not data:
                # si pas de donnees, on sort de la boucle handle_client, car plus rien a faire
                break

            print(f"Received message: {data.decode('utf-8')} from {client_socket.getpeername()}")
            if client_socket in clients:
                # on envoie les donnees a tous les clients
                print(f"message du client {clients.index(client_socket)}")
            # Broadcast the message to all clients
            ClientName = f"Joueur{clients.index(client_socket)}"
            broadcast(data, client_socket, ClientName)

        except socket.error:
            # Remove the client if there is an error receiving data
            clients.remove(client_socket)
            break

    # Close the client socket
    client_socket.close()


def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind(('0.0.0.0', 8080))

    # Enable the server to accept connections
    server_socket.listen(5)
    print("Server listening on port 8080")

    while True:
        # Accept a connection from a client
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        # Add the client to the list
        clients.append(client_socket)

        # Create a thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_server()
