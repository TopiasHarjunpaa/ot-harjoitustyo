import pygame


class Player(pygame.sprite.Sprite):
    """A class to represent player object at the game level.

    Attributes:
        level: Level object
        x_coordinate: Spawn location at the x-axis.
        y_coordinate: Spawn location at the y-axis.
        size: side length of the rectangular player object.
    """

    def __init__(self, level, x_coordinate, y_coordinate, size):
        """Constructs all the necessary attributes for the player object.

        Args:
            level (Level): Level object
            x_coordinate (int): Spawn location at the x-axis.
            y_coordinate (int): Spawn location at the y-axis.
            size (int): side length of the rectangular player object.
        """

        super().__init__()
        self._level = level
        self._orig_img = pygame.Surface(
            (size, size), pygame.SRCALPHA)
        self._visualize(size)
        self.image = self._orig_img
        self.rect = self.image.get_rect()
        self.position = pygame.math.Vector2(
            x_coordinate, y_coordinate)
        self.speed = 0
        self.rect.midbottom = (x_coordinate, y_coordinate)
        self.jumping = False
        self._angle = 0

    def jump(self):
        """Makes player object to jump if standing at the floor.

        Checks collision with floors and allow jump if collision occurs.
        Jump increases player speed from 0 to -14. This means that player
        will start lifting up during each update.

        Play the jumping sound unless the audio has not initialised.
        For example if audio has not initialised at the test cases.
        """

        floor_hit = pygame.sprite.spritecollide(
            self, self._level.sprites.floors, False)
        if floor_hit:
            self.speed -= 14
            self.jumping = True
            if self._level.audio is not None:
                self._level.audio.play_jump_sound()

    def update(self):
        """Updates location of the player object.

        Speed reduces by 0.7 every update. Negative speed corresponds lifting up
        and positive speed corresponds falling down. Speed is 0 while standing on a floor.
        This will simulate the gravity while jumping.

        Rotate player object at every update while jumping.
        End rotation if jumping ends or player object has already rotated 90 degrees.
        """

        self.speed += 0.7
        self.position.y += self.speed + 0.4
        self.rect.midbottom = (self.position.x, self.position.y)
        if self.jumping and self._angle >= -90:
            self.image = pygame.transform.rotate(
                self._orig_img, self._angle)
            self._angle -= 3
        else:
            self.jumping = False
            self._angle = 0
            self.image = pygame.transform.rotate(
                self._orig_img, self._angle)

    def _visualize(self, size):
        """Creates visualization for the player object.

        Player object has purple color with black borders.

        Args:
            size (int): side length of the rectangular player object.
        """

        black = (0, 0, 0)
        purple = (255, 0, 255)
        pygame.draw.rect(self._orig_img, (black), (0, 0, size, size))
        pygame.draw.rect(self._orig_img, (purple),
                         (3, 3, size - 6, size - 6))
