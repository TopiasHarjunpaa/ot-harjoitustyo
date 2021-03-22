import pygame
# Temporary solution
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, height):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (640, height)

    def update(self):
        self.rect.x -= 8
        if self.rect.right < 0:
            self.kill()
