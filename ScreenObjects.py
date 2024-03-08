import pygame

class Sendable :
    pass

class Shape(Sendable) : # basic shape
    def __init__(self, x:float, y:float) :
        self.vector = pygame.Vector2(x, y) # pos of shape
        self.type = 'Shape' # type

    def assignment(self, screen) :
        screen.objects.append(self)

class Square(Shape) : # sqaure obejct
    def __init__(self, x:float, y:float, side_length:int, color:str):
        super().__init__(x,y) # set vector
        self.side_length = side_length
        self.color = color

    def draw(self, screen) : # draw a sqaure on a screen
        pygame.draw.rect(screen, self.color, pygame.Rect(self.vector.x, self.vector.y, self.side_length, self.side_length))

class Clear(Sendable) :
    def __init__(self) :
        self.type = 'Clear' # type

    def assignment(self, screen) :
        screen.objects = []