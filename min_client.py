import socket
s = socket.socket()

h = socket.gethostname()
port = 1234

s.connect((h, p))
print(s.recv(1024))