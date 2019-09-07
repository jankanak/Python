import socket
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(("192.168.0.102",4444))
data=mysocket.recv(2048)
print (data)
data1=mysocket.send("pust".encode('utf-8'))
mysocket.close()
