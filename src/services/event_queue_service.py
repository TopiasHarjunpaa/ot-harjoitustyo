import pygame


class EventQueueService:
    def get(self):
        return pygame.event.get()
