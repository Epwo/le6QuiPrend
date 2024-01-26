import socket
import threading
# on va lire le fichier Master_ip.txt pour recuperer l'adresse ip du serveur
ip = open("Master_ip.txt", "r").read()

def receive_messages(client_socket):
    while True:
        try:
            # Receive and print messages from the server
            message = client_socket.recv(1024).decode('utf-8')
            print(f"\n Received message: {message}")
        except socket.error:
            # Break the loop if there is an error receiving data
            break

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((ip, 8080))
    # attention a bien prendre l'adresse ip de la machine serveur, en wifi, pas en ethernet !!
    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        # Get user input
        message = input("Enter your message: ")

        # Send the message to the server
        client_socket.send(message.encode('utf-8'))

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    start_client()
