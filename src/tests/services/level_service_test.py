import unittest
from services.level_service import LevelService
from entities.floor import Floor
from entities.obstacle import Obstacle


class TestLevelService(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.level = LevelService(self.width, self.height)
        self.base_height = self.height / 4 * 3
        self.floor_thickness = self.height / 80
        self.player = self.level.player

    def test_jump_handle_works_while_not_jumping(self):
        self.assertEqual(self.player.speed, 0)
        self.assertEqual(self.player.y, self.height / 4 * 3)

    def test_jump_handle_works_while_jumping(self):
        self.player.jump()
        self.level.update()
        self.assertNotEqual(self.player.speed, 0)
        self.assertNotEqual(self.player.y, self.base_height)

    def test_player_is_alive_at_the_start(self):
        self.assertTrue(self.level.player_is_alive())

    def test_player_is_not_alive_when_collide_with_lava(self):
        self.level.lavas.add(
            Floor(self, 0, self.base_height, self.width, self.floor_thickness, "l"))
        self.assertFalse(self.level.player_is_alive())

    def test_player_is_not_alive_when_collide_with_obstacle(self):
        self.level.obstacle.add(
            Obstacle(self, self.width/2, self.base_height, 50, 50))
        self.assertFalse(self.level.player_is_alive())
