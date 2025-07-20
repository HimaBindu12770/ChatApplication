import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen()

print("Server started... Waiting for a connection...")

client_socket, address = server.accept()
print(f"Connected with {address}")

while True:
    message = client_socket.recv(1024).decode('utf-8')
    if not message:
        break
    print(f"Client: {message}")
    reply = input("You (Server): ")
    client_socket.send(reply.encode('utf-8'))

client_socket.close()
server.close()
