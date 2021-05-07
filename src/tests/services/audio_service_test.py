import unittest
import pygame
from services.audio_service import AudioService


class TestAudioService(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.audio = AudioService()

    def test_game_music_begins_when_music_is_on(self):
        self.audio.play_music(1)
        playing = self.audio.music.get_busy()
        self.assertTrue(playing)

    def test_music_not_begin_when_music_is_off(self):
        self.audio.set_music_off()
        self.audio.play_music()
        self.audio.play_music()
        playing = self.audio.music.get_busy()
        self.assertFalse(playing)
        self.assertFalse(self.audio.music_on)

    def test_menu_music_does_not_restart_when_menu_music_is_active(self):
        self.audio.music.stop()
        self.audio.menu_music_active = True
        self.audio.play_music()
        playing = self.audio.music.get_busy()
        self.assertFalse(playing)

    def test_menu_music_restarts_when_menu_music_is_not_active(self):
        self.audio.music.stop()
        self.audio.menu_music_active = False
        self.audio.play_music()
        playing = self.audio.music.get_busy()
        self.assertTrue(playing)

    def test_menu_music_starts_when_music_is_set_on(self):
        self.audio.set_music_on()
        playing = self.audio.music.get_busy()
        self.assertTrue(playing)
        self.assertTrue(self.audio.menu_music_active)
        self.assertTrue(self.audio.music_on)

    def test_sound_effects_does_not_play_when_effects_are_off(self):
        self.audio.set_sound_effects_off()
        self.audio.play_back_sound()
        self.assertFalse(pygame.mixer.get_busy())
        self.audio.play_forward_sound()
        self.assertFalse(pygame.mixer.get_busy())
        self.audio.play_jump_sound()
        self.assertFalse(pygame.mixer.get_busy())
        self.audio.play_die_sound()
        self.assertFalse(pygame.mixer.get_busy())
        self.audio.play_key_sound()
        self.assertFalse(pygame.mixer.get_busy())

    def test_sound_effects_does_play_when_effects_are_on(self):
        self.audio.set_sound_effects_on()
        self.audio.play_back_sound()
        self.assertTrue(pygame.mixer.get_busy())
        self.audio.play_forward_sound()
        self.assertTrue(pygame.mixer.get_busy())
        self.audio.play_jump_sound()
        self.assertTrue(pygame.mixer.get_busy())
        self.audio.play_die_sound()
        self.assertTrue(pygame.mixer.get_busy())
        self.audio.play_key_sound()
        self.assertTrue(pygame.mixer.get_busy())

    def test_get_audio_information_when_both_on(self):
        audio_info = self.audio.get_audio_information()
        self.assertTrue(audio_info[0])
        self.assertTrue(audio_info[1])

    def test_get_audio_information_when_both_off(self):
        self.audio.set_music_off()
        self.audio.set_sound_effects_off()
        audio_info = self.audio.get_audio_information()
        self.assertFalse(audio_info[0])
        self.assertFalse(audio_info[1])

    def test_get_audio_information_when_one_off_and_one_on(self):
        self.audio.set_sound_effects_off()
        audio_info = self.audio.get_audio_information()
        self.assertTrue(audio_info[0])
        self.assertFalse(audio_info[1])
        self.audio.set_sound_effects_on()
        self.audio.set_music_off()
        audio_info = self.audio.get_audio_information()
        self.assertFalse(audio_info[0])
        self.assertTrue(audio_info[1])
