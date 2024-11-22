import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_CONST, BALL_CONST
from player import Player
from ball import Ball
from brick import Brick
from gridbrick import GridBrick
import constants
from dotenv import load_dotenv
  
def main():
    GRAY_COLOR = (128, 128, 128, 150)
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
    collisionable = pygame.sprite.Group()
    
    # Asigning containers 
    Player.containers = (updatable, drawable)
    Ball.containers = (updatable, drawable)
    Brick.containers = (drawable, collisionable)

    player = Player(player_x, player_y)
    ball = Ball(player_x, player_y - 19, BALL_CONST['radius'])
    ball.velocity += pygame.Vector2(1,-1)
    create_brick_grid = GridBrick(constants.LEVELS[level_number]) 
    # generate brick grid
    create_brick_grid.create()     

    def initialVaribles():
        global level_number, points, lives
        level_number = 0
        points = 0 
        lives = 3
    
    def restartGame():
        player.position.x, player.position.y = [player_x, player_y]
        ball.position.x, ball.position.y = [player_x, player_y - 10] 
        
        # reset brick grid
        for obj_coll in collisionable:
            obj_coll.kill()
            
        create_brick_grid = GridBrick(constants.LEVELS[0]) 
        create_brick_grid.create()
        initialVaribles()
     
    def restartLevel():
        # reset players position
        player.position.x, player.position.y = [player_x, player_y]
        ball.position.x, ball.position.y = [player_x, player_y - 10] 
        
        # reset brick grid
        for obj_coll in collisionable:
            obj_coll.kill()
        create_brick_grid.create()
        
        # reset player stats
        points = 0
        lives = 3
        pause = False
    
    def nextLevel(level_number):
        if level_number < len(constants.LEVELS): 
            # reset players position
            player.position.x, player.position.y = [player_x, player_y]
            ball.position.x, ball.position.y = [player_x, player_y - 10] 
            # reset player stats
            points = 0
            lives = 3
            pause = False
            create_brick_grid = GridBrick(constants.LEVELS[level_number]) 
            create_brick_grid.create()
        else:
            drawWin()     
    
    # Creating player's score
   
    scoreText = pygame.font.Font('freesansbold.ttf', 28)
    def showScore():
        scoreSurface = scoreText.render(f"Score: {str(points)}", True, 'red')
        screen.blit(scoreSurface, (20, SCREEN_HEIGHT-50))
    
    # Creating players lives
    # unistr = "❤️"
    livesText = pygame.font.Font("freesansbold.ttf", 28)  # Use the default font with size 28
    def showLives():
        # Render and display each life (heart)
        livesSurface = livesText.render(f"Lives: {lives}", True, 'red')  # Render the heart in red
        screen.blit(livesSurface, (20, SCREEN_HEIGHT - 90))  # Adjust position for each life

    # [TODO] finish funciton
    def drawWin():
        font = pygame.font.Font(None, 36)
        pygame.draw.rect(surface, GRAY_COLOR, [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])
        
        # Render text
        pause_text = font.render('Game paused: Press escape to resume', True, BLACK_COLOR)
        restart_text = font.render('Restart', True, BLACK_COLOR)
        
        # Blit text onto screen
        surface.blit(pause_text, (SCREEN_WIDTH // 4 + 20, SCREEN_HEIGHT // 4 + 10))
        surface.blit(restart_text, (SCREEN_WIDTH // 4 + 90, SCREEN_HEIGHT // 4 + 80))
        screen.blit(surface, (0, 0))
        pygame.display.update()
        return reset_rect
        
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
    
    def lostLife():
        player.position.x, player.position.y = [player_x, player_y]
        ball.position.x, ball.position.y = [player_x, player_y - 10] 
        
        

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
                    restartLevel()
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

            if ball.position.y > SCREEN_HEIGHT + 20:
                lives -= 1
                if lives < 1:
                    restartGame()

                lostLife()
                
            ball.check_collision(player.rectangle())
            ball.check_collision_walls()
            showScore()
            showLives()
            
            if len(collisionable) == 0:
                points = 0
                level_number += 1
                nextLevel(level_number)

        pygame.display.flip()
        dt = delta_time.tick(144)/1000


    pygame.quit()
    
        
if __name__ == "__main__":
    main()
