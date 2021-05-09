import pygame
from config import MENU_BG_PATH, LEVEL_BG_PATHS, FONT_PATH


class Renderer:
    """A class to represent renderer object which renders the display.

    Attributes:
        display: Pygame display object.
        width (int): Width of the display.
        height (int): Heigth of the display.
    """

    def __init__(self, display, width, height):
        """Constructs all the necessary attributes for the renderer object.

        Background images will be scaled according to screen size.

        Args:
            display (Display): Pygame display object.
            width (int): Width of the display.
            height (int): Heigth of the display.
        """

        self._display = display
        self.width = width
        self.height = height
        self._big = int(self.height / 10)
        self._extra_small = int(self.height / 30)
        self._menu_image = pygame.image.load(MENU_BG_PATH)
        self._menu_image = pygame.transform.scale(
            self._menu_image, (self.width, self.height))
        self._level_images = []
        for path in LEVEL_BG_PATHS:
            level_image = pygame.image.load(path)
            level_image = pygame.transform.scale(
                level_image, (9 * self.height, int(self.height * 0.8)))
            self._level_images.append(level_image)
        self._level_image_postion = 0

    def render_game(self, level):
        """Renders the display during game loop.

        Fills the display with slowly moving extrawide background image
        with some marginals to the edge.

        Draws all sprites and texts to the screen.
        Creates black vertical borders to the edges of the screen.

        Args:
            level (LevelService): Level service object.
        """

        self._display.fill((0, 0, 0))
        level_image = self._level_images[level.level_number - 1]
        self._display.blit(
            level_image, (self._level_image_postion, self.height / 14))
        self._level_image_postion -= 2
        level.all_sprites.draw(self._display)
        self._draw_text(f"LEVEL {level.level_number}",
                        self._extra_small, self.width / 2 + 3, self.height / 8 + 3, (0, 0, 0))
        self._draw_text(f"PROGRESS: {int(level.progress)}%", self._extra_small,
                        self.width / 2 + 3, self.height / 8 + self._extra_small * 1.2 + 3, (0, 0, 0))
        self._draw_text(f"LEVEL {level.level_number}",
                        self._extra_small, self.width / 2, self.height / 8, (255, 0, 255))
        self._draw_text(f"PROGRESS: {int(level.progress)}%", self._extra_small,
                        self.width / 2, self.height / 8 + self._extra_small * 1.2, (255, 0, 255))
        fill_width = self.width / 12
        rect1 = pygame.Rect(0, 0, fill_width, self.height)
        rect2 = pygame.Rect(self.width - fill_width,
                            0, fill_width, self.height)
        pygame.draw.rect(self._display, (0, 0, 0), rect1)
        pygame.draw.rect(self._display, (0, 0, 0), rect2)
        pygame.display.flip()

    def render_menu(self, title, lines: list):
        """Renders the display during menu screens.

        Fills the display with background image.
        Draw game name and title texts with multiple colors.

        Read the information from each line and draw text according
        to the information.

        Args:
            title (str): Screen title text.
            lines (list): Information which is stored into multiple lines.
        """

        self._display.blit(self._menu_image, (0, 0))
        self._draw_text("THE POSSIBLE GAME", self._big,
                        self.width / 2 + 3, self.height / 5 + 3)
        self._draw_text("THE POSSIBLE GAME", self._big,
                        self.width / 2, self.height / 5, (150, 50, 255))
        self._draw_text(title, self._big, self.width / 2 + 3,
                        self.height / 5 + 3 + (self._big * 1.2))
        self._draw_text(title, self._big, self.width / 2,
                        self.height / 5 + (self._big * 1.2), (0, 200, 0))
        for line in lines:
            if len(line) == 5:
                self._draw_text(line[0], line[1], line[2], line[3], line[4])
            else:
                self._draw_text(line[0], line[1], line[2], line[3])
        pygame.display.flip()

    def _draw_text(self, text, font_size, x_coordinate, y_coordinate, color=(255, 255, 255)):
        """Draws the text according to all necessary attributes.

        Args:
            text (str): Text
            font_size (int): Font size
            x_coordinate (int): Spawn location at the x-axis.
            y_coordinate (int): Spawn location at the y-axis.
            color (tuple, optional): Text color. Defaults to (255, 255, 255).
        """

        font = pygame.font.Font(FONT_PATH, font_size)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect()
        text_rect.center = (x_coordinate, y_coordinate)
        self._display.blit(text_surf, text_rect)

    def reset_game_background_position(self):
        self._level_image_postion = 0
