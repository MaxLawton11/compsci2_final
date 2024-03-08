import pygame



class Shape : # basic shape
    def __init__(self, x, y) :
        self.vector = pygame.Vector2(x, y) # pos of shape
        self.type = 'Shape' # type

class Square(Shape) : # sqaure obejct
    def __init__(self, x, y, side_length, color):
        super().__init__(x,y) # set vector
        self.side_length = side_length
        self.color = color
        self.sprite = pygame.Rect(self.vector.x,self.vector.y, side_length,side_length) # make sprite (a square)

    def draw(self, screen) : # draw a sqaure on a screen
        pygame.draw.rect(screen, self.color, self.sprite)

class Clear :
    def __init__(self) :
        self.type = Shape