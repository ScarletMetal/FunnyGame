import pygame

from client.event_dispatcher import game_dispatcher as dispatcher
from client.events import events as Events


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 25
        self.color = (244, 66, 232)

        dispatcher.subscribe(Events.DRAW_GAME, self.draw)
        dispatcher.subscribe(Events.ENEMY_UPDATE_LOCATION, self.update_location)
        dispatcher.subscribe(Events.ENEMY_HIT, self.enemy_hit)

    def update_location(self, x, y):
        self.x = x
        self.y = y

    def enemy_hit(self):
        print("Ouch!!")

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))