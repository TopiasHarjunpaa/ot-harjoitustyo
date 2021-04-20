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
        # TODO: Re-think if records needs own method for infos.
        records = self.infos.list_saves()
        self.menu_view_is_open = True
        MenuView(self.renderer).show(records)
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
            asc = self.wait_and_check_accepted_keys(
                range(97, 123), pygame.KEYDOWN)
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
        key = self.wait_and_check_accepted_keys(
            range(49, len(saves) + 49)) - 49
        self.infos.open_save(saves[key].save_id)
        self.show_start_view()

    def show_start_view(self):
        information = self.infos.get_progress_information()
        StartView(self.renderer).show(information)
        available_levels = min(
            information["number_of_levels"], information["levels_completed"] + 1)
        level = self.wait_and_check_accepted_keys(
            range(49, available_levels + 49)) - 48
        self.game.start_gameloop(level)

    def show_game_over_view(self):
        progress = int(self.game.level.progress)
        level = self.game.level.level_number
        information = self.infos.get_progress_information()
        if progress > information[f"level{level}"]:
            total_progress = (level - 1) * 100 + progress
            self.infos.update_save(total_progress, information["id"])
        GameOverView(self.renderer).show(information, progress, level)
        self.wait_and_check_accepted_keys([pygame.K_RETURN])
        self.show_start_view()

    def show_finish_view(self):
        level = self.game.level.level_number
        information = self.infos.get_progress_information()
        if information[f"level{level}"] != 100:
            total_progress = level * 100
            self.infos.update_save(total_progress, information["id"])
        FinishView(self.renderer).show(information, level)
        self.wait_and_check_accepted_keys([pygame.K_RETURN])
        self.show_start_view()

    def quit(self):
        pygame.quit()
        sys.exit()

    def wait_and_check_accepted_keys(self, keys: list, event_type=pygame.KEYUP):
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
                if event.type == event_type:
                    if event.key in keys:
                        input_key = event.key
                        waiting = False
        return input_key
