import pygame

class Square :
    def __init__(self, x, y, side_length, color):
        self.side_length = side_length
        self.color = color
        self.vector = pygame.Vector2(x, y)
        self.sprite = pygame.Rect(self.vector.x,self.vector.y, side_length,side_length)

    def draw(self, screen) :
        pygame.draw.rect(screen, self.color, self.sprite)