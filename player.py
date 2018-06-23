import pygame
from event_dispatcher import game_dispatcher as dispatcher
from events import events as Events
from vector_generator import Vector
import constants


class Player:
    def __init__(self, x=float(41), y=float(26)):
        self.x = float(x)
        self.y = float(y)
        self.width = 40
        self.height = 25
        self.color = (66, 244, 161)
        self.velocity = Vector(0, 0)
        dispatcher.subscribe(Events.PLAYER_CHANGE_POS, self.update_pos)
        dispatcher.subscribe(Events.DRAW_GAME, self.draw)
        dispatcher.subscribe(Events.UPDATE_GAME, self.update)

    def update(self):
        self.x += self.velocity.x
        self.y += self.velocity.y
        direction_change = self.wall_detection()  # collision physics
        if direction_change != Vector(1, 1):
            self.velocity.x *= 0.5 * direction_change.x
            self.velocity.y *= 0.5 * direction_change.y
            self.force_inbounds()

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def update_pos(self, vector):
        self.velocity += vector

    def force_inbounds(self):
        if 0 > self.x:
            self.x = 0
        elif self.x > constants.screen_width - self.width:
            self.x = constants.screen_width - self.width

        if 0 > self.y:
            self.y = 0
        elif self.y > constants.screen_height - self.height:
            self.y = constants.screen_height - self.height

    def wall_detection(self):
        collision = Vector(1, 1)

        if not 0 < self.x < constants.screen_width - self.width:
            collision.x = -1
        if not 0 < self.y < constants.screen_height - self.height:
            collision.y = -1

        return collision
