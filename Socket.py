import socket
import threading
import time
import copy

class Socket :
    def __init__(self, parent_Client) :
        self.parent_Client = parent_Client
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '192.168.1.63'
        self.port = 12345
        self.connection.connect((self.host, self.port))

        self.send_thread = threading.Thread(target=self.send)
        self.send_thread.start()

    def send(self) :
        sub_packet = {
            'shape' : None,
            'x' : 0,
            'y' : 0
        }
        packet = ''

        for object in self.parent_Client.screen.objects :
            object_sub_packet = copy.deepcopy(sub_packet)
            object_sub_packet['shape'] = 'circle'
            object_sub_packet['x'] = object.vector.x
            object_sub_packet['y'] = object.vector.y
            packet = packet+f";{object_sub_packet}"
             
        self.connection.send(packet.encode())

        time.sleep(0.3)
        self.send()

class MasterSocket :
    def __init__(self, parent_Client=None) :
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '192.168.1.63'
        self.port = 12345
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        self.client, addr = self.server_socket.accept()
        print("------", self.client)

        self.socket_receive_thread = threading.Thread(target=self.receive)
        self.socket_receive_thread.start()

    def receive(self) :
        while True :
            response = self.client.recv(1024).decode()

            print(response)

            response = response.split(';')
            response = response[1:]
            print(response)