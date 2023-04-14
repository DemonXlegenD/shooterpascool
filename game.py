import pygame
import time
import random
from screen import Screen
from spaceship import Spaceship
from enemy import Enemy
from button import Button

#créer une classe qui va représenter notre jeu
class Game:

    def __init__(self):
        self.screen = Screen(1920, 1080)
        #définir si notre jeu a commencé ou non
        self.is_playing = False
        self.mode_is_choose = False
        self.planete_is_choose = False
        self.difficulty = 1
        #générer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Spaceship(self, 200,15,15)
        self.all_players.add(self.player)

        self.pressed = {}

        self.button_play = Button(self.screen, 2.7, 1.7, 400, 150,'PygameAssets/button.png')

        #=====================================================================================================================#
        #------------------------------------------------------PLANETES-------------------------------------------------------#
        #=====================================================================================================================#

        self.buttons_planetes = [
            Button(self.screen, 1.5, 2.50, 300, 300,'PygameAssets/terre.png'), 
            Button(self.screen, 2, 1.5, 200, 200,'PygameAssets/planete1.png'), 
            Button(self.screen, 1.80, 7.5, 250, 250,'PygameAssets/planete2.png'),
            Button(self.screen, 2.5, 3, 200, 200,'PygameAssets/planete3.png'),
            Button(self.screen, 8, 1.5, 450, 300,'PygameAssets/planete4.png'),
            Button(self.screen, 1.20, 8.5, 175, 175,'PygameAssets/planete5.png'),
            Button(self.screen, 1.25, 1.25, 150, 150,'PygameAssets/planete6.png')
            ]
        
        #=====================================================================================================================#
        #------------------------------------------------------SETTINGS-------------------------------------------------------#
        #=====================================================================================================================#

        self.buttons_settings = [
            Button(self.screen, 100, 100, 50, 50,'PygameAssets/button-settings.png'),
            Button(self.screen, 10.15, 4, 200, 150,'PygameAssets/Gameplay.png'),
            Button(self.screen, 10.15, 4, 200, 150,'PygameAssets/Gameplay_underline.png'),
            Button(self.screen, 2.25, 4, 200, 150,'PygameAssets/audio_underline.png'),
            Button(self.screen, 1.3, 4, 200, 150,'PygameAssets/controle.png'),
            Button(self.screen, 1.3, 4, 200, 150,'PygameAssets/controle_underline.png'),
            Button(self.screen, 100, 100, 100, 100,'PygameAssets/retour.png')
        ]

        #=====================================================================================================================#
        #---------------------------------------------------DIFFICULTIES------------------------------------------------------#
        #=====================================================================================================================#

        self.buttons_difficulties = [
            Button(self.screen, 3, 6, 500, 150,'PygameAssets/easy-button.png'),
            Button(self.screen, 3, 3, 500, 150,'PygameAssets/medium-button.png'),
            Button(self.screen, 3, 2, 500, 150,'PygameAssets/hard-button.png'),
            Button(self.screen, 3, 1.5, 500, 150,'PygameAssets/nightmare-button.png')
        ]
        #groupe de monstres
        self.all_enemy = pygame.sprite.Group()

        #mettre le score a 0
        self.score = 0
        self.font = pygame.font.Font("Roboto/Roboto-Bold.ttf", 25)
        #gérer le son
        # self.sound_manager = SoundManager()
    
    # def test_score(self):
        # self.load_score.new_score = self.score
        # self.load_score.check_update()
        # if self.loard_score.name_needed:
            
        


    def create_player(self, difficulty):
        #générer notre joueur
        self.difficulty = difficulty
        self.all_players = pygame.sprite.Group()
        self.player = Spaceship(self, 200/self.difficulty, 10, 30/self.difficulty)
        self.all_players.add(self.player)

    #Condition
    def screen_game_modes(self):
        self.mode_is_choose = False
        self.planete_is_choose = True
    
    def show_settings(self):
        self.buttons_settings[1].show_button()
        self.buttons_settings[3].show_button()
        self.buttons_settings[5].show_button()
        self.buttons_settings[6].show_button()

    #Affiche l'écran les modes
    def show_game_modes(self):
        for difficulty in self.buttons_difficulties:
            difficulty.show_button()

    def screen_planetes(self):
        self.planete_is_choose = True
        self.mode_is_choose = False


    def show_planetes(self):
        for planete in self.buttons_planetes:
            planete.show_button()

    def is_planete_pressed(self, event):
        for planete in self.buttons_planetes:
            planete.is_button_pressed(event)

    def is_difficulty_pressed(self, event):
        for difficulty in self.buttons_difficulties:
            difficulty.is_button_pressed(event)



    def start(self):
        self.is_playing = True
        


    def game_over(self):
        #remettre le jeu à neuf, retirer les monstres, remettre les joueurs à 100 de vie, jeu en attente
        self.all_enemy = pygame.sprite.Group()
        self.player.hp = self.player.max_hp
        self.is_playing = False
        self.score = 0

    def add_score(self, points = 10):
        self.score += points

    def update(self, screen, seconde):

        #afficher le score sur l'écran  
        score_text = self.font.render(f"Score : {self.score}", 1, (255, 255, 255))
        screen.blit(score_text, (20, 20))

        #appliquer l'image de notre joueur
        screen.blit(self.player.image, self.player.rect)
            
        # Spawn ennemis
        if time.time() > seconde + 30:
            self.spawn_monster()
            seconde = time.time()


        # #actualiser la barre de vie du joueur
        # self.player.update_health_bar(screen)

        # #actualiser la barre d'évenement du jeu
        # self.comet_event.update_bar(screen)

        # #animer joueurs
        # self.player.update_animation()
        

        # #récuperer les projectiles du joueurs
        # for projectile in self.player.all_projectiles:
        #     projectile.move()

        # #récuperer les monstres du jeu
        # for monster in self.all_monsters:
        #     monster.forward()
        #     monster.update_health_bar(screen)
        #     monster.update_animation()

        #récuperer les comètes du jeu
        # for comet in self.comet_event.all_comets:
        #     comet.fall()

        # #appliquer l'ensemble des images de mon groupe de projectiles
        # self.player.all_projectiles.draw(screen)

        # #appliquer l'ensemble des images de mon groupe de monstres
        # self.all_monsters.draw(screen)

        # #appliquer l'ensemble des images de mon groupe de comètes
        # self.comet_event.all_comets.draw(screen)

        #vérifier si le joueur souhaite aller à gauche ou à droite
        if (self.pressed.get(pygame.K_RIGHT) or self.pressed.get(pygame.K_d)) and self.player.rect.x + self.player.rect.width<= screen.get_width():
            self.player.move_right()
        if (self.pressed.get(pygame.K_LEFT) or self.pressed.get(pygame.K_q)) and self.player.rect.x >= 0 :
            self.player.move_left()
        if (self.pressed.get(pygame.K_DOWN) or self.pressed.get(pygame.K_s)) and self.player.rect.y + self.player.rect.height<= screen.get_height():
            self.player.move_down()
        if (self.pressed.get(pygame.K_UP) or self.pressed.get(pygame.K_z)) and self.player.rect.y >= 0 :
            self.player.move_up()



    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster(self):
        enemy_number = random.randint(1, 2)
        print("number", enemy_number)

        for i in range(1, enemy_number):

            enemy_spawn = random.randint(0,1)
            print("spawn", enemy_spawn)

            if enemy_spawn == 0:
                print("0")
                # Ennemi de collision
                enemy = Enemy(self, 100*self.difficulty, 2*self.difficulty, 20*self.difficulty)
            elif enemy_spawn == 1:
                print("1")
                # Ennemi one shot
                enemy = Enemy(self, 10*self.difficulty, 0, 5000)

            self.all_enemy.add(enemy)