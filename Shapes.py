import pygame

class Shape : # basic shape
    def __init__(self, x, y) -> None:
        self.vector = pygame.Vector2(x, y)

class Square(Shape) : # sqaure
    def __init__(self, x, y, side_length, color):
        super().__init__(x,y)

        self.type = 'Square'
        self.side_length = side_length
        self.color = color
        self.sprite = pygame.Rect(self.vector.x,self.vector.y, side_length,side_length)

    def draw(self, screen) : # draw a sqaure on a screen
        pygame.draw.rect(screen, self.color, self.sprite)