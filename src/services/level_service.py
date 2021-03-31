import random
import pygame
from entities.player import Player
from entities.floor import Floor
from entities.obstacle import Obstacle
from settings import LEVEL_1_FLOOR, LEVEL_1_GROUND_OBSTACLES, LEVEL_1_AIR_FLOOR, WIDTH, HEIGHT  # temporary


class LevelService:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.lavas = pygame.sprite.Group()
        self.obstacle = pygame.sprite.Group()
        self.player = Player(self)
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
        #Lots of improvements with variables...
        for i in range(len(LEVEL_1_FLOOR)):
            if LEVEL_1_FLOOR[i] == 0:
                self.floors.add(Floor(i*2*WIDTH, HEIGHT/4*3, 2*WIDTH, 10, (255, 255, 255)))
                ground_obstacles = LEVEL_1_GROUND_OBSTACLES[i]
                for j in range(len(ground_obstacles)):
                    if ground_obstacles[j] == 1:
                        self.obstacle.add(Obstacle(i*2*WIDTH + j*2*WIDTH/10, HEIGHT/4*3, WIDTH/16, WIDTH/16))
            else:
                self.lavas.add(Floor(i*2*WIDTH, HEIGHT/4*3, 2*WIDTH, 10, (50, 50, 50)))
                air_floors = LEVEL_1_AIR_FLOOR[i]
                for j in range(len(air_floors)):
                    value = air_floors[j]
                    if value > 0:
                        self.floors.add(Floor(i*2*WIDTH + j*2*WIDTH/10, HEIGHT/4*3 - HEIGHT/10*value, 2*WIDTH/10, 10, (50, 50, 50)))
        self.all_sprites.add(self.player, self.floors, self.lavas, self.obstacle)
