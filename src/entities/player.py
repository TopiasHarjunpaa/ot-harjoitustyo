import pygame
# Temporary solution
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.Surface((40, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.y = 200
        self.x = 320
        self.speed = 0
        self.rect.midbottom = (self.x, self.y)

    def jump(self):
        floor_hit = pygame.sprite.spritecollide(self, self.game.floors, False)
        self.rect.x -= 1
        if floor_hit:
            self.speed -= 13

    def update(self):
        self.speed += 0.7
        self.y += self.speed + 0.4
        self.rect.midbottom = (self.x, self.y)
