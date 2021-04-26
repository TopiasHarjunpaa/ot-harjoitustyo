import unittest
from services.level_service import LevelService
from entities.sprites import Sprites
from entities.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.level = LevelService(self.width, self.height, 1)
        self.sprites = Sprites(self.level, self.width, self.height)
        self.player = self.level.player

    def test_allow_jump_during_floor_hit(self):
        self.player.jump()
        self.assertTrue(self.player.jumping)

    def test_not_allow_jump_while_players_is_in_air(self):
        self.player.position.y = 0
        self.player.rect.midbottom = (
            self.player.position.x, self.player.position.y)
        self.player.jump()
        self.assertFalse(self.player.jumping)
