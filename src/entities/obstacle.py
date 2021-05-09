import pygame


class Obstacle(pygame.sprite.Sprite):
    """A class to represent obstacle object at the game level.

    Attributes:
        level: Level object
        x_coordinate: Spawn location at the x-axis.
        y_coordinate: Spawn location at the y-axis.
        width: Width of the obstacle object.
        heigth: Heigth of the obstacle object.
    """

    def __init__(self, level, x_coordinate, y_coordinate, width, height):
        """Constructs all the necessary attributes for the obstacle object.

        Args:
            level (Level): Level object
            x_coordinate (int): Spawn location at the x-axis.
            y_coordinate (int): Spawn location at the y-axis.
            width (int): Width of the obstacle object.
            height (int): Heigth of the obstacle object.
        """

        super().__init__()
        self._level = level
        self.image = pygame.Surface(
            (width, height), pygame.SRCALPHA)
        self._visualize(width, height)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x_coordinate, y_coordinate)

    def update(self):
        """Updates location of the obstacle object which depends from the speed of level.

        Obstacle object will be deleted once it has moved outside of the screen.
        """
        self.rect.x -= self._level.speed
        if self.rect.right < 0:
            self.kill()

    def _visualize(self, width, height):
        """Creates visualization for the obstacle object.

        Obstacle object has blue color with black borders.

        Args:
            width (int): Width of the obstacle object.
            height (int): Heigth of the obstacle object.
        """

        black = (0, 0, 0)
        blue = (0, 0, 255)
        pygame.draw.rect(self.image, (black), (0, 0, width, height))
        pygame.draw.rect(self.image, (blue),
                         (3, 3, width - 6, height - 6))
