import pygame
from config import BG_PATH, BG_PATH2, FONT_PATH


class Renderer:
    """A class to represent renderer object which renders the display.

    Attributes:
        display: Pygame display object.
        width (int): Width of the display.
        heigth (int): Heigth of the display.
    """

    def __init__(self, display, width, height):
        """Constructs all the necessary attributes for the renderer object.

        Args:
            display (Display): Pygame display object.
            width (int): Width of the display.
            height (int): Heigth of the display.
        """

        self.display = display
        self.bg_color = ()
        self.bg_image = pygame.image.load(BG_PATH)

        # Game background testing begins.
        self.bg_i = pygame.image.load(BG_PATH2)
        self.bg_i = pygame.transform.scale(self.bg_i, (12 * height, height))
        self.pic_loc = 0
        # Game background testing ends.

        self.width = width
        self.height = height
        self.big = int(self.height / 10)
        self.extra_small = int(self.height / 30)

    def render_game(self, level):
        """Renders the display during game loop.

        Fills the display with black background
        TODO: Fills the display with background image.

        Draws all sprites and texts to the screen.
        Creates black vertical borders to the edges of the screen.

        Args:
            level (LevelService): Level service object.
        """

        # Game background testing begins.
        self.display.blit(self.bg_i, (self.pic_loc, 0))
        self.pic_loc -= 3
        #self.display.fill((0, 0, 0))
        rect3 = pygame.Rect(0, self.height / 12 * 9, self.width, self.height)
        pygame.draw.rect(self.display, (0, 0, 0), rect3)
        # Game background testing ends.

        level.all_sprites.draw(self.display)
        self.draw_text(f"LEVEL {level.level_number}",
                       self.extra_small, self.width / 2, self.height / 8)
        self.draw_text(f"PROGRESS: {int(level.progress)}%", self.extra_small,
                       self.width / 2, self.height / 8 + self.extra_small * 1.2)
        fill_width = self.width / 10
        rect1 = pygame.Rect(0, 0, fill_width, self.height)
        rect2 = pygame.Rect(self.width - fill_width,
                            0, fill_width, self.height)
        pygame.draw.rect(self.display, (0, 0, 0), rect1)
        pygame.draw.rect(self.display, (0, 0, 0), rect2)
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
        self.display.blit(text_surf, text_rect)
