import pygame

from client.event_dispatcher import game_dispatcher as dispatcher
from client.events import events as Events


class HPBar:
    def __init__(self, player):
        self.player = player
        dispatcher.subscribe(Events.DRAW_GAME, self.draw)
        dispatcher.subscribe(Events.UPDATE_GAME, self.update)

    def update(self):
        pass

    def draw(self, win):
        win.blit(pygame.font.SysFont('Comic Sans MS', 30).render(str(self.player.health), True, (255, 255, 255)),
                 (100, 100))
