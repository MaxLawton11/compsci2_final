import lib.ScreenObjects as ScreenObjects
import lib.Socket as Socket
import lib.Screen as Screen

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
            self.screen.assign(ScreenObjects.Square(cx,cy, 20, self.shape_color )) # print a shape localy
            self.socket.send(ScreenObjects.Square(cx,cy, 20, self.shape_color )) # send a shape to peer

        # send keybind cmds
        if self.user_input.getCClicked() : # clear on c
            self.screen.assign(ScreenObjects.Clear())
            self.socket.send(ScreenObjects.Clear()) # send a clear cmd to peer

        if self.user_input.getRClicked() : # red on r
            self.screen.assign(ScreenObjects.ChangeGBColor('firebrick1'))
            self.socket.send(ScreenObjects.ChangeGBColor('firebrick1'))

        if self.user_input.getGClicked() : # green on g
            self.screen.assign(ScreenObjects.ChangeGBColor('green3'))
            self.socket.send(ScreenObjects.ChangeGBColor('green3'))

        if self.user_input.getBClicked() : # blue on b
            self.screen.assign(ScreenObjects.ChangeGBColor('lightslateblue'))
            self.socket.send(ScreenObjects.ChangeGBColor('lightslateblue'))

        if self.user_input.getWClicked() : # white on white
            self.screen.assign(ScreenObjects.ChangeGBColor('white'))
            self.socket.send(ScreenObjects.ChangeGBColor('white'))

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


    