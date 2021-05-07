import unittest
import pygame
from services.game_service import GameService
from services.level_service import LevelService


class StubClock:
    def tick(self):
        pass


class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def __init__(self):
        self.width = 640
        self.height = 480

    def render_game(self, level):
        pass


class StubAudio:
    def play_die_sound(self):
        pass

    def play_jump_sound(self):
        pass


class StubUI:
    def __init__(self):
        self.audio = StubAudio()

    def show_finish_view(self):
        pass

    def show_game_over_view(self):
        pass

    def quit(self):
        pass

    def show_start_view(self):
        pass


class TestGameService(unittest.TestCase):
    def setUp(self):
        self.width = 640
        self.height = 480
        self.level = LevelService(640, 480, 0)
        self.menu = StubUI()

    def test_complete_level(self):
        events = [StubEvent(None, None), ]

        gameloop = GameService(
            self.menu,
            self.level,
            StubRenderer(),
            StubEventQueue(events),
            StubClock(),
            self.menu.audio
        )

        gameloop.start_gameloop(0)
        self.assertTrue(self.level.finished)

    def test_not_complete_level_without_keys(self):
        events = [StubEvent(None, None), ]

        gameloop = GameService(
            self.menu,
            self.level,
            StubRenderer(),
            StubEventQueue(events),
            StubClock(),
            self.menu.audio
        )

        gameloop.start_gameloop(1)
        self.assertFalse(self.level.finished)
    
    def test_jump_call_works_when_key_is_pressed(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_SPACE), ]

        gameloop = GameService(
            self.menu,
            self.level,
            StubRenderer(),
            StubEventQueue(events),
            StubClock(),
            self.menu.audio
        )

        gameloop.check_events()
        self.level.update()
        self.assertNotEqual(self.level.player.speed, 0)

    def test_escape_key_ends_loop(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_ESCAPE), ]

        gameloop = GameService(
            self.menu,
            self.level,
            StubRenderer(),
            StubEventQueue(events),
            StubClock(),
            self.menu.audio
        )

        gameloop.start_gameloop(0)
        self.assertFalse(gameloop.playing)