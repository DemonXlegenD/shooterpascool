import pygame
import math

#Initialisation des dimensions de la fenêtre
largeur = 1920
hauteur = 1080

class Screen:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.bg_width = w
        self.bg_height = h 
        self.background = pygame.image.load('PygameAssets/bgspace.jpg')
        self.background = pygame.transform.scale(self.background, (self.bg_width, self.bg_height))
        self.banner = pygame.image.load('PygameAssets/banner.png')
        self.banner = pygame.transform.scale(self.banner, (500, 500))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.x = math.ceil(self.screen.get_width()/3)

    def show_screen(self):
        pygame.display.set_caption("Shoot'em up")
        self.screen = pygame.display.set_mode((self.width, self.height))
        banner = pygame.image.load('PygameAssets/banner.png')
        banner = pygame.transform.scale(banner, (500, 500))
        banner_rect = banner.get_rect()
        banner_rect.x = math.ceil(self.screen.get_width()/3)

    def change_bg(self, path):
        self.background = pygame.image.load(path)
        self.background = pygame.transform.scale(self.background, (self.bg_width, self.bg_height))