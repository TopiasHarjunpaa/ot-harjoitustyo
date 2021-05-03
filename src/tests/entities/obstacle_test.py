import pygame
import unittest
from services.level_service import LevelService
from entities.obstacle import Obstacle


class TestObstacle(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.level = LevelService(self.width, self.height, 1)
        self.obstacle = Obstacle(
            self.level, self.width / 2, self.height / 2, 20, 20)
        self.obstacle_group = pygame.sprite.Group()
        self.obstacle_group.add(self.obstacle)

    def test_update_moves_outside_the_screen(self):
        self.assertEqual(len(self.obstacle_group), 1)
        while self.obstacle.rect.right >= 0:
            self.obstacle.update()
        self.assertEqual(len(self.obstacle_group), 0)
