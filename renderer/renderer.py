# Handles all graphics using PyGame 
# Draws bodies on the screen with positions from Body objects
# Controls FPS for smooth animation

import pygame

class Renderer:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height

    def draw(self, bodies):
        self.screen.fill((0, 0, 0))  # Black background
        for body in bodies:
            x, y = int(body.pos[0]), int(body.pos[1])
            pygame.draw.circle(self.screen, (255, 255, 255), (x, y), max(2, int(body.mass**0.33)))
        pygame.display.flip()
        self.clock.tick(60)  # 60 FPS
