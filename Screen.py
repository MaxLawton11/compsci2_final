import pygame

class Screen : # a window of pygame
    def __init__(self) :
        self.objects = [] # objects to be printed every frame

        # crate pygame window
        pygame.init() 
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.dt = 0 # store deltatime

    def assign(self, object) : # add new object to list
        object.assignment(object)

    def frame(self) : # update frame
        self.screen.fill("white") # reset screen
        self._drawObjects()

        # show and loop
        pygame.display.flip()
        self.dt = self.clock.tick(60) / 1000 # set new deltatime

    def _drawObjects(self) : # draw the objects on screen
        for object in self.objects :
            object.draw(self.screen)



class UserInput : # get user inputs
    def __init__(self) :
        # track if the events happened in the last frame 
        self.mouse_click_last = False

    def testEvents(self) :
        for event in pygame.event.get(): # cheack for quit or "x" on window
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN : # see if mouse was pressed
                self.mouse_click_last = True # set true cuz we pressed
            else :
                self.mouse_click_last = False # mouse was not pressed in this frame, set to false

    def getMousePos(self) : # get pos of mouse
        return pygame.mouse.get_pos()
    
    def getMouseClicked(self) : # see if mouse was pressed in last frame
        return self.mouse_click_last