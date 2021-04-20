import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x_coordinate, y_coordinate, size):
        super().__init__()
        self.game = game
        self.original_img = pygame.Surface(
            (size, size), pygame.SRCALPHA)  # pylint: disable=no-member
        self.visualize(size)
        self.image = self.original_img
        self.rect = self.image.get_rect()
        self.position = pygame.math.Vector2(  # pylint: disable=c-extension-no-member
            x_coordinate, y_coordinate)
        self.speed = 0
        self.rect.midbottom = (x_coordinate, y_coordinate)
        self.jumping = False
        self.angle = 0

    def jump(self):
        floor_hit = pygame.sprite.spritecollide(self, self.game.floors, False)
        if floor_hit:
            self.speed -= 14
            self.jumping = True

    def update(self):
        self.speed += 0.7
        self.position.y += self.speed + 0.4
        self.rect.midbottom = (self.position.x, self.position.y)
        if self.jumping and self.angle >= -90:
            self.image = pygame.transform.rotate(
                self.original_img, self.angle)
            self.angle -= 3
        else:
            self.jumping = False
            self.angle = 0
            self.image = pygame.transform.rotate(
                self.original_img, self.angle)

    def visualize(self, size):
        white = (255, 255, 255)
        purple = (255, 0, 255)
        pygame.draw.rect(self.original_img, (white), (0, 0, size, size))
        pygame.draw.rect(self.original_img, (purple),
                         (2, 2, size - 4, size - 4))
