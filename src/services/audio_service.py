import pygame
from config import MENU_MUSIC, LEVEL1_MUSIC, BACK, JUMP, KEY, FORWARD, DIE


class AudioService:
    def __init__(self):
        self.playlist = [MENU_MUSIC, LEVEL1_MUSIC]
        self.music = pygame.mixer.music
        self.music.set_volume(0.4)
        self.back = pygame.mixer.Sound(BACK)
        self.forward = pygame.mixer.Sound(FORWARD)
        self.key = pygame.mixer.Sound(KEY)
        self.jump = pygame.mixer.Sound(JUMP)
        self.jump.set_volume(0.5)
        self.die = pygame.mixer.Sound(DIE)
        self.menu_music_active = False
        self.music_on = True
        self.sound_effects_on = True

    def play_music(self, index=0):
        if self.music_on:
            if not self.menu_music_active and index == 0:
                self.music.fadeout(500)
                self.music.load(self.playlist[index])
                self.music.play(loops=-1)
                self.menu_music_active = True
            elif index >= 1:
                self.music.fadeout(500)
                self.music.load(self.playlist[index])
                self.music.play(loops=-1)
                self.menu_music_active = False

    def set_music_off(self):
        self.music_on = False
        self.music.fadeout(500)

    def set_sound_effects_off(self):
        self.sound_effects_on = False

    def set_music_on(self):
        self.music_on = True
        self.play_music()

    def set_sound_effects_on(self):
        self.sound_effects_on = True

    def play_back_sound(self):
        if self.sound_effects_on:
            self.back.play()

    def play_forward_sound(self):
        if self.sound_effects_on:
            self.forward.play()

    def play_key_sound(self):
        if self.sound_effects_on:
            self.key.play()

    def play_jump_sound(self):
        if self.sound_effects_on:
            self.jump.play()

    def play_die_sound(self):
        if self.sound_effects_on:
            self.die.play()
