import random
import pygame
from entities.player import Player
from entities.floor import Floor
from entities.obstacle import Obstacle


class LevelService:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.obstacle = pygame.sprite.Group()
        self.player = Player(self)
        self.init_sprites()

    def update(self):
        self.all_sprites.update()
        # Just for testing
        rnd = random.randint(0, 60)
        if rnd == 0 and len(self.obstacle) < 2:
            obstacle = Obstacle(400)
            self.all_sprites.add(obstacle)
            self.obstacle.add(obstacle)
        floor_hit = pygame.sprite.spritecollide(
            self.player, self.floors, False)
        if floor_hit:
            self.player.y = floor_hit[0].rect.top
            self.player.speed = 0
        dead = pygame.sprite.spritecollide(self.player, self.obstacle, False)
        if dead:
            return False
        return True

    def init_sprites(self):
        floor = Floor(400)
        self.floors.add(floor)
        self.all_sprites.add(self.player, self.floors, self.obstacle)
