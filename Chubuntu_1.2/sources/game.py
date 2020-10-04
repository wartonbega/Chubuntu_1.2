import pygame
from player import Player
from window import Window


class Game:

    def __init__(self):
        self.player = Player()
        self.window = Window()
        self.pressed = {}
