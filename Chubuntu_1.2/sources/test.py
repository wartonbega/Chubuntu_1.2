import pygame
from player import Player
from game import Game
from window import Window
import os

fichier = open('./settings/jeu.txt',"r")
app = fichier.read()
fichier.close()

pygame.init()

pygame.display.set_caption("jeu")
screen=pygame.display.set_mode((500,250))

background=pygame.image.load('./images/blanc.png')

game = Game()

player = Player()

window = Window()



running = True

while running:

    screen.blit(background, (0,0))

    screen.blit(game.player.image,game.player.rect)
    screen.blit(game.window.image,game.window.rect)

    pygame.display.flip()





    coord1 = game.player.rect.x
    coord2 = game.player.rect.y

    coord3 = game.window.rect.x
    coord4 = game.window.rect.y

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x+40<500:
        game.player.move_right()
        if coord1-10<coord3<coord1+10 and coord2-10<coord4<coord2+10:
            os.popen("python3 "+app+".py","r")
            pygame.quit()
            break
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x>-5:
        game.player.move_left()
        if coord1-10<coord3<coord1+10 and coord2-10<coord4<coord2+10:
            os.popen("python3 "+app+".py","r")
            pygame.quit()
            break
    elif game.pressed.get(pygame.K_UP) and game.player.rect.y>-5:
        game.player.move_up()
        if coord1-10<coord3<coord1+10 and coord2-10<coord4<coord2+10:
            os.popen("python3 "+app+".py","r")
            pygame.quit()
            break
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y+40<250:
        game.player.move_down()
        if coord1-10<coord3<coord1+10 and coord2-10<coord4<coord2+10:
            os.popen("python3 "+app+".py","r")
            pygame.quit()
            break

    if game.pressed.get(pygame.K_RIGHT) and game.window.rect.x>-5:
        game.window.move_left()
        if coord1-10<coord3<coord1+10 and coord2-10<coord4<coord2+10:
            os.popen("python3 "+app+".py","r")
            pygame.quit()
            break

    elif game.pressed.get(pygame.K_LEFT) and game.window.rect.x+40<500:
        game.window.move_right()
        if coord1-10<coord3<coord1+10 and coord2-10<coord4<coord2+10:
            os.popen("python3 "+app+".py","r")
            pygame.quit()
            break
    elif game.pressed.get(pygame.K_UP) and game.window.rect.y+40<250:
        game.window.move_down()
        if coord1-10<coord3<coord1+10 and coord2-10<coord4<coord2+10:
            os.popen("python3 "+app+".py","r")
            pygame.quit()
            break
    elif game.pressed.get(pygame.K_DOWN) and game.window.rect.y>-5:
        game.window.move_up()
        if coord1-10<coord3<coord1+10 and coord2-10<coord4<coord2+10:
            os.popen("python3 "+app+".py","r")
            pygame.quit()
            break


    distance = ((coord1-coord3)**2)+((coord2-coord4)**2)
    pygame.display.set_caption("distance : "+str(distance))




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False