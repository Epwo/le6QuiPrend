import socket
import threading
import time


class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.received_messages = []

    def GetReceivedMessages(self):
        return self.received_messages

    def broadcast(self, message):
        # afin d'éviter une concatenation post send, on va écrire 'lafin' du message avec '\end'
        message = (message.decode('utf-8') + '\\end').encode('utf-8')
        for client in self.clients:
            try:
                client.send(message)
            except socket.error:
                # Remove the client if unable to send a message to it
                self.clients.remove(client)
        time.sleep(0.05)

    def send_to_client(self, client_index, message, sender_name):

        time.sleep(0.2)  # on attend que le mesage precedent ai été envoyé
        if 0 <= client_index < len(self.clients):
            try:
                self.clients[client_index].send(f"{sender_name} : {message}".encode('utf-8'))
            except socket.error:
                # Remove the client if unable to send a message to it
                self.clients.remove(self.clients[client_index])

    def EmptyMessages(self, nbPlayer):
        self.received_messages = self.received_messages[:-nbPlayer]

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                if not data:
                    break

                ClientName = f"Joueur{self.clients.index(client_socket)}"
                print(f"Received message: {data.decode('utf-8')} from {ClientName} ({client_socket.getpeername()})")
                self.received_messages.append([ClientName, data.decode('utf-8')])
                self.broadcast(('You:' + ClientName).encode('utf-8'))
                time.sleep(0.5)

            except socket.error:
                self.clients.remove(client_socket)
                break

        client_socket.close()

    def GetClients(self):
        return self.clients

    def GetMessages(self):
        return self.received_messages

    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Accepted connection from {addr}")

            self.clients.append(client_socket)

            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

    def close(self):
        for client in self.clients:
            client.close()
        self.server_socket.close()


if __name__ == "__main__":
    server = ChatServer("localhost", 8080)
    server.start_server()
