import pygame


class GameService:
    """A class to represent game loop services.

    Attributes:
        ui: UI object
        level: Level object.
        renderer: Renderer object.
        event_queue: Event_queue object.
        clock: Clock object.
        audio: Audio object.
    """

    def __init__(self, ui, level, renderer, event_queue, clock, audio):
        """Constructs all the necessary attributes for the game service object.

        Args:
            ui (UI): UI object
            level (Level): Level object.
            renderer (Renderer): Renderer object.
            event_queue (EventQueueService: Event and queue service object.
            clock (Clock): Clock object.
            audio (Audio): Audio object.
        """

        self._clock = clock
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self.playing = False
        self._audio = audio
        self._menu = ui

    def start_gameloop(self, level):
        """Starts the game loop.

        Initialises Level object with display information, level number and audio object.

        Check events, playing status and render the display during the loop.
        Game loop ends if level is finished or player dies.

        Show finish view if level is finished.
        Show game over view and play die sound if player dies.


        Args:
            level (int): Level number
        """

        self.playing = True
        self._level.__init__(self._renderer.width,
                             self._renderer.height, level, self._audio)
        while self.playing:
            self._clock.tick()
            self._check_events()
            self.playing = self._level.update()
            self._render()
        if self._level.finished:
            self._menu.show_finish_view()
        self._audio.play_die_sound()
        self._menu.show_game_over_view()

    def _check_events(self):
        """Checks player events.

        Quits when player closes the game window.
        Calls jump when player presses space.
        Show start view when player presses escape.
        """

        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                self._menu.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._level.player.jump()
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self._menu.show_start_view()

    def _render(self):
        """Call renderer object which renders the display.
        """

        self._renderer.render_game(self._level)
