import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_CONST, BALL_CONST
from player import Player
from ball import Ball
from brick import Brick
from gridbrick import GridBrick
import constants

def main():
    pygame.init()
    delta_time = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 

    
    COORD_X = SCREEN_WIDTH / 2
    COORD_Y = SCREEN_HEIGHT - 50
    # Creating two containers updatable and drawable
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    block_grid = pygame.sprite.Group()
    collisionable = pygame.sprite.Group()
    

    # Asigning containers 
    Player.containers = (updatable, drawable)
    Ball.containers = (updatable, drawable)
    Brick.containers = (drawable, collisionable)

    player = Player(COORD_X, COORD_Y)
    ball = Ball(COORD_X, COORD_Y - 10, BALL_CONST['RADIUS'])
    ball.velocity += pygame.Vector2(1,-2)
    singleBrick = Brick(100, 100)
    create_brick_grid = GridBrick(constants.LEVELS[0]) 
    


    create_brick_grid.create()        
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        
        for obj_upt in updatable:
            obj_upt.update(dt)
        
        screen.fill("black")
                
        for obj_draw in drawable:
            obj_draw.draw(screen)
        
        for obj_coll in collisionable:
            if ball.check_collision(obj_coll.rectangle()):
               obj_coll.kill() 

        ball.check_collision_walls()
        ball.check_collision(player.rectangle())
        pygame.display.flip()
        dt = delta_time.tick(144)/1000
        
    
    pygame.quit()
    
        
if __name__ == "__main__":
    main()
