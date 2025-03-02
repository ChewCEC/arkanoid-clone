import pygame
from constants import BRICKS_CONST, SCREEN_WIDTH ,SCREEN_HEIGHT, DX_BORDER, DY_BORDER
from brick import Brick 


class GridBrick(pygame.sprite.Sprite):
    def __init__(self, layout):
        self.layout = layout # array[][]
        self.avaliable_height = SCREEN_HEIGHT // 2 
        self.avaliable_width = SCREEN_WIDTH - 20

    def create(self):
        step_x = BRICKS_CONST['width']
        step_y = BRICKS_CONST['height']
        border_x = DX_BORDER
        border_y = DY_BORDER

        # Call pygame.draw.rect with the correct arguments
        # To change the height and width its necessary to reescalate the layout
        # (matrix)
        # + 2 in the loops are the space between bricks
        layout_y = 0       
        for j in range(border_y, self.avaliable_height , step_y + 2):
            layout_x = 0
            for i in range(border_x, self.avaliable_width, step_x + 2):
                if self.layout[layout_y][layout_x]:
                    brick = Brick(i, j)
                layout_x += 1
            layout_y += 1    
