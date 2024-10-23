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
 
        layout_y = 0       
        for j in range(border_y, self.avaliable_height , 59 + 2):
            layout_x = 0
            for i in range(border_x, self.avaliable_width, 87 + 2):
                print(layout_y, layout_x )
                if self.layout[layout_y][layout_x]:
                    brick = Brick(i, j)
                layout_x += 1
            layout_y += 1    
