import pygame
from constants import PLAYER_CONST
from squareshape import SquareShape

class Player(SquareShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_CONST["WIDTH"], PLAYER_CONST["HEIGHT"],)
        self.powerUp = []
    
    def rectangle(self):
        # Create and return a pygame.Rect object based on the player's position and size
        return pygame.Rect(self.position.x, self.position.y, self.height, self.width)
    
    def draw(self, screen):
        # Call pygame.draw.rect with the correct arguments
        pygame.draw.rect(screen, "white", self.rectangle())
    
    def move(self, dt):
        forward = pygame.Vector2(1, 0)
        self.position += forward * PLAYER_CONST["SPEED"] * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        # move left or right
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.move(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.move(dt)

