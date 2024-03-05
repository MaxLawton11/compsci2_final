import socket
import threading
import json

import Shapes

ip = '172.20.10.2'
port = 1234

class Socket :
    def send(self, object) :
        packet = { # basic json packet
            'type'        : object.type,
            'x'           : object.vector.x    if isinstance(object, Shapes.Shape) else None,
            'y'           : object.vector.y    if isinstance(object, Shapes.Shape) else None,
            'side_length' : object.side_length if isinstance(object, Shapes.Shape) else None,
            'color'       : object.color       if isinstance(object, Shapes.Shape) else None,
        }
        packet = { # basic json packet
            'type'        : object.type,
            'x'           : object.vector.x,
            'y'           : object.vector.y,
            'side_length' : object.side_length,
            'color'       : object.color,
        }
        self.connection.send(str(packet).encode()) 

    def receive(self) :
        while True :
            packet = self.connection.recv(1024).decode()

            print("-RAW->", packet)

            if packet :
                if packet[-1] != '}' :
                    continue

            packet = packet.replace("'", "\"")

            if (not packet) or (packet.count('}') >= 2) :
                continue
            
            print(packet)
            packet = json.loads(packet) # turn back into json

            self.parent_Client.screen.objects.append(Shapes.Square(packet['x'], packet['y'], packet['side_length'], packet['color']) )



class MasterSocket(Socket) :
    def __init__(self, parent_Client) :
        self.parent_Client = parent_Client
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ip
        self.port = port
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        self.connection, addr = self.server_socket.accept()
        print("------", self.connection, "------")

        # start receiving
        self.socket_receive_thread = threading.Thread(target=self.receive)
        self.socket_receive_thread.start()


class ClientSocket(Socket) :
    def __init__(self, parent_Client) :
        self.parent_Client = parent_Client
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ip
        self.port = port
        self.connection.connect((self.host, self.port))

        # start receiving
        self.socket_receive_thread = threading.Thread(target=self.receive)
        self.socket_receive_thread.start()