import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('./images/mousepointer.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


    def move_right(self):
        self.rect.x +=self.velocity

    def move_left(self):
        self.rect.x -=self.velocity

    def move_up(self):
        self.rect.y -=self.velocity

    def move_down(self):
        self.rect.y +=self.velocity