import socket
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.bind(("192.168.0.102",4444))
mysocket.listen(5)
(client,(ip,port))=mysocket.accept()
client.send("cse".encode('utf-8'))
data2=client.recv(1233)
print(data2)
mysocket.close()
