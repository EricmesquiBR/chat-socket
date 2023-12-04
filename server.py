import socket
import threading
import datetime

class ChatServer:
    def __init__(self, host='localhost', port=9001):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        self.clients = {}
        self.nicknames = {}

    def broadcast(self, message, sender):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for client, nickname in self.clients.items():
            if client != sender:
                client.send(f'{timestamp} - {self.clients[sender]}: {message}'.encode('utf-8'))
                with open('chat_log.txt', 'a') as f:
                    f.write(f'{timestamp} - {self.clients[sender]}: {message}\n')

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                self.broadcast(message, client)
            except Exception as e:
                print(f'Error: {e}')
                client.close()
                del self.clients[client]
                break

    def receive(self):
        while True:
            client, address = self.server.accept()
            nickname = client.recv(1024).decode('utf-8')
            self.clients[client] = nickname
            print(f'{nickname} has joined the chat')
            with open('chat_log.txt', 'a') as f:
                f.write(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - {nickname} has joined the chat\n')
            threading.Thread(target=self.handle_client, args=(client,)).start()

    def run(self):
        print('Server started...')
        self.receive()

chat_server = ChatServer()
chat_server.run()
