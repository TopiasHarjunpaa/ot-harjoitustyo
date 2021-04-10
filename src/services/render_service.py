import pygame


class RenderService:
    def __init__(self, display, level, background):
        self.display = display
        self._level = level
        self.background = background
        self.width = self._level.width
        self.height = self._level.height

    def render_game(self):
        self.display.fill(self.background)
        self._level.all_sprites.draw(self.display)
        pygame.display.flip()
    
    def render_menu(self, lines: list):
        self.display.fill(self.background)
        for line in lines:
            self.draw_text(line[0], line[1], line[2], line[3])
        pygame.display.flip()
    
    def draw_text(self, text, font_size, x, y):
        font = pygame.font.Font("src/assets/fonts/fontstyle.ttf", font_size)
        text_surf = font.render(text, True, (255, 255, 255))
        text_rect = text_surf.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surf, text_rect)
