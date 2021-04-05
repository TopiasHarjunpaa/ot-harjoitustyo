import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, game, x, y, width, height):
        super().__init__()
        self.game = game
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)
        self.visualize(width, height)

    def update(self):
        self.rect.x -= self.game.speed
        if self.rect.right < 0:
            self.kill()

    def visualize(self, width, height):
        # Temporary solution
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        bs = 2
        pygame.draw.rect(self.image, (WHITE), (0, 0, width, height))
        pygame.draw.rect(self.image, (BLUE),
                         (bs, bs, width - 2 * bs, height - 2 * bs))
