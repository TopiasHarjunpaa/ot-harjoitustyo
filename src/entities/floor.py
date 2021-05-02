import pygame


class Floor(pygame.sprite.Sprite):
    """A class to represent floor object at the game level.

    Attributes:
        level: Level object
        x_coordinate: Spawn location at the x-axis.
        y_coordinate: Spawn location at the y-axis.
        width: Width of the floor object.
        heigth: Heigth of the floor object.
        floor_type: Type of the floor (normal floor, lava or goal)
    """

    def __init__(self, level, x_coordinate, y_coordinate, width, height, floor_type):
        """Constructs all the necessary attributes for the floor object.

        Args:
            level (Level): Level object
            x_coordinate (int): Spawn location at the x-axis.
            y_coordinate (int): Spawn location at the y-axis.
            width (int): Width of the floor object.
            height (int): Heigth of the floor object.
            floor_type (str): Type of the floor (normal floor, lava or goal)
        """

        super().__init__()
        self.level = level
        self.floor_type = floor_type
        self.image = pygame.Surface(
            (width, height), pygame.SRCALPHA)
        self.visualize(width, height)
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate

    def update(self):
        """Updates location of the floor object which depends from the speed of level.

        Floor object will be deleted once it has moved outside of the screen.
        """

        self.rect.x -= self.level.speed
        if self.rect.right < 0:
            self.kill()

    def visualize(self, width, height):
        """Creates visualization for the floor object.

        Each of the floor type has different colors.

        Args:
            width (int): Width of the floor object.
            height (int): Heigth of the floor object.
        """

        if self.floor_type == "f":
            color1 = (255, 255, 255)
            color2 = (178, 34, 34)
        if self.floor_type == "l":
            color1 = (178, 34, 34)
            color2 = (0, 0, 0)
        if self.floor_type == "g":
            color1 = (255, 255, 255)
            color2 = (0, 255, 0)

        pygame.draw.rect(self.image, (color1), (0, 0, width, height))
        pygame.draw.rect(self.image, (color2),
                         (2, 2, width - 4, height - 4))
