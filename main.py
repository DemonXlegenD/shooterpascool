import pygame
import sys
import math
import time

from game import Game
from settings import Settings
#import the class Enemy from the file enemy.py

#import the class Spaceship from the file spaceship.py

from screen import *
from affichage import *

#définir une clock
clock = pygame.time.Clock()
FPS = 100

#Initialize Pygame
pygame.init()



game = Game()
settings = Settings()

# Define game varibales
scroll = 0
tiles = math.ceil(game.screen.width/game.screen.bg_width) + 1
seconde = time.time()

game.screen.show_screen()
#Boucle de jeu

running = True

while running:

    # draw scrolling background
    for i in range(0, tiles):
        game.screen.blit(game.screen.background, (i * game.screen.bg_width + scroll, 0))

    #Scroll background
    scroll -= 5

    # reset scroll
    if abs(scroll) > game.screen.bg_width:
        scroll = 0

    #  ------------------------------------------- Projectiles -------------------------------------------
    #recuperer les projectiles
    for projectile in game.player.all_projectile:
        projectile.move()

    # appliquer l'ensemble des image de mon groupe de projectile
    game.player.all_projectile.draw(game.screen)

    #  ------------------------------------------- Enemy -------------------------------------------
    #recuperer les ennemy
    for enemy in game.all_enemy:
        enemy.forward()
        enemy.update_health_bar(game.screen) 
        # while enemy.rect.x != 1600:
        #     enemy.spawn()

    # appliquer l'ensemble des image de mon groupe de mosntres
    game.all_enemy.draw(game.screen)


     #  ------------------------------------------- Game Related -------------------------------------------
    #vérifier si le jeu a commencé ou non
    if (game.is_playing and game.mode_is_choose):
        #déclencher les isntructions de la partie
        game.update(game.screen, seconde)
    #---------settings--------#
    elif(not game.is_playing and not game.mode_is_choose and not game.planete_is_choose and settings.is_settings):
        game.show_settings()
    #verifier quelles sont les settings lancés
    elif(not game.is_playing and not game.mode_is_choose and not game.planete_is_choose and settings.is_gameplay):
        game.show_gameplay()
    elif(not game.is_playing and not game.mode_is_choose and not game.planete_is_choose and settings.is_audio):
        game.show_audio()
    elif(not game.is_playing and not game.mode_is_choose and not game.planete_is_choose and settings.is_commandes):
        game.show_commandes()
        
    #Show the screen with the difficulties
    elif(not game.is_playing and not game.mode_is_choose and not game.planete_is_choose):
        game.show_planetes()

    #vérifier si notre jeu n'a pas commencé
    #Show the screen with the difficulties
    elif(not game.is_playing and not game.mode_is_choose and game.planete_is_choose):
        game.show_difficulty()
    #vérifier si notre jeu n'a pas commencé
    else:
        game.show_menu()

    #Dessin de la fenêtre
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Fermeture du jeu")
            sys.exit()
            
            
        # Faire spawn des ennemis
        if game.is_playing == True:
            
            if time.time() > seconde + 3:
                game.spawn_monster()
                seconde = time.time()

        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #détecter si la touche espace est enclenchée pour lance notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif (event.type == pygame.MOUSEBUTTONDOWN):


            #vérification pour svaoir si la souris est en collision avec le bouton
            if (game.button_play.collidepoint(event.pos)):
                game.show_planetes()

            #vérification pour svaoir si la souris est en collision avec le bouton
            elif(game.buttons_settings[0].button_rect.collidepoint(event.pos)):
                settings.show_settings()
            elif(game.buttons_settings[1].button_rect.collidepoint(event.pos)):
                settings.show_gameplay()
            elif(game.buttons_settings[3].button_rect.collidepoint(event.pos)):
                settings.show_audio()
            elif(game.buttons_settings[5].button_rect.collidepoint(event.pos)):
                settings.show_commandes()
            elif(game.buttons_settings[-1].button_rect.collidepoint(event.pos)):
                settings.back_settings()
            
            elif (game.is_planete_pressed(event)):
                game.screen_game_modes()
            
            
            elif (game.buttons_difficulties[0].button_rect.collidepoint(event.pos)):
                game.create_player(1)
                game.start()

            elif (game.buttons_difficulties[0].button_rect.collidepoint(event.pos)):
                game.create_player(1.5)

                game.start()
            elif game.buttons_difficulties[0].button_rect.collidepoint(event.pos):
                game.create_player(2)

                game.start()
            elif (game.buttons_difficulties[0].button_rect.collidepoint(event.pos)):
                game.create_player(3)

                game.start()
                
                #mettre le jeu en monde "lancé"
                

           
    #fixer le nombre de fps sur ma clock
    clock.tick(FPS)  
