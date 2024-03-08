import ScreenObjects as ScreenObjects
import Socket as Socket
import Screen as Screen

class _SubClient : # holds the methods used by both types of clients
    def __init__(self) :
        self.screen = Screen.Screen() # computer's screen
        self.user_input = Screen.UserInput() # input from screen

    def tick(self) : # run ever time the clock ticks
        self.user_input.testEvents() # update eventss
        self.addObjectOnClick() # add object
        self.screen.frame() # new frame

    def addObjectOnClick(self) : # if the mosue was pressed, then print and send a shape
        if self.user_input.getMouseClicked() : # test for press
            cx, cy = self.user_input.getMousePos() # get cords
            self.screen.assign( ScreenObjects.Square(cx,cy, 20, self.shape_color )) # print a shape localy
            self.socket.send(ScreenObjects.Square(cx,cy, 20, self.shape_color )) # send a shape to peer

        if self.user_input.getCClicked() :
            self.socket.send(ScreenObjects.Clear()) # send a clear cmd to peer

class Client(_SubClient) : # the Client
    def __init__(self):
        super().__init__()
        self.socket = Socket.ClientSocket(self) # has a "Client" socket
        self.shape_color = 'red' # prints red shapes

class Master(_SubClient) : # the Master
    def __init__(self):
        super().__init__()
        self.socket = Socket.MasterSocket(self) # has a "Master" socket
        self.shape_color = 'blue' # prints blue shapes


    