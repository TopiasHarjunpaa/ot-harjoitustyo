from os import sys
import pygame
from ui.start_view import StartView
from ui.menu_view import MenuView
from ui.game_over_view import GameOverView
from ui.finish_view import FinishView
from ui.new_game_view import NewGameView
from ui.load_game_view import LoadGameView
from services.level_service import LevelService
from services.game_service import GameService


class UI:
    """A class to represent main UI which handles every view.
    """

    def __init__(self, audio, renderer, event_queue, clock, info):
        """Constructs all the necessary attributes for UI.

        Args:
            audio (AudioService): Audio service object.
            renderer (Renderer): Renderer object.
            event_queue (EventQueueService: Event and queue service object.
            clock (Clock): Clock object.
            info (InformationService): Information service object.
        """

        self.audio = audio
        self.renderer = renderer
        self.event_queue = event_queue
        self.clock = clock
        self.info = info
        self.menu_view_is_open = False
        self.level = LevelService(renderer.width, renderer.height, 1, audio)
        self.game = GameService(
            self, self.level, renderer, event_queue, clock, audio)

    def start_menu(self):
        """Starts main menu. Is used to launch the game.
        """

        self.show_menu_view()

    def show_menu_view(self):
        """Shows the menu view.

        Start menu music.
        Gets the records from database.
        Shows the menu view.
        Waits for player key and forwards to the next view:
        n = new game view
        l = load game view

        Note: Currently records are using list of save objects.
        This list is not ideal for this purposes and requires some ugly filtering menu view.
        Better solution could be to create another method at information service to
        recieve own list for records.
        """

        self.audio.play_music()
        records = self.info.list_saves()
        self.menu_view_is_open = True
        MenuView(self.renderer).show(records)
        key = self.wait_and_check_accepted_keys([pygame.K_n, pygame.K_l])
        self.menu_view_is_open = False
        if key == pygame.K_n:
            self.show_new_game_view()
        if key == pygame.K_l:
            self.show_load_game_view()

    def show_new_game_view(self):
        """Shows the new game view.

        Sets continue text color to grey and nickname with four asterix.
        Shows the new game view and wait for player to type all 4 letters.
        Change continue text color to default (black) and wait for player to continue or edit text.
        Create new save with nickname after player has chosen to continue.
        Show start screen.
        """

        nickname = "****"
        continue_text_color = (70, 70, 70)
        NewGameView(self.renderer).show(nickname, continue_text_color)
        nickname = self.wait_for_nickname(nickname, 1)
        key = self.wait_and_check_accepted_keys(
            [pygame.K_RETURN, pygame.K_BACKSPACE], pygame.KEYDOWN)
        while key == pygame.K_BACKSPACE:
            nickname = nickname[:3] + "*"
            NewGameView(self.renderer).show(nickname, continue_text_color)
            nickname = self.wait_for_nickname(nickname, 4)
            key = self.wait_and_check_accepted_keys(
                [pygame.K_RETURN, pygame.K_BACKSPACE], pygame.KEYDOWN)
        self.info.create_new_save(nickname)
        self.show_start_view()

    def show_load_game_view(self):
        """Placeholder...
        """

        saves = self.info.list_saves()
        LoadGameView(self.renderer).show(saves)
        key = self.wait_and_check_accepted_keys(
            range(49, len(saves) + 49)) - 49
        self.info.open_save(saves[key].save_id)
        self.show_start_view()

    def show_start_view(self):
        self.audio.play_music()
        information = self.info.get_progress_information()
        StartView(self.renderer).show(information)
        available_levels = min(
            information["number_of_levels"], information["levels_completed"] + 1)
        level = self.wait_and_check_accepted_keys(
            range(49, available_levels + 49)) - 48
        self.renderer.reset_game_background_position()
        self.audio.play_music(level)
        self.game.start_gameloop(level)

    def show_game_over_view(self):
        self.audio.play_music()
        progress = int(self.level.progress)
        level = self.level.level_number
        information = self.info.get_progress_information()
        if progress > information[f"level{level}"]:
            total_progress = (level - 1) * 100 + progress
            self.info.update_save(total_progress, information["id"])
        GameOverView(self.renderer).show(information, progress, level)
        self.wait_and_check_accepted_keys([pygame.K_RETURN])
        self.show_start_view()

    def show_finish_view(self):
        self.audio.play_music()
        level = self.level.level_number
        information = self.info.get_progress_information()
        if information[f"level{level}"] != 100:
            total_progress = level * 100
            self.info.update_save(total_progress, information["id"])
        FinishView(self.renderer).show(information, level)
        self.wait_and_check_accepted_keys([pygame.K_RETURN])
        self.show_start_view()

    def quit(self):
        pygame.quit()
        sys.exit()

    def wait_for_nickname(self, nickname, char_number):
        accepted_keys = list(range(97, 123))
        accepted_keys.append(pygame.K_BACKSPACE)
        while char_number <= 4:
            asc = self.wait_and_check_accepted_keys(
                accepted_keys, pygame.KEYDOWN)
            if asc == pygame.K_BACKSPACE:
                if char_number == 1:
                    char_number -= 1
                    nickname = "****"
                else:
                    char_number -= 2
                    nickname = nickname[:char_number] + (4 - char_number) * "*"
            else:
                nickname = nickname[:char_number - 1] + \
                    chr(asc - 32) + (4 - char_number) * "*"
            if char_number == 4:
                continue_text_color = (255, 255, 255)
            else:
                continue_text_color = (70, 70, 70)
            NewGameView(self.renderer).show(nickname, continue_text_color)
            char_number += 1
        return nickname

    def wait_and_check_accepted_keys(self, keys: list, event_type=pygame.KEYUP):
        input_key = None
        waiting = True
        while waiting:
            self.clock.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.audio.play_back_sound()
                    waiting = False
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        waiting = False
                        self.audio.play_back_sound()
                        if self.menu_view_is_open:
                            self.quit()
                        self.show_menu_view()
                if event.type == event_type:
                    if event.key in keys:
                        input_key = event.key
                        waiting = False
                        if event.type == pygame.KEYUP:
                            self.audio.play_forward_sound()
                        else:
                            self.audio.play_key_sound()
        return input_key
