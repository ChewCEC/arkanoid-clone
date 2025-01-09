class GameState:
    def __init__(self):
        self.level_number = 0
        self.points = 0
        self.lives = 3
        self.pause = False

    def restartState(self):
        """Reset the game state to the initial values."""
        self.level_number = 0
        self.points = 0
        self.lives = 3
        self.pause = False

    def nextLevel(self):
        """Advance to the next level."""
        self.level_number += 1

        
