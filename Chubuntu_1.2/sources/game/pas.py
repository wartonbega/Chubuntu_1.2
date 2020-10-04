import pygame


class Pas(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('./pas.png')
        self.rect = self.image.get_rect()




