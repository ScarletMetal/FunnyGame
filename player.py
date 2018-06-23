import pygame


class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 25
        self.color = (66, 244, 161)

    def update(self):
        pass

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    def change_x(self, x):
        self.x += x

    def change_y(self, y):
        self.y += y
