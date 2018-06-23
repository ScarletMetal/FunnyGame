import pygame
pygame.init()


run = True
win = pygame.display.set_mode((400, 255))
pygame.display.set_caption("Super Game")
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()
