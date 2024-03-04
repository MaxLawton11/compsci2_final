import socket
import threading
import time
import copy
import json

import Shapes

ip = '172.20.10.2'
port = 1234

class Socket :
    def send(self, object) :
        packet = {
            'shape' : 'circle',
            'x' : object.vector.x,
            'y' : object.vector.y,
            'side_length' : object.side_length,
            'color' : object.color
        }
        self.connection.send(str(packet).encode())

    def receive(self) :
        while True :
            response = self.connection.recv(1024).decode()

            packet = response.split(';')
            packet = packet[1:]
            for single_packet in packet :
                if single_packet :
                    if single_packet[-1] != '}' :
                        continue

                single_packet = single_packet.replace("'", "\"")

                if not single_packet :
                    continue
                
                single_packet = json.loads(single_packet)
                self.parent_Client.screen.objects.append(Shapes.Circle(single_packet['x'], single_packet['y'], single_packet['side_length'], single_packet['color']) )



class MasterSocket(Socket) :
    def __init__(self, parent_Client) :
        self.parent_Client = parent_Client
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ip
        self.port = port
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        self.connection, addr = self.server_socket.accept()
        print("------", self.connection)

        self.socket_receive_thread = threading.Thread(target=self.receive)
        self.socket_receive_thread.start()


class ClientSocket(Socket) :
    def __init__(self, parent_Client) :
        self.parent_Client = parent_Client
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ip
        self.port = port
        self.connection.connect((self.host, self.port))

        self.socket_receive_thread = threading.Thread(target=self.receive)
        self.socket_receive_thread.start()