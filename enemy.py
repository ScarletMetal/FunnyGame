import pygame
from event_dispatcher import game_dispatcher as dispatcher
from events import events as Events


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 25
        self.color = (244, 66, 232)

        dispatcher.subscribe(Events.DRAW_GAME, self.draw)
        dispatcher.subscribe(Events.ENEMY_UPDATE_LOCATION, self.update_location)

    def update_location(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))