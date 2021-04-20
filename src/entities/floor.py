import pygame


class Floor(pygame.sprite.Sprite):
    def __init__(self, level, x_coordinate, y_coordinate, width, height, floor_type):
        super().__init__()
        self.level = level
        self.floor_type = floor_type
        self.image = pygame.Surface(
            (width, height), pygame.SRCALPHA)  # pylint: disable=no-member
        self.visualize(width, height)
        self.rect = self.image.get_rect()
        self.rect.x = x_coordinate
        self.rect.y = y_coordinate

    def update(self):
        self.rect.x -= self.level.speed
        if self.rect.right < 0:
            self.kill()

    def visualize(self, width, height):
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
