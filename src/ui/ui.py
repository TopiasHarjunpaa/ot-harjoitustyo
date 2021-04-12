from os import sys
import pygame
from ui.start_view import StartView
from ui.menu_view import MenuView
from ui.game_over_view import GameOverView
from ui.finish_view import FinishView
from ui.new_game_view import NewGameView
from ui.load_game_view import LoadGameView
from services.information_service import InformationService


class UI:
    def __init__(self, game):
        self.game = game
        self.renderer = game.renderer
        self.menu_view_is_open = False
        self.infos = InformationService()

    def start_menu(self):
        self.show_menu_view()

    def show_menu_view(self):
        # TODO: Get all time records from the database and render
        self.menu_view_is_open = True
        MenuView(self.renderer).show()
        key = self.wait_and_check_accepted_keys([pygame.K_n, pygame.K_l])
        self.menu_view_is_open = False
        if key == pygame.K_n:
            self.show_new_game_view()
        if key == pygame.K_l:
            self.show_load_game_view()

    def show_new_game_view(self):
        nickname = "****"
        continue_text_color = (70, 70, 70)
        NewGameView(self.renderer).show(nickname, continue_text_color)
        for i in range(4):
            asc = self.wait_for_nickname_keys()
            nickname = nickname[:i] + chr(asc - 32) + (3 - i) * "*"
            if i == 3:
                continue_text_color = (255, 255, 255)
            NewGameView(self.renderer).show(nickname, continue_text_color)
        self.wait_and_check_accepted_keys([pygame.K_RETURN])
        self.infos.create_new_save(nickname)
        self.show_start_view()

    def show_load_game_view(self):
        saves = self.infos.list_saves()
        LoadGameView(self.renderer).show(saves)
        # TODO: Loop users choice and activate chosen save
        self.wait_and_check_accepted_keys([pygame.K_1])  # Temp for testing
        self.infos.open_save(saves[0].nickname)  # Temp for testing
        self.show_start_view()

    def show_start_view(self):
        information = self.infos.get_progress_information()
        StartView(self.renderer).show(information)
        # TODO: Add functionality to choose level if unlocked...
        self.wait_and_check_accepted_keys([pygame.K_1])
        self.game.start_gameloop()

    def show_game_over_view(self):
        # TODO: Check discovered percentage and render into screen
        # TODO: Save into database if that's new record
        GameOverView(self.renderer).show()
        self.wait_and_check_accepted_keys([pygame.K_RETURN])
        self.show_start_view()

    def show_finish_view(self):
        # TODO: Check if the level is already completed
        # TODO: Unlock new level if needed (update progress at database)
        FinishView(self.renderer).show()
        self.wait_and_check_accepted_keys([pygame.K_RETURN])
        self.show_start_view()

    def quit(self):
        pygame.quit()
        sys.exit()

    def wait_and_check_accepted_keys(self, keys: list):
        input_key = None
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
                    if event.key in keys:
                        input_key = event.key
                        waiting = False
        return input_key

    def wait_for_nickname_keys(self):
        input_key = None
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
                        self.show_menu_view()
                    if 97 <= event.key <= 122:
                        input_key = event.key
                        waiting = False
        return input_key
