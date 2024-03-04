import pygame

class Screen :
    def __init__(self) :
        self.objects = []

        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.dt = 0

    def addObject(self, object) :
        self.objects.append(object)

    def frame(self) :
        self._drawObjects()

        # show and loop
        pygame.display.flip()
        self.dt = self.clock.tick(60) / 1000

    def _drawObjects(self) :
        self.screen.fill("white") # reset screen
        for object in self.objects :
            object.draw(self.screen)