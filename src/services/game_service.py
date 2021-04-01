from os import sys
import pygame
from ui.start_view import StartView
from ui.login_view import LoginView
from ui.transition_view import TransitionView
from settings import WIDTH, HEIGHT, TITLE, BACKGROUND, FPS  # Temporary
from services.level_service import LevelService
from services.event_service import EventService


class GameService:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.level = LevelService()
        self.logged_in = False
        self.playing = False
        self.events = EventService(self.clock)

    def start(self):
        if not self.logged_in:
            self.show_login_view()
        self.show_start_view()

    def run(self):
        self.level.__init__()
        while self.playing:
            self.clock.tick(FPS)
            self.check_events()
            self.playing = self.level.update()
            self.show_game_view()
        self.show_transition_view()

    def quit(self):
        pygame.quit()
        sys.exit()

    def check_events(self):
        event = self.events.handle_events()
        if event == "QUIT":
            self.quit()
        if event == "ESC":
            self.playing = False
            self.show_start_view()
        if event == "JUMP":
            self.level.player.jump()

    def show_game_view(self):
        self.display.fill(BACKGROUND)
        self.level.all_sprites.draw(self.display)
        pygame.display.flip()

    def show_start_view(self):
        StartView(self.display).show()
        if self.events.wait_for_key_pressed(pygame.K_s, FPS) == "QUIT":
            self.quit()
        self.playing = True
        self.run()

    def show_login_view(self):
        LoginView(self.display).show()
        if self.events.wait_for_key_pressed(pygame.K_l, FPS) == "QUIT":
            self.quit()
        self.logged_in = True

    def show_transition_view(self):
        # Needs some improvements...
        TransitionView(self.display).show()
        if self.events.wait_for_key_pressed(pygame.K_c, FPS) == "QUIT":
            self.quit()
        self.start()
