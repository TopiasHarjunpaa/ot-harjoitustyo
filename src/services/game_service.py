from os import sys
import pygame
from ui.start_view import StartView
from ui.login_view import LoginView
from ui.transition_view import TransitionView
from settings import WIDTH, HEIGHT, TITLE, BACKGROUND, FPS  # Temporary
from services.level_service import LevelService
from services.event_service import EventService


class GameService:
    def __init__(self, level, renderer, event_queue, clock):
        self.clock = clock
        self.level = level
        self.renderer = renderer
        self.event_queue = event_queue
        self.logged_in = False
        self.playing = False
        self.events = EventService(self.clock)

    def start(self):
        if not self.logged_in:
            self.show_login_view()
        self.show_start_view()

    def run(self):
        self.level.__init__(self.level.width, self.level.height)
        while self.playing:
            self.clock.tick()
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
        self.renderer.render()

    def show_start_view(self):
        StartView(self.renderer.display).show()
        if self.events.wait_for_key_pressed(pygame.K_s) == "QUIT":
            self.quit()
        self.playing = True
        self.run()

    def show_login_view(self):
        LoginView(self.renderer.display).show()
        if self.events.wait_for_key_pressed(pygame.K_l) == "QUIT":
            self.quit()
        self.logged_in = True

    def show_transition_view(self):
        # Needs some improvements...
        TransitionView(self.renderer.display).show()
        if self.events.wait_for_key_pressed(pygame.K_c) == "QUIT":
            self.quit()
        self.start()
