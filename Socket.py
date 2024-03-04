import socket
import threading
import time
import copy
import json

import Shapes

ip = '172.20.10.2'
port = 1234

class Socket :
    def send(self) :
        sub_packet = {
            'shape' : None,
            'x' : 0,
            'y' : 0,
            'side_length' : 0,
            'color' : None
        }
        packet = ''

        for object in self.parent_Client.screen.objects :
            object_sub_packet = copy.deepcopy(sub_packet)

            object_sub_packet['shape'] = 'circle'
            object_sub_packet['x'] = object.vector.x
            object_sub_packet['y'] = object.vector.y
            object_sub_packet['side_length'] = object.side_length
            object_sub_packet['color'] = object.color

            packet = packet+f";{object_sub_packet}"
             
        self.connection.send(packet.encode())

        time.sleep(0.3)
        self.send() # send again

    def receive(self) :
        while True :
            response = self.connection.recv(1024).decode()

            setter = []
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
                self.parent_Client.screen.objects = [setter.append(Shapes.Circle(single_packet['x'], single_packet['y'], single_packet['side_length'], single_packet['color']))]



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

        self.send_thread = threading.Thread(target=self.send)
        self.send_thread.start()

        self.socket_receive_thread = threading.Thread(target=self.receive)
        self.socket_receive_thread.start()


class ClientSocket(Socket) :
    def __init__(self, parent_Client) :
        self.parent_Client = parent_Client
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ip
        self.port = port
        self.connection.connect((self.host, self.port))

        self.send_thread = threading.Thread(target=self.send)
        self.send_thread.start()

        self.socket_receive_thread = threading.Thread(target=self.receive)
        self.socket_receive_thread.start()