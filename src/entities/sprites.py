import pygame
from entities.player import Player
from entities.floor import Floor
from entities.obstacle import Obstacle
from config import MAP_PATHS


class Sprites:
    """A class to represent sprites object. This object initialises all sprites.

    Attributes:
        level: Level object
        width: Width of the display.
        heigth: Heigth of the display.
    """

    def __init__(self, level, width, height):
        """Constructs all the necessary attributes for the sprites object and inits all sprites.

        Args:
            level (Level): Level object
            width (int): Width of the display.
            heigth (int): Heigth of the display.
        """

        self.level = level
        self.size = (width, height)
        self.all_sprites = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.lavas = pygame.sprite.Group()
        self.goals = pygame.sprite.Group()
        self.obstacle = pygame.sprite.Group()
        self.player = Player(self.level, self.size[0]/2,
                             self.size[1] / 4 * 3, self.size[0] / 40)
        self.init_sprites()

    def init_sprites(self):
        """Initialises all sprites according to display size and filemap.

        Sprite size parameters will be adjusted depending from the display size.
        Spawn location for all sprites will be obtained from the .csv file.
        Each level has own .csv file with spawn information.

        Each sprite types will be separated into own groups and also into list of all sprites.
        """

        obstacle_size = self.size[0] / 40
        object_w = self.size[0] / 20
        object_h = self.size[1] / 12
        filename = MAP_PATHS[self.level.level_number]

        with open(filename) as file:
            row_nr = 0
            for row in file:
                parts = row.strip().split(",")
                column_nr = 0
                for part in parts:
                    if part == "f":
                        floor = Floor(self.level, column_nr * object_w,
                                      row_nr * object_h, object_w,
                                      obstacle_size, "f")
                        self.floors.add(floor)
                    if part == "l":
                        lava = Floor(self.level, column_nr * object_w,
                                     row_nr * object_h, object_w,
                                     obstacle_size, "l")
                        self.lavas.add(lava)
                    if part == "g":
                        goal = Floor(self.level, column_nr * object_w, row_nr * object_h,
                                     object_w, obstacle_size, "g")
                        self.goals.add(goal)
                    if part == "x":
                        obstacle = Obstacle(self.level, column_nr * object_w + object_w / 2,
                                            (row_nr + 1) * object_h,
                                            obstacle_size, obstacle_size)
                        self.obstacle.add(obstacle)
                    column_nr += 1
                row_nr += 1

        self.all_sprites.add(self.player, self.floors,
                             self.lavas, self.obstacle, self.goals)
