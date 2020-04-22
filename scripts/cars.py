import pygame,random
from pygame.locals import *


class Red_Car(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("sprites/car_red.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(120,66))
        self.mask = pygame.mask.from_surface(self.image)#mask para deixar a colisao bem proxima
        self.rect = self.image.get_rect()
        self.direction = [190,255,325]
        self.rect[0] = random.choice(self.direction)
        self.rect[1] = -200
        
        
        
    def update(self, velocidade):
        self.rect[1] += velocidade

class White_Car(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("sprites/car_white.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(120,66))
        self.mask = pygame.mask.from_surface(self.image)#mask para deixar a colisao bem proxima
        self.rect = self.image.get_rect()
        self.direction = [190,255,325]
        self.rect[0] = random.choice(self.direction)
        self.rect[1] = -500
        
        
        
    def update(self, velocidade):
        self.rect[1] += velocidade

class Black_Car(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("sprites/car_black.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(100,56))
        self.mask = pygame.mask.from_surface(self.image) #mask para deixar a colisao bem proxima
        self.rect = self.image.get_rect()
        self.direction = [180,265,330]
        self.rect[0] = random.choice(self.direction)
        self.rect[1] = -800
        
        
        
    def update(self, velocidade):
        self.rect[1] += velocidade