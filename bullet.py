import pygame
from event_dispatcher import game_dispatcher as dispatcher
from events import events as Events
import constants


class Bullet:
    def __init__(self, enemy, x, y, velocity, radius=5, color=(255, 255, 255)):
        self.velocity = velocity
        self.x = x
        self.y = y
        self.target = enemy
        self.radius = radius
        self.color = color

        dispatcher.subscribe(Events.UPDATE_GAME, self.update)
        dispatcher.subscribe(Events.DRAW_GAME, self.draw)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.x += self.velocity.x
        self.y += self.velocity.y

    def check_if_inbound(self):
        return self.radius < self.x < constants.screen_width - self.radius \
               and self.radius < self.y < constants.screen_height - self.radius

    def check_if_hit(self):
        return (self.x - self.target.x + self.target.width / 2) ** 2 + (
                    self.y - self.target.y + self.target.height / 2) ** 2 < (self.radius + self.target.width / 2) ** 2
