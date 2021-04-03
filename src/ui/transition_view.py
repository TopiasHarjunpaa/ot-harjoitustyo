import pygame
from settings import WIDTH, HEIGHT, TITLE, BACKGROUND


class TransitionView:
    def __init__(self, display):
        self._display = display
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()

    def show(self):
        self._display.fill(BACKGROUND)
        font = pygame.font.SysFont("Arial", 24)
        text = font.render(
            "This is transition screen (press c - continue)", True, (255, 0, 0))
        center = text.get_rect()
        center.center = (self.width/2, self.height/2)
        self._display.blit(text, center)
        pygame.display.flip()
