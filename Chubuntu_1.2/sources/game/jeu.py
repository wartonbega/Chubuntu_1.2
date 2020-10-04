import pygame
from game import Game

pygame.init()

game = Game()

pygame.display.set_caption("jeu")
screen=pygame.display.set_mode((500,500))

background=pygame.image.load('./fond.png')

running = True
nbr=[]
while running:
    pas = 0
    nbr+=game.goose.rect
    screen.blit(game.goose.image,game.goose.rect)
    screen.blit(background, (0,0))
    screen.blit(game.goose.image,game.goose.rect)

    game.goose.all_pas.draw(screen)

    pygame.display.flip()
    pas+=1

    if game.pressed.get(pygame.K_RIGHT) and game.goose.rect.x+40<500:
        game.goose.all_pas.draw(screen)
        game.goose.move_right()

    elif game.pressed.get(pygame.K_LEFT) and game.goose.rect.x>-5:
        game.goose.move_left()

    elif game.pressed.get(pygame.K_UP) and game.goose.rect.y>-5:
        game.goose.move_up()

    elif game.pressed.get(pygame.K_DOWN) and game.goose.rect.y+40<470:
        game.goose.move_down()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
