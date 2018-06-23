import pygame
from event_dispatcher import game_dispatcher as dispatcher
from events import Events
from vector_generator import Vector
import constants


class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 25
        self.color = (66, 244, 161)
        self.velocity = Vector()
        dispatcher.subscribe(Events.PLAYER_CHANGE_POS, self.update_pos)

    def update(self):
        pass

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def update_pos(self, vector):
        self.velocity += vector
        direction_change = self.wall_detection()

        if direction_change != Vector(1, 1):
            self.velocity.x *= -0.5 * direction_change.x
            self.velocity.y *= -0.5 * direction_change.y

    def wall_detection(self):
        collision = Vector(1, 1)

        if not self.width < self.x < constants.screen_width - self.width:
            collision.x = -1
        if not self.height < self.y < constants.screen_height - self.height:
            collision.y = -1

        return collision
