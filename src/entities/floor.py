import pygame


class Floor(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height, type):
        super().__init__()
        self.game = game
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.visualize(width, height)

    def update(self):
        self.rect.x -= self.game.speed
        if self.rect.right < 0:
            self.kill()

    def visualize(self, width, height):
        # Temporary solution
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        FIREBRICK = (178, 34, 34)
        GREEN = (0, 255, 0)
        bs = 2

        if self.type == "f":
            pygame.draw.rect(self.image, (WHITE), (0, 0, width, height))
            pygame.draw.rect(self.image, (FIREBRICK),
                             (bs, bs, width - 2 * bs, height - 2 * bs))
        if self.type == "l":
            pygame.draw.rect(self.image, (FIREBRICK), (0, 0, width, height))
            pygame.draw.rect(self.image, (BLACK),
                             (bs, bs, width - 2 * bs, height - 2 * bs))
        if self.type == "g":
            pygame.draw.rect(self.image, (WHITE), (0, 0, width, height))
            pygame.draw.rect(self.image, (GREEN),
                             (bs, bs, width - 2 * bs, height - 2 * bs))
