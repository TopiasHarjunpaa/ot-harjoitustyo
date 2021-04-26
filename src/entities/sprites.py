import pygame
from entities.player import Player
from entities.floor import Floor
from entities.obstacle import Obstacle
from config import MAP_PATHS


class Sprites:
    def __init__(self, level, width, height):
        self.level = level
        self.size = (width, height)
        self.all_sprites = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.lavas = pygame.sprite.Group()
        self.goals = pygame.sprite.Group()
        self.obstacle = pygame.sprite.Group()
        self.player = Player(self.level, self.size[0]/2,
                             self.size[1] / 4 * 3, self.size[0] / 40)
        self.init_sprites()

    def init_sprites(self):
        obstacle_size = self.size[0] / 40
        object_w = self.size[0] / 20
        object_h = self.size[1] / 12
        filename = MAP_PATHS[self.level.level_number]

        with open(filename) as file:
            row_nr = 0
            for row in file:
                parts = row.strip().split(",")
                column_nr = 0
                for part in parts:
                    if part == "f":
                        floor = Floor(self.level, column_nr * object_w,
                                      row_nr * object_h, object_w,
                                      obstacle_size, "f")
                        self.floors.add(floor)
                    if part == "l":
                        lava = Floor(self.level, column_nr * object_w,
                                     row_nr * object_h, object_w,
                                     obstacle_size, "l")
                        self.lavas.add(lava)
                    if part == "g":
                        goal = Floor(self.level, column_nr * object_w, row_nr * object_h,
                                     object_w, obstacle_size, "g")
                        self.goals.add(goal)
                    if part == "x":
                        obstacle = Obstacle(self.level, column_nr * object_w + object_w / 2,
                                            (row_nr + 1) * object_h,
                                            obstacle_size, obstacle_size)
                        self.obstacle.add(obstacle)
                    column_nr += 1
                row_nr += 1

        self.all_sprites.add(self.player, self.floors,
                             self.lavas, self.obstacle, self.goals)
