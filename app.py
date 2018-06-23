import pygame
from event_dispatcher import game_dispatcher as dispatcher
from player import Player
from events import Events

pygame.init()
run = True
win = pygame.display.set_mode((400, 255))
pygame.display.set_caption("Super Game")

player = Player()


def update_io(k):
    if k[pygame.K_LEFT]:
        dispatcher.dispatch(Events.PLAYER_CHANGE_X, x=-1)
    if k[pygame.K_RIGHT]:
        dispatcher.dispatch(Events.PLAYER_CHANGE_X, x=1)

    if k[pygame.K_UP]:
        dispatcher.dispatch(Events.PLAYER_CHANGE_Y, y=-1)
    if k[pygame.K_DOWN]:
        dispatcher.dispatch(Events.PLAYER_CHANGE_Y, y=1)


while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    update_io(keys)

pygame.quit()
