import pygame


class Floor(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height, type):
        super().__init__()
        self.game = game
        self.type = type
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.visualize(width, height)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= self.game.speed
        if self.rect.right < 0:
            self.kill()

    def visualize(self, width, height):
        if self.type == "f":
            color1 = (255, 255, 255)
            color2 = (178, 34, 34)
        if self.type == "l":
            color1 = (178, 34, 34)
            color2 = (0, 0, 0)
        if self.type == "g":
            color1 = (255, 255, 255)
            color2 = (0, 255, 0)

        pygame.draw.rect(self.image, (color1), (0, 0, width, height))
        pygame.draw.rect(self.image, (color2),
                         (2, 2, width - 4, height - 4))
