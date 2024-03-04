import pygame

class Circle :
    def __init__(self, x, y, side_length, color):
        self.side_length = side_length
        self.color = color
        self.vector = pygame.Vector2(x, y)

    def draw(self, screen) :
        self.sprite = pygame.Rect(self.vector.x,self.vector.y, self.side_length, self.side_length)
        pygame.draw.rect(screen, self.color, self.sprite)