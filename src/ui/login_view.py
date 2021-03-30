import pygame
from settings import WIDTH, HEIGHT, TITLE, BACKGROUND


class LoginView:
    def __init__(self, display):
        self._display = display

    def show(self):
        self._display.fill(BACKGROUND)
        font = pygame.font.SysFont("Arial", 24)
        text = font.render(
            "This is login screen (press l to log)", True, (255, 0, 0))
        center = text.get_rect()
        center.center = (WIDTH/2, HEIGHT/2)
        self._display.blit(text, center)
        pygame.display.flip()
