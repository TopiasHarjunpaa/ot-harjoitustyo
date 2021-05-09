from os import sys
import pygame
from ui.start_view import StartView
from ui.menu_view import MenuView
from ui.game_over_view import GameOverView
from ui.finish_view import FinishView
from ui.new_game_view import NewGameView
from ui.load_game_view import LoadGameView
from ui.setup_view import SetupView
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

        self._audio = audio
        self._renderer = renderer
        self.event_queue = event_queue
        self._clock = clock
        self._info = info
        self._menu_view_is_open = False
        self._level = LevelService(renderer.width, renderer.height, 1, audio)
        self._game = GameService(
            self, self._level, renderer, event_queue, clock, audio)

    def start_menu(self):
        """Starts main menu. Is used to launch the game.
        """

        self._show_menu_view()

    def _show_menu_view(self):
        """Shows the menu view.

        Start menu music.
        Get top 3 records from the database.
        Shows the menu view.
        Waits for key and forwards to the next view:
        n = new game view
        l = load game view
        s = game setup view
        """

        self._audio.play_music()
        records = self._info.get_top_records(3)
        self._menu_view_is_open = True
        MenuView(self._renderer).show(records)
        key = self._wait_and_check_accepted_keys(
            [pygame.K_n, pygame.K_l, pygame.K_s])
        self._menu_view_is_open = False
        if key == pygame.K_n:
            self._show_new_game_view()
        if key == pygame.K_l:
            self._show_load_game_view()
        if key == pygame.K_s:
            self._show_setup_view()

    def _show_setup_view(self):
        """Shows the game setup view.

        Check music and sound fx status from audio service (on / off)
        Show the setup view with two setting types:
        1. music on / music off
        2. sound fx on / sound fx on

        Wait for key (1 = music and 2 = sound fx) and make the changes.
        Loop ends when esc or quit event happens while waiting for a key.
        """

        while True:
            audio_info = self._audio.get_audio_information()
            SetupView(self._renderer).show(audio_info)
            key = self._wait_and_check_accepted_keys([49, 50]) - 48
            if key == 1:
                if audio_info[0]:
                    self._audio.set_music_off()
                else:
                    self._audio.set_music_on()
            if key == 2:
                if audio_info[1]:
                    self._audio.set_sound_effects_off()
                else:
                    self._audio.set_sound_effects_on()

    def _show_new_game_view(self):
        """Shows the new game view.

        Sets continue text color to grey and nickname with four asterix.
        Shows the new game view and wait for player to type all 4 letters.
        Change continue text color to default (black) and wait for player to continue or edit text.
        Create new save with nickname after player has chosen to continue.
        Show start screen.
        """

        nickname = "****"
        continue_text_color = (70, 70, 70)
        NewGameView(self._renderer).show(nickname, continue_text_color)
        nickname = self._wait_for_nickname(nickname, 1)
        key = self._wait_and_check_accepted_keys(
            [pygame.K_RETURN, pygame.K_BACKSPACE], pygame.KEYDOWN)
        while key == pygame.K_BACKSPACE:
            nickname = nickname[:3] + "*"
            NewGameView(self._renderer).show(nickname, continue_text_color)
            nickname = self._wait_for_nickname(nickname, 4)
            key = self._wait_and_check_accepted_keys(
                [pygame.K_RETURN, pygame.K_BACKSPACE], pygame.KEYDOWN)
        self._info.create_new_save(nickname)
        self.show_start_view()

    def _show_load_game_view(self):
        """Shows the load game view

        Get list of saves (min. 0 saves and max. 8 saves ) from information service.
        Wait for key and open the save according to key number.
        Show the start view.
        """

        saves = self._info.list_saves(8)
        LoadGameView(self._renderer).show(saves)
        key = self._wait_and_check_accepted_keys(
            range(49, len(saves) + 49)) - 49
        self._info.open_save(saves[key].save_id)
        self.show_start_view()

    def show_start_view(self):
        """Shows the start game view

        Start menu music (if player returns from the game, otherwise nothing happens)
        Get progress information from the current save and show the start game view.
        Wait for key (available keys depends from the save progress):
        1. At least one level available
        2. 2nd key is available if 1st level is completed
        3. 3rd key is available if 2nd level is completed etc...

        Game has moving background. Reset its position back to beginning.
        Start playing music according to the level and key choice.
        Start game loop according to the level and key choice. 
        """

        self._audio.play_music()
        information = self._info.get_progress_information()
        StartView(self._renderer).show(information)
        available_levels = min(
            information["number_of_levels"], information["levels_completed"] + 1)
        level = self._wait_and_check_accepted_keys(
            range(49, available_levels + 49)) - 48
        self._renderer.reset_game_background_position()
        self._audio.play_music(level)
        self._game.start_gameloop(level)

    def show_game_over_view(self):
        """Shows the game over view

        Start playing menu music.
        Get the progress from previous game event.
        Compare the progress with earlier record and update if previous was higher.
        Show the game over screen-
        Waits for key and forwards to the next view:
        enter = start game view (ie. try again).
        esc = back to main menu.
        """

        self._audio.play_music()
        progress = int(self._level.progress)
        level = self._level.level_number
        information = self._info.get_progress_information()
        if progress > information[f"level{level}"]:
            total_progress = (level - 1) * 100 + progress
            self._info.update_save(total_progress, information["id"])
        GameOverView(self._renderer).show(information, progress, level)
        self._wait_and_check_accepted_keys([pygame.K_RETURN])
        self.show_start_view()

    def show_finish_view(self):
        """Shows the finish view

        Start playing menu music.
        Get the progress from previous game event.
        Check if current level was already completed. Update if it was not.
        Show the finish screen.
        Waits for key and forwards to the next view:
        enter = start game view (ie. continue playing).
        esc = back to main menu.
        """

        self._audio.play_music()
        level = self._level.level_number
        information = self._info.get_progress_information()
        if information[f"level{level}"] != 100:
            total_progress = level * 100
            self._info.update_save(total_progress, information["id"])
        FinishView(self._renderer).show(information, level)
        self._wait_and_check_accepted_keys([pygame.K_RETURN])
        self.show_start_view()

    def quit(self):
        """Quits the game.
        """

        pygame.quit()
        sys.exit()

    def _wait_for_nickname(self, nickname, char_number):
        """Waits for key presses and updates nickname.

        This is used to form 4 letter nickname. Only
        alphabets are accepted (not numbers or special letters)

        Start collecting the alphabets and fill remaining
        letters with asterix. Update the screen after every accepted key press.
        Continue text will be rendered as grey until four letters has been typed.
        Backspace replaces last letter with asterix and takes one step back in wait loop.

        Args:
            nickname (str): String of letters
            char_number (int): Number of letter in nickname.

        Returns:
            str: Returns nickname with big letters.
        """

        accepted_keys = list(range(97, 123))
        accepted_keys.append(pygame.K_BACKSPACE)
        while char_number <= 4:
            asc = self._wait_and_check_accepted_keys(
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
            NewGameView(self._renderer).show(nickname, continue_text_color)
            char_number += 1
        return nickname

    def _wait_and_check_accepted_keys(self, keys: list, event_type=pygame.KEYUP):
        """Waits and checks accepted keys.

        Check escape and quit keys:
        1. QUIT = game ends
        2. ESC = returns to menu and game ends if menu view is open

        Waits for accepted keys. When proper key is found:
        1. Play key press sound
        2. Save the key
        3. Stop wait loop

        Args:
            keys (list): List of accepted keys
            event_type ((pygame.event), optional): Defaults to pygame.KEYUP.

        Returns:
            int: Returns ascii number of pressed key.
        """

        input_key = None
        waiting = True
        while waiting:
            self._clock.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._audio.play_back_sound()
                    waiting = False
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        waiting = False
                        self._audio.play_back_sound()
                        if self._menu_view_is_open:
                            self.quit()
                        self._show_menu_view()
                if event.type == event_type:
                    if event.key in keys:
                        input_key = event.key
                        waiting = False
                        if event.type == pygame.KEYUP:
                            self._audio.play_forward_sound()
                        else:
                            self._audio.play_key_sound()
        return input_key
