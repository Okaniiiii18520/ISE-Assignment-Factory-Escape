import pygame
import os


class MainMenu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Load assets
        asset_path = 'main_menu'
        self.title = pygame.image.load(os.path.join(asset_path, 'menu_title.png')).convert_alpha()
        self.start_btn = pygame.image.load(os.path.join(asset_path, 'button_start.png')).convert_alpha()
        self.quit_btn = pygame.image.load(os.path.join(asset_path, 'button_quit.png')).convert_alpha()
        
        self.start_btn = pygame.transform.scale(self.start_btn, (int(self.screen_width * 0.25), int(self.screen_height * 0.125)))
        self.quit_btn = pygame.transform.scale(self.quit_btn, (int(self.screen_width * 0.25), int(self.screen_height * 0.125)))

        # Position elements
        self.title_rect = self.title.get_rect(center=(screen_width // 2, screen_height // 3))
        self.start_rect = self.start_btn.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        self.quit_rect = self.quit_btn.get_rect(center=(screen_width // 2, screen_height // 2 + 170))
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_rect.collidepoint(event.pos):
                return 'start'
            elif self.quit_rect.collidepoint(event.pos):
                return 'quit'
        return None
    
    def draw(self, screen):
        screen.fill((50, 50, 80))
        screen.blit(self.title, self.title_rect)
        screen.blit(self.start_btn, self.start_rect)
        screen.blit(self.quit_btn, self.quit_rect)
