"""
Luke's Dungeon Crawler - Main entry point
"""
import pygame
import sys
from core.game import Game

def main():
    # Initialize Pygame
    pygame.init()
    
    # Create game instance
    game = Game()
    
    # Main game loop
    running = True
    clock = pygame.time.Clock()
    
    while running:
        dt = clock.tick(60) / 1000.0  # Delta time in seconds
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)
        
        # Update game state
        game.update(dt)
        
        # Render
        game.render()
        
        # Update display
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
