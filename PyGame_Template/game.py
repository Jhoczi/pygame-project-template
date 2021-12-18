import pygame
from Helpers.extensions import Extensions

class Game:
    def __init__(self):
        pygame.init()
        #SETTINGS:
        self.SCREEN_WIDTH = 840
        self.SCREEN_HEIGHT = 620
        self.run = False
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.COLORS = Extensions().COLORS
    def Event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
    def Update(self):
        pygame.display.update()
    def Render(self):
        self.screen.fill(self.COLORS["BLACK"])
    def Run(self):
        self.run = True
        while self.run:
            # Event
            self.Event()
            # Update
            self.Update()
            # Render
            self.Render()

            self.clock.tick(self.FPS)
        pygame.quit()