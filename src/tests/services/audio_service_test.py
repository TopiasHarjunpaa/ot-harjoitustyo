import unittest
import pygame
from services.audio_service import AudioService


class TestAudioService(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.audio = AudioService()

    def test_something(self):
        pass
