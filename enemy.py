import pygame
import random
import time

#Classe des ennemis
class Enemy(pygame.sprite.Sprite):

    def __init__(self, game, max_hp, speed, attack):
        super().__init__()
        self.game = game

        self.hp = max_hp
        self.max_hp = max_hp
        self.speed = speed
        self.attack = attack
        self.image = pygame.image.load('PygameAssets/button-settings.png')
        # self.image = pygame.transform.scale(self.image, (1200,1200))
        self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect()
        self.projectileHit = 0
        self.destroy = time.time()

        # self.rect.x = 2300
        self.rect.x = 1600
        self.rect.y = random.randint(100, 800)

        self.origine_image = self.image
        self.angle = 0




# idée : changer la couleur de la barre en fonction de l'environnement
    def update_health_bar(self, surface):
        #definir la couleur de la jauge de vie
        bar_color = (255, 0, 0) #rouge
        #definir une couleur pour l'arriere plan de la jauge
        back_bar_color = (60, 60, 60)

        #definir la position de la jauge de vie + largeur+ epaisseur
        hp = (self.hp / self.max_hp) * 200
        bar_position = [self.rect.x, self.rect.y - 20, hp, 10]
        #definir la positiond e l'arrere plan de la jauge
        back_bar_position = [self.rect.x, self.rect.y - 20, 200, 10]

        #dessine la bar de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        

    def remove(self):
        self.game.all_enemy.remove(self)

    # def spawn(self):
    #     self.rect.x -= 10

    def rotation(self):
        self.angle -= 0.5
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def damage(self, amount):
        if (self.hp - amount < amount) :
            self.remove()
        else:
            self.hp -= amount

    def forward(self):
        # Tourne s'il a une vitesse initiale
        # if self.speed != 0:
        #     self.rotation()


        #mets des degats aux joueurs si collision et supprime l'ennemi
        if self.game.check_collision(self, self.game.all_players):
            self.remove()
            self.game.player.damage(self.attack)
            print(self.game.player.hp)
        else:
            self.rect.x -= self.speed


        # in self.game.check_collision(self, self.game.player.all_projectile):
        #     self.damage(self.game.player.attack)
        #     print(self.hp)

        if self.rect.x < -200:
            self.remove()

        if self.destroy + 10 < time.time():
            # while self.rect.x != 2300:
            #     self.rect.x += 10
            self.remove()
