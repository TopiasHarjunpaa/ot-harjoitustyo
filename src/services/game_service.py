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
            event_queue (Event_queue): Event_queue object.
            clock (Clock): Clock object.
            audio (Audio): Audio object.
        """

        self.clock = clock
        self.level = level
        self.renderer = renderer
        self.event_queue = event_queue
        self.playing = False
        self.audio = audio
        self.menu = ui

    def start_gameloop(self, level):
        """Starts the game loop.

        Initialises Level object with display information, level number and audio object.

        Check events, playing status and render the display during the loop.
        Game loop ends if level is finished or player dies.

        Show finish view if level is finished.
        Show game over view and play die sound if player dies.


        Args:
            level (Level): Level object.
        """

        self.playing = True
        self.level.__init__(self.renderer.width,
                            self.renderer.height, level, self.audio)
        while self.playing:
            self.clock.tick()
            self.check_events()
            self.playing = self.level.update()
            self.render()
        if self.level.finished:
            self.menu.show_finish_view()
        self.menu.audio.play_die_sound()
        self.menu.show_game_over_view()

    def check_events(self):
        """Checks player events.

        Quits when player closes the game window.
        Calls jump when player presses space.
        Show start view when player presses escape.
        """

        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                self.menu.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.level.player.jump()
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.menu.show_start_view()

    def render(self):
        """Call renderer object which renders the display.
        """

        self.renderer.render_game(self.level)
