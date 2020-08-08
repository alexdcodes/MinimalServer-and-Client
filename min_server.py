import socket

s = socket.socket()

h = socket.gethostname()
p = 1234
s.bind((h, p))

s.listen(5)
while True:
    c, addr = s.accept()
    print("Got Connection! from", addr)
    c.send("Thank you for connecting")
    c.close()