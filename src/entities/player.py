"""
Player entity class
"""
import pygame
from items.inventory import Inventory

# Race stats (from design doc)
RACE_STATS = {
    'human': {'hp': 100, 'speed': 5.0, 'inventory_slots': 10, 'stamina': 100},
    'elf': {'hp': 80, 'speed': 6.0, 'inventory_slots': 8, 'stamina': 120},
    'dwarf': {'hp': 130, 'speed': 4.0, 'inventory_slots': 12, 'stamina': 80},
    'golemkin': {'hp': 180, 'speed': 3.5, 'inventory_slots': 15, 'stamina': 60},
    'umbral': {'hp': 70, 'speed': 5.5, 'inventory_slots': 9, 'stamina': 110}
}

class Player:
    def __init__(self, x, y, race='human'):
        self.x = x
        self.y = y
        self.race = race
        
        # Get race stats
        stats = RACE_STATS[race]
        self.max_hp = stats['hp']
        self.hp = self.max_hp
        self.speed = stats['speed'] * 50  # Scale for pixel movement
        self.max_stamina = stats['stamina']
        self.stamina = self.max_stamina
        
        # Inventory
        self.inventory = Inventory(max_slots=stats['inventory_slots'])
        
        # Visual
        self.width = 32
        self.height = 32
        self.color = (100, 200, 255)  # Light blue
        
        # Movement
        self.velocity_x = 0
        self.velocity_y = 0
    
    def update(self, dt, keys):
        """Update player state"""
        # Movement
        self.velocity_x = 0
        self.velocity_y = 0
        
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.velocity_y = -self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.velocity_y = self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed
        
        # Normalize diagonal movement
        if self.velocity_x != 0 and self.velocity_y != 0:
            self.velocity_x *= 0.707  # 1/sqrt(2)
            self.velocity_y *= 0.707
        
        # Apply movement
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
    
    def draw(self, screen):
        """Draw player"""
        # Draw shadow
        shadow_rect = pygame.Rect(
            int(self.x - self.width // 2 + 2),
            int(self.y - self.height // 2 + self.height - 4),
            self.width - 4,
            8
        )
        pygame.draw.ellipse(screen, (0, 0, 0, 100), shadow_rect)
        
        # Draw player body
        player_rect = pygame.Rect(
            int(self.x - self.width // 2),
            int(self.y - self.height // 2),
            self.width,
            self.height
        )
        pygame.draw.rect(screen, self.color, player_rect)
        pygame.draw.rect(screen, (255, 255, 255), player_rect, 2)
        
        # Draw direction indicator (simple dot)
        indicator_x = int(self.x)
        indicator_y = int(self.y - self.height // 4)
        pygame.draw.circle(screen, (255, 255, 255), (indicator_x, indicator_y), 3)
