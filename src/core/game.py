"""
Core game class - manages game state, entities, and rendering
"""
import pygame
from entities.player import Player
from items.inventory import Inventory

class Game:
    def __init__(self):
        # Screen setup
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Luke's Dungeon Crawler")
        
        # Game state
        self.state = "playing"  # playing, paused, inventory, menu
        
        # Player setup
        self.player = Player(x=400, y=300, race='human')
        
        # Test inventory
        self.inventory_open = False
        
        # Camera offset (for scrolling)
        self.camera_x = 0
        self.camera_y = 0
        
        # Fonts
        self.font = pygame.font.Font(None, 24)
        self.title_font = pygame.font.Font(None, 48)
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i or event.key == pygame.K_TAB:
                self.inventory_open = not self.inventory_open
            elif event.key == pygame.K_ESCAPE:
                if self.inventory_open:
                    self.inventory_open = False
                else:
                    # Pause menu (TODO)
                    pass
    
    def update(self, dt):
        if not self.inventory_open:
            # Update player
            keys = pygame.key.get_pressed()
            self.player.update(dt, keys)
    
    def render(self):
        # Clear screen
        self.screen.fill((20, 20, 30))  # Dark blue background
        
        # Draw grid (debug)
        self.draw_grid()
        
        # Draw player
        self.player.draw(self.screen)
        
        # Draw HUD
        self.draw_hud()
        
        # Draw inventory if open
        if self.inventory_open:
            self.draw_inventory()
    
    def draw_grid(self):
        """Draw a grid for debugging positioning"""
        grid_color = (40, 40, 50)
        for x in range(0, self.screen_width, 64):
            pygame.draw.line(self.screen, grid_color, (x, 0), (x, self.screen_height))
        for y in range(0, self.screen_height, 64):
            pygame.draw.line(self.screen, grid_color, (0, y), (self.screen_width, y))
    
    def draw_hud(self):
        """Draw heads-up display"""
        # HP bar
        hp_text = self.font.render(f"HP: {self.player.hp}/{self.player.max_hp}", True, (255, 255, 255))
        self.screen.blit(hp_text, (10, 10))
        
        # HP bar visual
        bar_width = 200
        bar_height = 20
        hp_percent = self.player.hp / self.player.max_hp
        pygame.draw.rect(self.screen, (100, 100, 100), (10, 35, bar_width, bar_height))
        pygame.draw.rect(self.screen, (255, 50, 50), (10, 35, int(bar_width * hp_percent), bar_height))
        pygame.draw.rect(self.screen, (255, 255, 255), (10, 35, bar_width, bar_height), 2)
        
        # Inventory slots
        inv_text = self.font.render(
            f"Inventory: {self.player.inventory.used_slots()}/{self.player.inventory.max_slots}",
            True, (255, 255, 255)
        )
        self.screen.blit(inv_text, (10, 65))
        
        # Controls hint
        controls_text = self.font.render("WASD: Move | I: Inventory | ESC: Menu", True, (150, 150, 150))
        self.screen.blit(controls_text, (10, self.screen_height - 30))
    
    def draw_inventory(self):
        """Draw inventory screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, 0))
        
        # Inventory panel
        panel_width = 600
        panel_height = 500
        panel_x = (self.screen_width - panel_width) // 2
        panel_y = (self.screen_height - panel_height) // 2
        
        pygame.draw.rect(self.screen, (40, 40, 50), (panel_x, panel_y, panel_width, panel_height))
        pygame.draw.rect(self.screen, (200, 200, 200), (panel_x, panel_y, panel_width, panel_height), 3)
        
        # Title
        title_text = self.title_font.render("Inventory", True, (255, 255, 255))
        self.screen.blit(title_text, (panel_x + 20, panel_y + 20))
        
        # Inventory slots
        slots_text = self.font.render(
            f"Slots Used: {self.player.inventory.used_slots()} / {self.player.inventory.max_slots}",
            True, (255, 255, 255)
        )
        self.screen.blit(slots_text, (panel_x + 20, panel_y + 80))
        
        # List items
        y_offset = 120
        if len(self.player.inventory.items) == 0:
            empty_text = self.font.render("(Empty)", True, (150, 150, 150))
            self.screen.blit(empty_text, (panel_x + 40, panel_y + y_offset))
        else:
            for item in self.player.inventory.items:
                item_text = self.font.render(
                    f"• {item.name} ({item.size} slot{'s' if item.size > 1 else ''})",
                    True, (200, 200, 200)
                )
                self.screen.blit(item_text, (panel_x + 40, panel_y + y_offset))
                y_offset += 30
        
        # Close hint
        close_text = self.font.render("Press I or ESC to close", True, (150, 150, 150))
        self.screen.blit(close_text, (panel_x + 20, panel_y + panel_height - 40))
