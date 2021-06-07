import socket

C=socket.socket()

C.connect(('localhost',8080))

print(C.recv(1024).decode())