import pygame
from services.game_service import GameService
from services.level_service import LevelService
from services.clock_service import ClockService
from services.render_service import RenderService
from services.event_queue_service import EventQueueService
from services.audio_service import AudioService
from config import FPS, TITLE


def main():
    # Needs to be changed thru UI instead...
    pygame.init()  # pylint: disable=no-member
    display_info = pygame.display.Info()
    display_width = display_info.current_w
    display_heigth = display_info.current_h
    display = pygame.display.set_mode((display_width, display_heigth))
    pygame.display.set_caption(TITLE)

    audio = AudioService()
    level = LevelService(display_width, display_heigth, 1, audio)
    renderer = RenderService(display, level)
    clock = ClockService(FPS)
    event_queue = EventQueueService()
    game = GameService(level, renderer, event_queue, clock,
                       display_width, display_heigth, audio)

    game.launch()


if __name__ == "__main__":
    main()
