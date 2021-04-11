from os import sys
import pygame
from ui.start_view import StartView
from ui.menu_view import MenuView
from ui.game_over_view import GameOverView
from ui.finish_view import FinishView
from ui.new_game_view import NewGameView
from ui.load_game_view import LoadGameView


class UI:
    def __init__(self, game):
        self.game = game
        self.renderer = game.renderer
        self.menu_view_is_open = False

    def start_menu(self):
        self.show_menu_view()

    def show_menu_view(self):
        #Get all time records from the database and render
        self.menu_view_is_open = True
        MenuView(self.renderer).show()
        self.wait_for_key_pressed(pygame.K_n)
        self.menu_view_is_open = False
        # if new game
        self.show_new_game_view()
        # if load game
        # self.show_load_game_view()

        # Not working... Try remake key press functions...
        # key = self.check_key() #Temp
        #self.menu_view_is_open = False
        # if key == pygame.K_n:
        #    self.show_new_game_view()
        # if key == pygame.K_l:
        #    self.show_load_game_view()

    def show_new_game_view(self):
        nickname = "****"
        continue_text_color = (70, 70, 70)
        NewGameView(self.renderer).show(nickname, continue_text_color)
        for i in range(4):
            asc = self.wait_for_nickname_key()
            nickname = nickname[:i] + chr(asc - 32) + (3 - i) * "*"
            if i == 3:
                continue_text_color = (255, 255, 255)
            NewGameView(self.renderer).show(nickname, continue_text_color)
        self.wait_for_key_pressed(pygame.K_RETURN)
        # Save new game into database...
        self.show_start_view()

    def show_load_game_view(self):
        # Load saves from the database.
        saves = ["TOTO", "ASWD", "ROLF", "BBBK", "MNAR"]  # Test list...
        LoadGameView(self.renderer).show(saves)
        # Wait for players choice and get save params
        self.wait_for_key_pressed(pygame.K_1)  # Testing...
        self.show_start_view()

    def show_start_view(self):
        # Get unlock and progress information from the database
        # Open all unlocked levels and add progress parameters
        # Render also name of the save
        StartView(self.renderer).show()
        # Add functionality to choose level if unlocked...
        self.wait_for_key_pressed(pygame.K_1)
        self.game.start_gameloop()

    def show_game_over_view(self):
        # Check discovered percentage and render into screen
        # Save into database if that's new record
        GameOverView(self.renderer).show()
        self.wait_for_key_pressed(pygame.K_RETURN)
        self.show_start_view()

    def show_finish_view(self):
        # Check if the level is already completed
        # Unlock new level if needed
        # Save into database
        FinishView(self.renderer).show()
        self.wait_for_key_pressed(pygame.K_RETURN)
        self.show_start_view()

    def quit(self):
        pygame.quit()
        sys.exit()

    # Needs to be modified
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

    # Needs to be modified
    def wait_for_nickname_key(self):
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
                        return event.key

    # Temp. Not working as intended...
    def check_key(self):
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
                    waiting = False
                    return event.key
