import unittest
from services.level_service import LevelService
from entities.floor import Floor
from entities.obstacle import Obstacle


class TestLevelService(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.level = LevelService(self.width, self.height, 0)
        self.base_height = self.height / 4 * 3
        self.floor_thickness = self.height / 80
        self.player = self.level.player

    def test_jump_handle_works_while_not_jumping(self):
        self.assertEqual(self.player.speed, 0)
        self.assertEqual(self.player.position.y, self.height / 4 * 3)

    def test_jump_handle_works_while_jumping(self):
        self.player.jump()
        self.level.update()
        self.assertNotEqual(self.player.speed, 0)
        self.assertNotEqual(self.player.position.y, self.base_height)

    def test_player_is_alive_at_the_start(self):
        self.assertTrue(self.level.player_is_alive())

    def test_player_is_not_alive_when_collide_with_lava(self):
        self.level.sprites.lavas.add(
            Floor(self, 0, self.base_height, self.width, self.floor_thickness, "l"))
        self.assertFalse(self.level.player_is_alive())

    def test_player_is_not_alive_when_collide_with_obstacle(self):
        self.level.sprites.obstacle.add(
            Obstacle(self, self.width/2, self.base_height, 50, 50))
        self.assertFalse(self.level.player_is_alive())

    def test_handle_goal(self):
        self.level.sprites.goals.add(
            Floor(self, 0, self.base_height, self.width, self.floor_thickness, "g"))
        self.level.handle_goal()
        self.assertTrue(self.level.finished)

    def test_speed_decreases_to_zero_when_finished(self):
        self.level.finished = True
        speed = self.level.speed
        while speed > 0:
            self.level.update()
            self.assertEqual(speed, self.level.speed + 1)
            speed = self.level.speed

    def test_update_returns_false_when_speed_is_zero(self):
        self.level.finished = True
        self.level.speed = 1
        self.assertFalse(self.level.update())
