import pygame
from config import BG_PATH, FONT_PATH


class Renderer:
    def __init__(self, display, width, height):
        self.display = display
        self.bg_color = ()
        self.bg_image = pygame.image.load(BG_PATH)
        self.width = width
        self.height = height
        self.big = int(self.height / 10)
        self.extra_small = int(self.height / 30)

    def render_game(self, level):
        #self.display.blit(self.bg_image, (0, 0))
        self.display.fill((0, 0, 0))
        level.all_sprites.draw(self.display)
        self.draw_text(f"LEVEL {level.level_number}",
                       self.extra_small, self.width / 2, self.height / 8)
        self.draw_text(f"PROGRESS: {int(level.progress)}%", self.extra_small,
                       self.width / 2, self.height / 8 + self.extra_small * 1.2)
        # Just testing...
        fill_width = self.width / 10
        rect1 = pygame.Rect(0, 0, fill_width, self.height)
        rect2 = pygame.Rect(self.width - fill_width,
                            0, fill_width, self.height)
        pygame.draw.rect(self.display, (0, 0, 0), rect1)
        pygame.draw.rect(self.display, (0, 0, 0), rect2)
        # Testing ends...
        pygame.display.flip()

    def render_menu(self, title, lines: list):
        self.display.blit(self.bg_image, (0, 0))
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

    def draw_text(self, text, font_size, x_coordinate, y_coordinate, color=(255, 255, 255)):
        font = pygame.font.Font(FONT_PATH, font_size)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect()
        text_rect.center = (x_coordinate, y_coordinate)
        self.display.blit(text_surf, text_rect)
