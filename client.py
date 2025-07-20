import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

print("Connected to the server...")

while True:
    message = input("You (Client): ")
    client.send(message.encode('utf-8'))
    reply = client.recv(1024).decode('utf-8')
    print(f"Server: {reply}")
