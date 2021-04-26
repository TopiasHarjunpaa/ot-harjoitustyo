import pygame


class GameService:
    def __init__(self, ui, level, renderer, event_queue, clock, audio):
        self.clock = clock
        self.level = level
        self.renderer = renderer
        self.event_queue = event_queue
        self.playing = False
        self.audio = audio
        self.menu = ui

    def start_gameloop(self, level):
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
        self.renderer.render_game(self.level)
