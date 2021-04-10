import pygame
from entities.player import Player
from entities.floor import Floor
from entities.obstacle import Obstacle


class LevelService:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.all_sprites = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.lavas = pygame.sprite.Group()
        self.goals = pygame.sprite.Group()
        self.obstacle = pygame.sprite.Group()
        self.player = Player(self, self.width/2, self.height /
                             4 * 3, self.width / 40)
        self.init_sprites()
        self.speed = 10
        self.finished = False
        self.update()

    def update(self):
        self.all_sprites.update()
        self.handle_jump()
        self.handle_goal()
        if self.finished:
            self.speed -= 1
            if self.speed == 0:
                return False
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

    def handle_goal(self):
        touch = pygame.sprite.spritecollide(self.player, self.goals, False)
        if touch:
            self.player.y = touch[0].rect.top
            self.player.speed = 0
            self.finished = True

    def init_sprites(self):
        obstacle_size = self.width / 40
        object_w = self.width / 20
        object_h = self.height / 12
        floor_thickness = self.width / 40

        filename = "src/assets/level_1.csv"
        # filename = "src/assets/level_1_test.csv" #for testing

        with open(filename) as file:
            row_nr = 0
            for row in file:
                parts = row.strip().split(",")
                column_nr = 0
                for part in parts:
                    if part == "f":
                        floor = Floor(self, column_nr * object_w,
                                      row_nr * object_h, object_w,
                                      floor_thickness, "f")
                        self.floors.add(floor)
                    if part == "l":
                        lava = Floor(self, column_nr * object_w,
                                     row_nr * object_h, object_w,
                                     floor_thickness, "l")
                        self.lavas.add(lava)
                    if part == "g":
                        goal = Floor(self, column_nr * object_w, row_nr * object_h,
                                     object_w, floor_thickness, "g")
                        self.goals.add(goal)
                    if part == "x":
                        obstacle = Obstacle(self, column_nr * object_w + object_w / 2,
                                            (row_nr + 1) * object_h,
                                            obstacle_size, obstacle_size)
                        self.obstacle.add(obstacle)
                    column_nr += 1
                row_nr += 1

        self.all_sprites.add(self.player, self.floors,
                             self.lavas, self.obstacle, self.goals)
