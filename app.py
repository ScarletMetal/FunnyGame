import pygame
from event_dispatcher import game_dispatcher as dispatcher
from player import Player
from events import events as Events
from vector_generator import Vector
from cursor import Cursor
import constants

pygame.init()
run = True
win = pygame.display.set_mode((constants.screen_width, constants.screen_height))
pygame.display.set_caption("Super Game")

player = Player()
cursor = Cursor()
clock = pygame.time.Clock()


def update_player_velocity(keys):
    vector = Vector()
    if keys[pygame.K_a]:
        vector.x = -0.5
    if keys[pygame.K_d]:
        vector.x = 0.5

    if keys[pygame.K_w]:
        vector.y = -0.5
    if keys[pygame.K_s]:
        vector.y = 0.5

    if vector != Vector():
        dispatcher.dispatch(Events.PLAYER_CHANGE_POS, vector=vector)


def update_io(keys):
    update_player_velocity(keys)


while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    update_io(keys)
    dispatcher.dispatch(Events.UPDATE_GAME)
    win.fill((0, 0, 0))
    dispatcher.dispatch(Events.DRAW_GAME, win=win)
    pygame.display.update()

pygame.quit()
