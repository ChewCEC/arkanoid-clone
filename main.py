import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_CONST 
from player import Player
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

    # Asigning containers 
    Player.container = (updatable, drawable)
    
    player = Player(COORD_X, COORD_Y)

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
        player.update(dt)
        player.draw(screen)
        
        pygame.display.flip()
        dt = delta_time.tick(144)/1000
        
    
    
    pygame.quit()
    
        
if __name__ == "__main__":
    main()