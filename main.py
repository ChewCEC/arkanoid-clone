import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_CONST, BALL_CONST
from player import Player
from ball import Ball
from brick import Brick
from gridbrick import GridBrick
import constants

def main():
    GRAY_COLOR = (128, 128, 128, 150)
    DARK_GRAY_COLOR = 'dark gray'
    WHITE_COLOR = "white"
    BLACK_COLOR = "black"
    
    pygame.init()
    delta_time = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))     
    surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT - 50
    # Creating two containers updatable and drawable
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    block_grid = pygame.sprite.Group()
    collisionable = pygame.sprite.Group()
    
    # Asigning containers 
    Player.containers = (updatable, drawable)
    Ball.containers = (updatable, drawable)
    Brick.containers = (drawable, collisionable)

    player = Player(player_x, player_y)
    ball = Ball(player_x, player_y - 10, BALL_CONST['RADIUS'])
    ball.velocity += pygame.Vector2(1,-2)
    create_brick_grid = GridBrick(constants.LEVELS[4]) 
    # generate brick grid
    create_brick_grid.create()     

    # Creating player's score
   
    def restartGame():
        # reset players position
        player.position.x, player.position.y = [player_x, player_y]
        ball.position.x, ball.position.y = [player_x, player_y - 10] 
        
        # reset brick grid
        for obj_coll in collisionable:
            obj_coll.kill()
        create_brick_grid.create()
        
        # reset player stats
        points = 0
        print(points)
        lives = 3
        pause = False
    
    points = 0    
    scoreText = pygame.font.Font('freesansbold.ttf', 28)
    def showScore():
        scoreSurface = scoreText.render(f"Score: {str(points)}", True, 'red')
        screen.blit(scoreSurface, (20, SCREEN_HEIGHT-50))

    # Creating players lives
    lives = 3  # Example: 3 lives
    # unistr = "❤️"
    livesText = pygame.font.Font("freesansbold.ttf", 28)  # Use the default font with size 28
    def showLives():
        # Render and display each life (heart)
        livesSurface = livesText.render(f"Lives: {lives}", True, 'red')  # Render the heart in red
        screen.blit(livesSurface, (20, SCREEN_HEIGHT - 90))  # Adjust position for each life

    def drawPause():
        
        font = pygame.font.Font(None, 36)
        pygame.draw.rect(surface, GRAY_COLOR, [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])
        
        # Pause message box
        reset_rect = pygame.draw.rect(surface, WHITE_COLOR, 
                                    [SCREEN_WIDTH // 4 + 90, SCREEN_HEIGHT // 4 + 70, 280, 50], 0, 10)
        
        # Render text
        pause_text = font.render('Game paused: Press escape to resume', True, BLACK_COLOR)
        restart_text = font.render('Restart', True, BLACK_COLOR)
        
        # Blit text onto screen
        surface.blit(pause_text, (SCREEN_WIDTH // 4 + 20, SCREEN_HEIGHT // 4 + 10))
        surface.blit(restart_text, (SCREEN_WIDTH // 4 + 90, SCREEN_HEIGHT // 4 + 80))
        screen.blit(surface, (0, 0))
        pygame.display.update()
        return reset_rect 
        
    running = True
    pause = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pause = not pause
                    reset_rect = drawPause()
            if event.type == pygame.MOUSEBUTTONDOWN and pause:
                if reset_rect.collidepoint(event.pos):
                    restartGame()
                    points = 0

                    pause = False  # Unpause the game after restarting 
        if not pause:    
            for obj_upt in updatable:
                obj_upt.update(dt)
            
            screen.fill("black")
                    
            for obj_draw in drawable:
                obj_draw.draw(screen)
            
            for obj_coll in collisionable:
                if ball.check_collision(obj_coll.rectangle()):
                    obj_coll.kill()
                    points += 100   

            ball.check_collision_walls()
            ball.check_collision(player.rectangle())
    
            showScore()
            showLives()

        pygame.display.flip()
        dt = delta_time.tick(144)/1000


    pygame.quit()
    
        
if __name__ == "__main__":
    main()
