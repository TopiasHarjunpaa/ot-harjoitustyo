import pygame


class RenderService:
    def __init__(self, display, level, background):
        self.display = display
        self._level = level
        self.background = background
        self.width = self._level.width
        self.height = self._level.height
        self.big = int(self.height / 10)

    def render_game(self):
        self.display.fill(self.background)
        self._level.all_sprites.draw(self.display)
        pygame.display.flip()

    def render_menu(self, title, lines: list):
        self.display.fill(self.background)
        self.draw_text("THE POSSIBLE GAME", self.big,
                       self.width / 2 + 3, self.height / 5 + 3)
        self.draw_text("THE POSSIBLE GAME", self.big,
                       self.width / 2, self.height / 5, (150, 50, 255))
        self.draw_text(title, self.big, self.width / 2 + 3,
                       self.height / 5 + 3 + (self.big * 1.2))
        self.draw_text(title, self.big, self.width / 2,
                       self.height / 5 + (self.big * 1.2), (0, 200, 0))
        for line in lines:
            if len(line) == 5:
                self.draw_text(line[0], line[1], line[2], line[3], line[4])
            else:
                self.draw_text(line[0], line[1], line[2], line[3])
        pygame.display.flip()

    def draw_text(self, text, font_size, x, y, color=(255, 255, 255)):
        font = pygame.font.Font("src/assets/fonts/fontstyle.ttf", font_size)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surf, text_rect)
