import pygame
from services.game_service import GameService
from services.level_service import LevelService
from services.clock_service import ClockService
from services.render_service import RenderService
from services.event_queue_service import EventQueueService
from settings import FPS, TITLE


def main():
    pygame.init()
    display_info = pygame.display.Info()
    display_width = display_info.current_w
    display_heigth = display_info.current_h
    display = pygame.display.set_mode((display_width, display_heigth))
    pygame.display.set_caption(TITLE)

    # TODO: Re-think order between UI and GameService.
    level = LevelService(display_width, display_heigth, 1)
    renderer = RenderService(display, level)
    clock = ClockService(FPS)
    event_queue = EventQueueService()

    game = GameService(level, renderer, event_queue, clock,
                       display_width, display_heigth)
    game.launch()


if __name__ == "__main__":
    main()
