import pygame


class GameService:
    def __init__(self, level, renderer, clock):
        self._renderer = renderer
        self._clock = clock
        self.level = level
        self.playing = True

    def run(self):
        while self.playing:
            self._clock.tick()
            self.events()
            self.playing = self.level.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Needs to be fixed
                self.playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.level.player.jump()

    def draw(self):
        self._renderer.render()
