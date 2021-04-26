import pygame
from entities.sprites import Sprites


class LevelService:
    def __init__(self, width, height, level_number, audio=None):
        self.audio = audio
        self.level_number = level_number
        self.speed = 10
        self.sprites = Sprites(self, width, height)
        self.all_sprites = self.sprites.all_sprites
        self.player = self.sprites.player
        self.finished = False
        self.progress = 0
        self.update()

    def update(self):
        self.all_sprites.update()
        self.handle_jump()
        self.handle_goal()
        self.progress += self.speed / 220
        if self.finished:
            self.speed -= 1
            if self.speed == 0:
                return False
        return self.player_is_alive()

    def player_is_alive(self):
        if pygame.sprite.spritecollide(self.player, self.sprites.lavas, False):
            return False
        if pygame.sprite.spritecollide(self.player, self.sprites.obstacle, False):
            return False
        return True

    def handle_jump(self):
        touch = pygame.sprite.spritecollide(
            self.player, self.sprites.floors, False)
        if touch:
            self.player.position.y = touch[0].rect.top
            self.player.speed = 0

    def handle_goal(self):
        touch = pygame.sprite.spritecollide(
            self.player, self.sprites.goals, False)
        if touch:
            self.player.position.y = touch[0].rect.top
            self.player.speed = 0
            self.finished = True
