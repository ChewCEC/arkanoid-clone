import pygame
import constants

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, BALL_CONST
from player import Player
from ball import Ball
from brick import Brick
from gridbrick import GridBrick
from game_state import GameState


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

    # Creating objects game
    game_state = GameState()
    player = Player(player_x, player_y)
    ball = Ball(player_x, player_y - 19, BALL_CONST['radius'])
    ball.velocity += pygame.Vector2(1,-1)
    create_brick_grid = GridBrick(constants.LEVELS[game_state.level_number])
    
    # generate brick grid
    create_brick_grid.create()

    
    def restartGame():
        game_state.restartState()
        resetPlayerPosition()
        
        # reset brick grid
        for obj_coll in collisionable:
            obj_coll.kill()
            
        create_brick_grid = GridBrick(constants.LEVELS[0]) 
        create_brick_grid.create()
      
     
    def restartLevel():
        # reset players position
        resetPlayerPosition() 
        
        # reset brick grid
        for obj_coll in collisionable:
            obj_coll.kill()
        create_brick_grid.create()
        
    def nextLevel():
        if game_state.level_number < len(constants.LEVELS):
            game_state.nextLevel()
            # reset players position
            resetPlayerPosition()
            create_brick_grid = GridBrick(constants.LEVELS[game_state.level_number]) 
            create_brick_grid.create()
            
        else:
            drawWin()  
    
    
    def resetPlayerPosition():
        player.position.x, player.position.y = [player_x, player_y]
        ball.position.x, ball.position.y = [player_x, player_y - 10]
    
    
    score_text = pygame.font.Font('freesansbold.ttf', 28)
    def showScore():
        score_surface = score_text.render(f"Score: {str(game_state.points)}", True, 'red')
        screen.blit(score_surface, (20, SCREEN_HEIGHT-50))
    
    # Creating players lives
    # unistr = "❤️"
    lives_text = pygame.font.Font("freesansbold.ttf", 28)  # Use the default font with size 28
    def showLives():
        # Render and display each life (heart)
        lives_surface = lives_text.render(f"Lives: {game_state.lives}", True, 'red')  # Render the heart in red
        screen.blit(lives_surface, (20, SCREEN_HEIGHT - 90))  # Adjust position for each life

    def drawPause():
        font = pygame.font.Font("freesansbold.ttf", 36)
        pygame.draw.rect(surface, GRAY_COLOR, [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])
        
        # Pause message box
        reset_rect = pygame.draw.rect(surface, WHITE_COLOR, 
                                    [SCREEN_WIDTH // 4 + 90, SCREEN_HEIGHT // 4 + 70, 280, 50], 0, 10)
        
        # Render text
        pause_text = font.render('Game paused:\nPress escape to resume', True, BLACK_COLOR)
        restart_text = font.render('Restart', True, BLACK_COLOR)
        
        # Blit text onto screen
        surface.blit(pause_text, (SCREEN_WIDTH // 4 + 20, SCREEN_HEIGHT // 4 + 10))
        surface.blit(restart_text, (SCREEN_WIDTH // 4 + 90, SCREEN_HEIGHT // 4 + 80))
        screen.blit(surface, (0, 0))
        pygame.display.update()
        return reset_rect 
     
    # [TODO] Fixing the displaying of the white box
    # [TODO] Make New Game after [enter] is pressed 
    def drawWin():
        font = pygame.font.Font("freesansbold.ttf", 32)
        pygame.draw.rect(surface, GRAY_COLOR, [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])
        # Pause message box
        win_rect = pygame.draw.rect(surface, WHITE_COLOR, 
                                    [SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3, 280], 0, 10)
        
        win_text = font.render('YOU WIN!', True, BLACK_COLOR)
        new_game_text = font.render('Press [enter] to start a new game', True, BLACK_COLOR)
        
        surface.blit(win_text, (SCREEN_WIDTH // 4 + 90, SCREEN_HEIGHT // 4 + 70))
        surface.blit(new_game_text, (SCREEN_WIDTH // 4 + 90, SCREEN_HEIGHT // 4 + 100))
        
        screen.blit(surface, (0, 0))
        
        pygame.display.update()
        return win_rect    

    running = True
    game_state.pause = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_state.pause = not game_state.pause
                    reset_rect = drawPause()
            if event.type == pygame.MOUSEBUTTONDOWN and game_state.pause:
                if reset_rect.collidepoint(event.pos):
                    restartLevel()
                    game_state.pause = False  # Unpause the game after restarting 
                    
        if not game_state.pause:
            
            for obj_upt in updatable:
                obj_upt.update(dt)
            
            screen.fill("black")
                    
            for obj_draw in drawable:
                obj_draw.draw(screen)
            
            for obj_coll in collisionable:
                if ball.checkCollision(obj_coll.rectangle()):
                    obj_coll.kill()
                    game_state.points += 100   

            if ball.position.y > SCREEN_HEIGHT + 20:
                game_state.lives -= 1
                if game_state.lives < 1:
                    restartGame()

                resetPlayerPosition()
                
            ball.checkCollision(player.rectangle())
            ball.checkCollisionWalls()
            showScore()
            showLives()
            
            # if game_state.points == 100:
            #     game_state.pause = not game_state.pause  
            #     drawWin()
            
            if len(collisionable) == 0:
                nextLevel()

        pygame.display.flip()
        dt = delta_time.tick(144)/1000


    pygame.quit()
    
        
if __name__ == "__main__":
    main()
