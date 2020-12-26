import socket
port=4050

ip='0.0.0.0'


def get_request(client_socket):  # get request
    full_request=""
    got_request=False
    while not got_request:
        # print("getting request")
        request = client_socket.recv(1024).decode()
        # print(len(request))
        full_request += request
        if len(request)<=1024:
            # print("got request")
            got_request=True
    return full_request


# client_socket.shutdown(1)

def create_server():
    server_socket = socket.socket()
    try:
        server_socket.bind((ip, port))
        server_socket.listen(5)
        print("Server is up and running")
        (client_socket, client_address) = server_socket.accept()
        print("Client connected")
        a=get_request(client_socket)
        print(a)
        client_socket.sendall(a.encode())
        client_socket.shutdown(1)
        server_socket.close()
    except KeyboardInterrupt:
        server_socket.close()
    except Exception as exp:
        server_socket.close()
        print("Exp: "+ str(exp))


create_server()
