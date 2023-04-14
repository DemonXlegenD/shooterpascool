import pygame

#definir la classe qui va gerer le projectile du joueur

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.speed = 15
        self.player = player
        self.damage = 15
        self.image = pygame.image.load('PygameAssets/Missile-Transparent.png')
        self.image = pygame.transform.scale(self.image, (120,30))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80

    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self) : 
        self.rect.x += self.speed
       
        #verif si collision monstre
        for enemy in self.player.game.check_collision(self, self.player.game.all_enemy):
            self.remove()
            #Mettre les damages ici
            enemy.damage(self.player.attack)
            
            

        #verifier si le projectile n'est plus présent sur l'ecran
        if self.rect.x > 1920:
            self.remove()
            