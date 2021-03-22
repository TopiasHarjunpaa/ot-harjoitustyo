import pygame


class ClockService:
    def __init__(self, fps):
        self._clock = pygame.time.Clock()
        self._fps = fps

    def tick(self):
        self._clock.tick(self._fps)

    def get_ticks(self):
        return pygame.time.get_ticks()
