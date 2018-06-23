import time

import pygame

from client import constants
from client.bullet import Bullet
from client.event_dispatcher import game_dispatcher as dispatcher
from client.events import events as Events
from client.vector import Vector


class Player:
    def __init__(self, x=float(41), y=float(26)):
        self.x = float(x)
        self.y = float(y)
        self.width = 40
        self.height = 25
        self.color = (66, 244, 161)
        self.velocity = Vector(0, 0)
        self.bullets = []
        self.time_since_shot = time.time()
        dispatcher.subscribe(Events.PLAYER_CHANGE_POS, self.update_pos)
        dispatcher.subscribe(Events.DRAW_GAME, self.draw)
        dispatcher.subscribe(Events.UPDATE_GAME, self.update)
        dispatcher.subscribe(Events.PLAYER_APPEND_BULLET, self.append_bullet)

    def update(self):
        self.x += self.velocity.x
        self.y += self.velocity.y
        if self.velocity.get_magnitude() > constants.max_speed:
            self.velocity *= constants.max_speed / self.velocity.get_magnitude()
        self.velocity *= 0.99
        direction_change = self.wall_detection()  # collision physics
        if direction_change != Vector(1, 1):
            self.velocity.x *= 0.5 * direction_change.x
            self.velocity.y *= 0.5 * direction_change.y
            self.force_inbounds()

        for bullet in self.bullets:
            bullet.update()
            if not bullet.check_if_inbound():
                index = self.bullets.index(bullet)
                del self.bullets[index]
            if bullet.check_if_hit():
                index = self.bullets.index(bullet)
                del self.bullets[index]
                dispatcher.dispatch(Events.ENEMY_HIT)

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

        for bullet in self.bullets:
            bullet.draw(win)

    def append_bullet(self, cursor_pos, enemy):
        if len(self.bullets) < constants.max_bullets and \
                time.time() - self.time_since_shot > constants.time_between_shots:
            self.time_since_shot = time.time()
            bullet_velocity = Vector(cursor_pos()[0] - self.x, cursor_pos()[1] - self.y)
            self.bullets.append(
                Bullet(x=self.x + self.width / 2, y=self.y + self.height / 2,
                       velocity=constants.bullet_speed / bullet_velocity.get_magnitude() * bullet_velocity,
                       enemy=enemy))

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
