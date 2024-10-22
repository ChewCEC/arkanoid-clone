import pygame
from constants import BRICKS_CONST



class GridBrick():
    def __init__(self, layout):
        self.layout = layout # array[][]
        self.screen = 

    def draw(self):
        # Call pygame.draw.rect with the correct arguments
        for row in self.layout:
            for box in row:
                if box:
                    
                    
        
        pygame.draw.rect(self.screen, self.color, self.rectangle())
    