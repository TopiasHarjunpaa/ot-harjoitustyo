import pygame
from entities.player import Player
from entities.floor import Floor
from entities.obstacle import Obstacle
from settings import LEVEL_1_FLOOR, LEVEL_1_GROUND_OBSTACLES, LEVEL_1_AIR_FLOOR


class LevelService:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.all_sprites = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.lavas = pygame.sprite.Group()
        self.obstacle = pygame.sprite.Group()
        self.player = Player(self, width/2, self.height /
                             4 * 3, self.width / 40)
        self.init_sprites()
        self.update()

    def update(self):
        self.all_sprites.update()
        self.handle_jump()
        return self.player_is_alive()

    def player_is_alive(self):
        if pygame.sprite.spritecollide(self.player, self.lavas, False):
            return False
        if pygame.sprite.spritecollide(self.player, self.obstacle, False):
            return False
        return True

    def handle_jump(self):
        touch = pygame.sprite.spritecollide(self.player, self.floors, False)
        if touch:
            self.player.y = touch[0].rect.top
            self.player.speed = 0

    def init_sprites(self):
        # Lots of improvements with variables...
        floor_width = self.width * 2
        air_floor_width = self.width / 5
        air_foor_steps = self.height/10
        floor_thickness = self.height / 80
        base_height = self.height / 4 * 3
        obstacle_size = self.width / 40

        for i in range(len(LEVEL_1_FLOOR)):
            if LEVEL_1_FLOOR[i] == 0:
                self.floors.add(Floor(i*floor_width, base_height,
                                floor_width, floor_thickness, (255, 255, 255)))
                ground_obstacles = LEVEL_1_GROUND_OBSTACLES[i]
                for j in range(len(ground_obstacles)):
                    if ground_obstacles[j] == 1:
                        self.obstacle.add(
                            Obstacle((i + j/10) * floor_width, base_height,
                                     obstacle_size, obstacle_size))
            else:
                self.lavas.add(Floor(i*floor_width, base_height,
                                     floor_width, floor_thickness, (55, 55, 55)))
                air_floors = LEVEL_1_AIR_FLOOR[i]
                for j in range(len(air_floors)):
                    value = air_floors[j]
                    if value > 0:
                        self.floors.add(Floor(
                            (i + j/10) * floor_width, base_height -
                            air_foor_steps * value,
                            air_floor_width, floor_thickness, (55, 55, 55)))

        self.all_sprites.add(self.player, self.floors,
                             self.lavas, self.obstacle)
