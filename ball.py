import pygame
from constants import BALL_CONST

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            center = self.position, 
            color = "white", 
            radius = self.radius, 
            width = 1 
            )


    def update(self, dt):
        self.position += self.velocity * dt * BALL_CONST["SPEED"]
        