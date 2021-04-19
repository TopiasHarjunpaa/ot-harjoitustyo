import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, level, x, y, width, height):
        super().__init__()
        self.level = level
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.visualize(width, height)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

    def update(self):
        self.rect.x -= self.level.speed
        if self.rect.right < 0:
            self.kill()

    def visualize(self, width, height):
        white = (255, 255, 255)
        blue = (0, 0, 255)
        pygame.draw.rect(self.image, (white), (0, 0, width, height))
        pygame.draw.rect(self.image, (blue),
                         (2, 2, width - 4, height - 4))
