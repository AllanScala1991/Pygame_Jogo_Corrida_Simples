import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("sprites/police.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(120,66))
        self.mask = pygame.mask.from_surface(self.image)#mask para deixar a colisao bem proxima
        self.rect = self.image.get_rect()
        self.rect[0] = 240
        self.rect[1] = 600
        
        self.velocidade = 3
        self.points = 0
        
        
    def update(self):
        pass
            
        
    
    
            