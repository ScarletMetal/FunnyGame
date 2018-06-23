from enum import Enum


class Events:
    def __init__(self):
        self.PLAYER_CHANGE_POS = "player-change-pos"
        self.PLAYER_APPEND_BULLET = "player-append-bullet"
        self.PLAYER_HIT = "player-hit"

        self.ENEMY_UPDATE_LOCATION = "enemy-update-location"
        self.ENEMY_HIT = "enemy-hit"

        self.DRAW_GAME = "draw-game"
        self.UPDATE_GAME = "update-game"


events = Events()
