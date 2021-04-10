import pygame
from ui.ui import UI


class GameService:
    def __init__(self, level, renderer, event_queue, clock, width, height):
        self.clock = clock
        self.level = level
        self.renderer = renderer
        self.event_queue = event_queue
        self.playing = False
        self.menu = UI(self)  # Maybe change name of the file...
        self.width = width
        self.heigth = height

    def launch(self):
        self.menu.start_menu()

    def start_gameloop(self):
        self.playing = True
        self.level.__init__(self.width, self.heigth)
        while self.playing:
            self.clock.tick()
            self.check_events()
            self.playing = self.level.update()
            self.render()
        if self.level.finished:
            self.menu.show_finish_view()
        self.menu.show_transition_view()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.menu.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.level.player.jump()
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.menu.show_start_view()

    def render(self):
        self.renderer.render_game()
