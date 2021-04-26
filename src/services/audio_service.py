import pygame
from config import PLAYLIST, BACK, JUMP, KEY, FORWARD, DIE


class AudioService:
    def __init__(self):
        self.playlist = PLAYLIST
        self.music = pygame.mixer.music
        self.music.set_volume(0.4)
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
            back = pygame.mixer.Sound(BACK)
            back.play()

    def play_forward_sound(self):
        if self.sound_effects_on:
            forward = pygame.mixer.Sound(FORWARD)
            forward.play()

    def play_key_sound(self):
        if self.sound_effects_on:
            key = pygame.mixer.Sound(KEY)
            key.set_volume(0.5)
            key.play()

    def play_jump_sound(self):
        if self.sound_effects_on:
            jump = pygame.mixer.Sound(JUMP)
            jump.set_volume(0.5)
            jump.play()

    def play_die_sound(self):
        if self.sound_effects_on:
            die = pygame.mixer.Sound(DIE)
            die.play()
