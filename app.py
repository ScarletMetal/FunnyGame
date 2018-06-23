import pygame
from event_dispatcher import game_dispatcher as dispatcher
from player import Player
from events import events as Events
from vector_generator import Vector

import constants

pygame.init()
run = True
win = pygame.display.set_mode((constants.screen_width, constants.screen_height))
pygame.display.set_caption("Super Game")

player = Player()


def update_player_velocity(keys):
    vector = Vector()
    if keys[pygame.K_LEFT]:
        vector.x = -1
    if keys[pygame.K_RIGHT]:
        vector.x = 1

    if keys[pygame.K_UP]:
        vector.y = -1
    if keys[pygame.K_DOWN]:
        vector.y = 1

    if vector != Vector():
        dispatcher.dispatch(Events.PLAYER_CHANGE_POS, vector=vector)


def update_io(keys):
    update_player_velocity(keys)

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    update_io(keys)

    dispatcher.dispatch(Events.DRAW_GAME, win=win)
    pygame.display.update()

pygame.quit()
