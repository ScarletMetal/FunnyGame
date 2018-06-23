import pygame
from event_dispatcher import game_dispatcher as dispatcher
from events import Events
from vector_generator import Vector

class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 25
        self.color = (66, 244, 161)
        self.vector = Vector()
        dispatcher.subscribe(Events.PLAYER_CHANGE_POS, self.update_pos)

    def update(self):
        pass

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def update_pos(self, vector):
        self.vector += vector
