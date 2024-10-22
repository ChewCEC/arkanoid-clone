import pygame, math
from constants import BALL_CONST, SCREEN_WIDTH, SCREEN_HEIGHT, DX_BORDER

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            center = self.position, 
            color = "white", 
            radius = self.radius, 
            width = 1 
            )
        

    def update(self, dt):
        self.position += self.velocity * dt * BALL_CONST["SPEED"]
    
    
    def check_collision(self, square):
        # Find the closest point on the rectangle to the center of the self
        closest_x = max(square.left, min(self.position.x, square.right))
        closest_y = max(square.top, min(self.position.y, square.bottom))

        # Calculate the distance between the self's center and this closest point
        distance_x = self.position.x - closest_x
        distance_y = self.position.y - closest_y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        left_right = (self.position.x < square.left or self.position.x > square.right)
        top_bottom = (self.position.y < square.top or self.position.y > square.bottom)

        # If the distance is less than or equal to the self's radius, there's a collision
        if distance <= self.radius:
            if left_right:
                print("collsion left right")
                self.velocity.x = -self.velocity.x

            if top_bottom:
                print("collsion top bottom")
                self.velocity.y = -self.velocity.y
        print("No collision")
        return False

    def check_collision_walls(self):
        if self.position.x < DX_BORDER or self.position.x > SCREEN_WIDTH - DX_BORDER:
            self.velocity.x = -self.velocity.x
            
        if self.position.y < DX_BORDER - 5 or self.position.y > SCREEN_HEIGHT: 
            self.velocity.y = -self.velocity.y
        
        
