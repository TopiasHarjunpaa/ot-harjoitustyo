import pygame
# Temporary solution
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Floor(pygame.sprite.Sprite):
    def __init__(self, height):
        super().__init__()
        self.image = pygame.Surface((640, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = height
