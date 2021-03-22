import pygame


class RenderService:
    def __init__(self, display, level, background):
        self._display = display
        self._level = level
        self._background = background

    def render(self):
        self._display.fill(self._background)
        self._level.all_sprites.draw(self._display)
        pygame.display.flip()
