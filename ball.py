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
        self.position += self.velocity * dt * BALL_CONST["speed"]
    
    
    def check_collision(self, square):
        # Find the closest point on the rectangle to the center of the self
        closest_x = max(square.left, min(self.position.x, square.right))
        closest_y = max(square.top, min(self.position.y, square.bottom))

        # Calculate the distance between the ball's center and this closest point
        distance_x = self.position.x - closest_x
        distance_y = self.position.y - closest_y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        # Check if collision happened
        if distance <= self.radius:
            # Create a vector for the collision normal
            collision_normal = pygame.Vector2(distance_x, distance_y)

            # Only reflect if the collision normal is non-zero
            if collision_normal.length() != 0:
                collision_normal = collision_normal.normalize()
                self.velocity = self.velocity.reflect(collision_normal)
            else:
                # If the normal is zero, fall back to a basic velocity reversal
                self.velocity.x = -self.velocity.x
                self.velocity.y = -self.velocity.y
                
            return True

    def check_collision_walls(self):
        if self.position.x < DX_BORDER or self.position.x > SCREEN_WIDTH - DX_BORDER:
            self.velocity.x = -self.velocity.x
            
        if self.position.y < DX_BORDER - 5: 
            self.velocity.y = -self.velocity.y
        
  
        
