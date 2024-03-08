import pygame

class Sendable :
    def __init__(self) :
        self.type = None

class Shape(Sendable) : # basic shape
    def __init__(self, x, y) :
        super().__init__()
        self.vector = pygame.Vector2(x, y) # pos of shape
        self.type = 'Shape' # type

    def assignment(self, screen) :
        screen.objects.append(self)

class Square(Shape) : # sqaure obejct
    def __init__(self, x, y, side_length, color):
        super().__init__(x,y) # set vector
        self.side_length = side_length
        self.color = color

    def draw(self, screen) : # draw a sqaure on a screen
        pygame.draw.rect(screen, self.color, pygame.Rect(self.vector.x, self.vector.y, self.side_length, self.side_length))

class Clear(Sendable) : # a cmd to clear a screen
    def __init__(self) :
        super().__init__()
        self.type = 'Clear' # type

    def assignment(self, screen) : # clear when run
        screen.objects = []

class ChangeGBColor(Sendable) : # a cmd to change bg color
    def __init__(self, color) :
        super().__init__()
        self.type = 'BGColor' # type
        self.color = color

    def assignment(self, screen) : # change colot to stored color
        screen.color = self.color