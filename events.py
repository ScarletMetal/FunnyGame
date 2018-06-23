from enum import Enum


class Events:
    def __init__(self):
        self.PLAYER_CHANGE_POS = "plcs"
        self.PLAYER_APPEND_BULLET = "plappblt"

        self.ENEMY_UPDATE_LOCATION = "enuploc"

        self.DRAW_GAME = "drgm"
        self.UPDATE_GAME = "updtgm"



events = Events()
