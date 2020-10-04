import pygame
from pas import Pas

class Goose(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.all_pas = pygame.sprite.Group()
        self.image = pygame.image.load('./goose.png')
        self.pas = pygame.image.load('./pas.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def pas(self):
        self.all_pas.add(Pas())


    def move_right(self):
        self.rect.x +=self.velocity

    def move_left(self):
        self.rect.x -=self.velocity

    def move_up(self):
        self.rect.y -=self.velocity

    def move_down(self):
        self.rect.y +=self.velocity