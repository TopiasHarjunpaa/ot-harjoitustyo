import pygame


class EventService:
    def __init__(self, clock):
        self.clock = clock

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "SPACE"

    def wait_for_key_pressed(self, key, fps):
        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    return "QUIT"
                if event.type == pygame.KEYUP:
                    if event.key == key:
                        waiting = False
