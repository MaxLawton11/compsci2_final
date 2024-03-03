import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 12345

server_socket.bind((host, port))

server_socket.listen(5)

print("Server listening on {}:{}".format(host, port))

client_socket, addr = server_socket.accept()
print('Got connection from', addr)

while True:
    data = client_socket.recv(1024).decode()
    print("Received:", data)

client_socket.close()
