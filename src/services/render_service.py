import pygame


class RenderService:
    def __init__(self, display, level, background):
        self.display = display
        self._level = level
        self._background = background

    def render(self):
        self.display.fill(self._background)
        self._level.all_sprites.draw(self.display)
        pygame.display.flip()
