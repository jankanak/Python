import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
mysock.connect(("192.168.0.102",1337))
mysock.sendto(("hello from client".encode('utf-8')),("192.168.0.102",1337))
