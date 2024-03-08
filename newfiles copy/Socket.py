import socket
import threading
import json
import warnings

import ScreenObjects as ScreenObjects

# ip of master computer
ip = '172.16.31.61'
port = 1234

class Socket : # basic socket menthods
    def send(self, object) : # send info over socket
        packet = { # basic json packet
            # Note: this packet is overengineered, but the thought was that you could have non-shape \
            # cmds also sent via the packet. (ie. Clear, ChangeBgColor, etc)
            'type'        : object.type,       # everthying sent must have a type
            'x'           : object.vector.x    if isinstance(object, ScreenObjects.Shape) else None,
            'y'           : object.vector.y    if isinstance(object, ScreenObjects.Shape) else None,
            'side_length' : object.side_length if isinstance(object, ScreenObjects.Shape) else None,
            'color'       : object.color       if isinstance(object, ScreenObjects.Shape) else None,
        }
        self.connection.send(str(packet).encode()) # send packet

    def receive(self) : # receive packet
        while True : # always be looking for new packets
            packet = self.connection.recv(1024).decode() # look for new packet (waits unit it finds one)

            if packet : # test if the packet is vaild
                if packet[-1] != '}' :
                    continue # next packet

            packet = packet.replace("'", "\"") # make sure there isn't any ' cuz we need " for json

            if (not packet) or (packet.count('}') >= 2) : # more packet testing
                continue # next packet
            
            print(packet) # show pacet
            packet = json.loads(packet) # turn back into json

            match packet['type'] : # see how this type of packet should be handled
                case 'Shape' : # is a shape
                    self.parent_Client.screen.addObject(ScreenObjects.Square(packet['x'], packet['y'], packet['side_length'], packet['color']) ) # add new packet to local screen
                case _ : # if none of above
                    warnings.warn("Invalid packet type received. Moving on.") # let user know that there was an incorrect packet
                    continue

class MasterSocket(Socket) : # the Master Socket
    def __init__(self, parent_Client) :
        self.parent_Client = parent_Client # track parent

        # start socker server
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ip
        self.port = port
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        self.connection, addr = self.server_socket.accept() # wait for a client to join
        print("------", self.connection, "------") # show one has joined

        # start receiving (runs in parallel)
        self.socket_receive_thread = threading.Thread(target=self.receive)
        self.socket_receive_thread.start()


class ClientSocket(Socket) : # the Client Socket
    def __init__(self, parent_Client) :
        self.parent_Client = parent_Client # track parent

        # join socket server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ip
        self.port = port
        self.connection.connect((self.host, self.port))

        # start receiving (runs in parallel)
        self.socket_receive_thread = threading.Thread(target=self.receive)
        self.socket_receive_thread.start()