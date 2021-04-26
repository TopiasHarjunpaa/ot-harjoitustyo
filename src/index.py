import pygame
from services.clock_service import ClockService
from services.event_queue_service import EventQueueService
from services.audio_service import AudioService
from services.information_service import InformationService
from ui.renderer import Renderer
from ui.ui import UI
from config import FPS, TITLE


def main():
    pygame.init()
    display_info = pygame.display.Info()
    display_width = display_info.current_w
    display_heigth = display_info.current_h
    display = pygame.display.set_mode((display_width, display_heigth))
    pygame.display.set_caption(TITLE)

    audio = AudioService()
    renderer = Renderer(display, display_width, display_heigth)
    event_queue = EventQueueService()
    clock = ClockService(FPS)
    info = InformationService()
    user_interface = UI(audio, renderer, event_queue, clock, info)

    user_interface.start_menu()


if __name__ == "__main__":
    main()
