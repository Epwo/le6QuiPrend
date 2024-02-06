import socket
import threading
import time


class ChatClient:
    def __init__(self, server_address, server_port):
        self.server_address = server_address
        self.server_port = server_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
        self.ReceivedMessage = [None]


    def GetReceivedMessages(self):
        return self.ReceivedMessage

    def receive_messages(self):
        while self.connected:
            try:
                # Receive and print messages from the server
                message = self.socket.recv(1024).decode('utf-8')
                endSeparator = message.find('\\end')
                if endSeparator != -1:
                    message = message[:endSeparator]
                if message != self.ReceivedMessage[-1]:
                    self.ReceivedMessage.append(message)
                    print(f"new : {message}")
                    print(f"messageS: {self.ReceivedMessage}")
            except socket.error:
                break

    def send_message(self, message):
        if self.connected:
            # Send the message to the server
            self.socket.send(message.encode('utf-8'))

    def connect(self):
        try:
            self.socket.connect((self.server_address, self.server_port))
            self.connected = True

            # Start a thread to receive messages from the server
            receive_thread = threading.Thread(target=self.receive_messages, daemon=True)
            receive_thread.start()

            # Send a test message after connecting
            self.send_message('GetGameState')
        except Exception as e:
            print(f"Error connecting to the server: {e}")

    def close(self):
        self.connected = False
        self.socket.close()


if __name__ == "__main__":
    # Read the server IP from the file
    server_ip = open("Master_ip.txt", "r").read().strip()

    # Create a ChatClient instance and connect to the server
    client = ChatClient(server_ip, 8080)
    client.connect()
    client.send_message("Hello, server!")
    # Keep the main thread alive to allow background threads to run
    try:
        while True:
            pass
    except KeyboardInterrupt:
        # Close the client when the user presses Ctrl+C
        client.close()
