import pygame, random
from pygame.locals import *

class Street_Ground(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("sprites/street_color.png")
        self.rect = self.image.get_rect()
        self.rect[0] = 320
        self.rect[1] = -30
        
        self.velocidade = 10
               
    def update(self):
        self.rect[1] += self.velocidade
        
class Trees(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("sprites/tree.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(118,182))
        self.rect = self.image.get_rect()
        self.rect[0] = random.randint(5, 90)
        self.rect[1] = -150
        
        self.velocidade = 1      
        
    def update(self):
        self.rect[1] += self.velocidade

class Trees2(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("sprites/tree2.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(118,182))
        self.rect = self.image.get_rect()
        self.rect[0] = random.randint(390, 620)
        self.rect[1] = -150
        
        self.velocidade = 1
             
    def update(self):
        self.rect[1] += self.velocidade



            