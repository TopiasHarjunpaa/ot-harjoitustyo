import pygame
from services.game_service import GameService
from services.level_service import LevelService
from services.render_service import RenderService
from services.clock_service import ClockService
from repositories.user_repository import user_repository
from repositories.result_repository import result_repository

WIDTH = 640
HEIGHT = 480
TITLE = "The Possible Game"
BACKGROUND = (0, 0, 0)
FPS = 60


def main():
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    level = LevelService()
    renderer = RenderService(display, level, BACKGROUND)
    clock = ClockService(FPS)
    game = GameService(level, renderer, clock)
    game.run()
    # while game.running:

    #    level = LevelService()
    #    renderer = RenderService(display, level, BACKGROUND)
    #    game = GameService(level, renderer, clock)

    pygame.quit()


if __name__ == "__main__":
    main()
