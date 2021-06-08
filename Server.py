import socket

server=socket.socket()
server.bind(('localhost',8080))

server.listen()

while True:
    client,address = server.accept()
    print("connection with", address)
    client.send(bytes('Hi', 'utf-8'))
    client.close()
