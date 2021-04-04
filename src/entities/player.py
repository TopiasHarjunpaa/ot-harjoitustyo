import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, size):
        super().__init__()
        self.game = game
        self.original_image = pygame.Surface((size, size), pygame.SRCALPHA)
        self.visualize(size)
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = 0
        self.rect.midbottom = (self.x, self.y)
        self.jumping = False
        self.angle = 0

    def jump(self):
        floor_hit = pygame.sprite.spritecollide(self, self.game.floors, False)
        self.rect.x -= 1
        if floor_hit:
            self.speed -= 14
            self.jumping = True

    def update(self):
        self.speed += 0.7
        self.y += self.speed + 0.4
        self.rect.midbottom = (self.x, self.y)
        if self.jumping and self.angle >= -90:
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.angle -= 3
        else:
            self.jumping = False
            self.angle = 0
            self.image = pygame.transform.rotate(self.original_image, self.angle)
    
    def visualize(self, size):
        #Temporary solution
        WHITE =(255, 255, 255)
        PURPLE = (255, 0, 255)
        bs = 2
        pygame.draw.rect(self.original_image, (WHITE), (0, 0, size, size))
        pygame.draw.rect(self.original_image, (PURPLE), (bs, bs, size - 2 * bs, size - 2 * bs))
