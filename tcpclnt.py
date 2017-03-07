from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 2000))
s.send(b'How are you')
x = s.recv(8192)
print(x)
