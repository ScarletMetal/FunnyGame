import pygame
from event_dispatcher import game_dispatcher as dispatcher
from events import Events


class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 25
        self.color = (66, 244, 161)
        dispatcher.subscribe(Events.PLAYER_CHANGE_X, self.change_x)
        dispatcher.subscribe(Events.PLAYER_CHANGE_Y, self.change_y)

    def update(self):
        pass

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def change_x(self, x):
        pass

    def change_y(self, y):
        pass
