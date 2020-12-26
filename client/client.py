import socket

ip='127.0.0.1'
socket_=4050


my_socket = socket.socket()
my_socket.connect((ip,socket_))


inp=input(">>")
my_socket.send(inp.encode())
data = my_socket.recv(1024).decode()
print(data)