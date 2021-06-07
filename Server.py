import socket

S=socket.socket()
S.bind(('localhost',8080))

S.listen()

while True:
    C,address = S.accept()
    print("connection with", address)
    C.send(bytes('Hi', 'utf-8'))
    C.close()