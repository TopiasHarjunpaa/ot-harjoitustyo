from os import sys
import pygame
from ui.start_view import StartView
from ui.menu_view import MenuView
from ui.transition_view import TransitionView
from ui.finish_view import FinishView


class UI:
    def __init__(self, game):
        self.game = game
        self.renderer = game.renderer
        self.menu_view_is_open = False

    def start_menu(self):
        self.show_menu_view()

    def show_menu_view(self):
        self.menu_view_is_open = True
        MenuView(self.renderer).show()
        self.wait_for_key_pressed(pygame.K_n)
        self.menu_view_is_open = False
        self.show_start_view()

        # Multiple choices needs to be implemented, such as:
        # - Start new game -> goes to fresh start_view
        # - Continue saved game --> goes to start_view with saved params
        #       * Perhaps new window with list of saves?
        #       * Or list below the new game option
        # - Later add new window for options...?

    def show_start_view(self):
        StartView(self.renderer).show()
        self.wait_for_key_pressed(pygame.K_s)
        self.game.start_gameloop()

        # Multiple choices needs to be implemented, such as:
        # - Start game loop
        # - Go back to menu_view (ESC returns back)
        # - Make possibility to choose level. Right now only 1 level.

    def show_transition_view(self):
        #Rename transition_view into game_over_view or something...
        # Needs lots of improvements... Just temp for testing...
        TransitionView(self.renderer).show()
        self.wait_for_key_pressed(pygame.K_c)
        self.show_start_view()
        # Multiple choices needs to be implemented, such as:
        # - Start game loop again (from same level)
        # - Go back to start_view

    def show_finish_view(self):
        # Needs lots of improvements... Just temp for testing...
        FinishView(self.renderer).show()
        self.wait_for_key_pressed(pygame.K_c)
        self.show_start_view()

    def quit(self):
        pygame.quit()
        sys.exit()

    def wait_for_key_pressed(self, key):
        waiting = True
        while waiting:
            self.game.clock.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        waiting = False
                        if self.menu_view_is_open:
                            self.quit()
                        self.show_menu_view()
                if event.type == pygame.KEYUP:
                    if event.key == key:
                        waiting = False
