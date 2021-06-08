import socket

client=socket.socket()

client.connect(('localhost',8080))

print(client.recv(1024).decode())
