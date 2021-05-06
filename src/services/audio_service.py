import pygame
from config import PLAYLIST, BACK, JUMP, KEY, FORWARD, DIE


class AudioService:
    """A class to represent audio service which handles the audio of the game.

    """

    def __init__(self):
        """Loads audio files for the audio service.

        Audio filepaths are obtained from the config -file.
        """

        self.playlist = PLAYLIST
        self.music = pygame.mixer.music
        self.music.set_volume(0.4)
        self.menu_music_active = False
        self.music_on = True
        self.sound_effects_on = True

    def play_music(self, index=0):
        """Handles the background music.

        Does nothing if music is flagged off or
        if menu music is active and index is 0.
        Otherwise play the music according to the index.

        Args:
            index (int, optional): Is used to choose music from the playlist.
            0 = menu music (default)
            1 = level 1 music
            2 = level 2 music...
        """
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
        """Flags the music off and stops the current music.
        """
        self.menu_music_active = False
        self.music_on = False
        self.music.stop()

    def set_sound_effects_off(self):
        """Flags the sound effects off.
        """

        self.sound_effects_on = False

    def set_music_on(self):
        """Flags the music on and start menu music.
        """

        self.music_on = True
        self.play_music()

    def set_sound_effects_on(self):
        """Flags the sound effects on.
        """

        self.sound_effects_on = True

    def get_audio_information(self):
        return (self.music_on, self.sound_effects_on)

    def play_back_sound(self):
        """Play the sound effect "back" if sound effects are flagged on.
        """

        if self.sound_effects_on:
            back = pygame.mixer.Sound(BACK)
            back.play()

    def play_forward_sound(self):
        """Play the sound effect "forward" if sound effects are flagged on.
        """

        if self.sound_effects_on:
            forward = pygame.mixer.Sound(FORWARD)
            forward.play()

    def play_key_sound(self):
        """Play the sound effect "key" if sound effects are flagged on.

        Adjust the volume.
        """

        if self.sound_effects_on:
            key = pygame.mixer.Sound(KEY)
            key.set_volume(0.5)
            key.play()

    def play_jump_sound(self):
        """Play the sound effect "jump" if sound effects are flagged on.

        Adjust the volume.
        """

        if self.sound_effects_on:
            jump = pygame.mixer.Sound(JUMP)
            jump.set_volume(0.5)
            jump.play()

    def play_die_sound(self):
        """Play the sound effect "die" if sound effects are flagged on.
        """

        if self.sound_effects_on:
            die = pygame.mixer.Sound(DIE)
            die.play()
