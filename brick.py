import pygame   
from squareshape import SquareShape
from constants import BRICKS_CONST
from random import randint 

class Brick(SquareShape):
    def __init__(self, x, y ):
        super().__init__(x, y, BRICKS_CONST['width'], BRICKS_CONST['height'])
        self.color = self.randomColor()

    def rectangle(self):
        # Create and return a pygame.Rect object based on the player's position and size
        return pygame.Rect(self.position.x, self.position.y, self.height, self.width)

    def draw(self, screen):
        # Call pygame.draw.rect with the correct arguments
        pygame.draw.rect(screen, self.color, self.rectangle())
    

    def randomColor(self):
        return (randint(1,255), randint(1,255), randint(1,255))      
 
        
