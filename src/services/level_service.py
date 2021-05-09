import pygame
from entities.sprites import Sprites


class LevelService:
    """A class to represent level services.

    Attributes:
        width: Width of the display.
        height: Heigth of the display.
        level_number: Number of the level in game.
        audio: Audio service object.
    """

    def __init__(self, width, height, level_number, audio=None):
        """Constructs all the necessary attributes for the level service object.

        Args:
            width (int): Width of the display.
            height (int): Heigth of the display.
            level_number (int): Number of the level in game.
            audio (AudioService, optional): Audio service object. Defaults to None.
        """

        self.audio = audio
        self.level_number = level_number
        self.speed = 9 + level_number
        self.sprites = Sprites(self, width, height)
        self.all_sprites = self.sprites.all_sprites
        self.player = self.sprites.player
        self.finished = False
        self.progress = 0
        self.update()

    def update(self):
        """Updates all sprites in a game loop.

        Controls player object and progress points.
        Object movement speed starts slowly decrease to zero
        if players reaches finish line.

        Returns:
            True: If player is alive.
            False: If player is dead or reaches goal.
        """

        self.all_sprites.update()
        self._handle_jump()
        self._handle_goal()
        self.progress += self.speed / 220
        if self.finished:
            self.speed -= 1
            if self.speed == 0:
                return False
        return self._player_is_alive()

    def _player_is_alive(self):
        """Checks if player is alive during game loop.

        Checks collision with both obstacles and lavas (ie. non-friendly objects).

        Returns:
            True: If no collision occured.
            False: If collision occured with non-friendly object.
        """

        if pygame.sprite.spritecollide(self.player, self.sprites.lavas, False):
            return False
        if pygame.sprite.spritecollide(self.player, self.sprites.obstacle, False):
            return False
        return True

    def _handle_jump(self):
        """Checks if player is touching the floor.

        Touching the floor allows player to jump.
        Also players vertical speed will be reseted and location will be
        updated on top of the floor surface (prevents player falling through floor).
        """

        touch = pygame.sprite.spritecollide(
            self.player, self.sprites.floors, False)
        if touch:
            self.player.position.y = touch[0].rect.top
            self.player.speed = 0

    def _handle_goal(self):
        """Checks if player reaches the goal.

        Touching the goal starts preparation of level finish
        event at the update method.
        """

        touch = pygame.sprite.spritecollide(
            self.player, self.sprites.goals, False)
        if touch:
            self.player.position.y = touch[0].rect.top
            self.player.speed = 0
            self.finished = True
