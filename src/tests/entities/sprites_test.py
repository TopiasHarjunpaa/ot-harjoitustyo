import unittest
from services.level_service import LevelService
from entities.sprites import Sprites


class TestSprites(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.level = LevelService(self.width, self.height, 1)
        self.sprites = Sprites(self.level, self.width, self.height)

    def test_init_sprites_creates_every_sprite_types(self):
        self.assertNotEqual(len(self.sprites.floors), 0)
        self.assertNotEqual(len(self.sprites.lavas), 0)
        self.assertNotEqual(len(self.sprites.goals), 0)
        self.assertNotEqual(len(self.sprites.obstacle), 0)
        self.assertNotEqual(len(self.sprites.all_sprites), 0)
