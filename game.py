import pygame, os
from pygame.locals import *
import pytmx
from pytmx import TiledImageLayer
from pytmx import TiledObjectGroup
from pytmx import TiledTileLayer
from pytmx.util_pygame import load_pygame
from scripts.mapa import Mapa
from scripts.player import Player
from scripts.objects import Street_Ground, Trees, Trees2
from scripts.cars import Red_Car, White_Car, Black_Car

class Game():
    def __init__ (self):
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        self.janela = pygame.display.set_mode((640,736))#pygame.FULLSCREEN - pygame.HWSURFACE

        self.game_font = pygame.font.Font("fonts/font1.ttf",40)
        self.arcade_font = pygame.font.Font("fonts/Arcade.ttf",30)
        
        #SOUNDS
        pygame.mixer.init()
        self.game_music = pygame.mixer.Sound("sounds/game_music.wav")
        self.sucess = pygame.mixer.Sound("sounds/success.wav")
        pygame.mixer.Channel(0).play(self.game_music, -1)


        self.mapa = Mapa()
        self.mapa_img = self.mapa.make_map()
        self.mapa_rect = self.mapa_img.get_rect()


        self.player = Player()
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)
        self.move_right = False
        self.move_left = False
        self.get_points = self.player.points
        self.level = 1
        

        self.street_ground = Street_Ground()
        self.tree = Trees()
        self.tree2 = Trees2()
        self.objects_group = pygame.sprite.Group()
        self.objects_group.add(self.street_ground, self.tree, self.tree2)

        self.red_car = Red_Car()
        self.white_car = White_Car()
        self.black_car = Black_Car()
        self.cars_group = pygame.sprite.Group()
        self.cars_group.add(self.red_car, self.white_car, self.black_car)
        self.velocidade_carros = 2


        #LOOP DO JOGO
        self.racing = True
        self.gaming = True
        self.game_over = False
        self.winner = False
        self.fps = pygame.time.Clock()
        
        while self.racing:
            self.fps.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    
                if event.type == KEYDOWN:
                    if event.key == K_p: # pausa o game
                        self.gaming = False
                        self.janela.fill((0,0,0))
                        self.pause_text = self.game_font.render("JOGO PAUSADO",1,(255,255,255))
                        self.return_text = self.game_font.render("PARA RETORNAR AO JOGO PRESSIONE 'i' ",1,(255,255,255))
                        self.janela.blit(self.pause_text,(200,300))
                        self.janela.blit(self.return_text,(50,500))
                    if event.key == K_i:# despausa o game
                        self.gaming = True
                    if self.game_over:
                        if event.key == K_r:
                                Game()
                                pygame.quit()
                                            
                    if self.gaming:
                        if event.key == K_LEFT:
                            self.move_left = True
                        if event.key == K_RIGHT:
                            self.move_right = True
                            
                if event.type == KEYUP:
                    if self.gaming:
                        if event.key == K_LEFT:
                            self.move_left = False
                        if event.key == K_RIGHT:
                            self.move_right = False
                            
            if self.gaming: # verifica se nao pausou
                if self.move_left:
                    self.player.rect[0] -= self.player.velocidade
                if self.move_right:
                    self.player.rect[0] += self.player.velocidade
                
                self.janela.blit(self.mapa_img, self.mapa_rect)
                self.objects_group.draw(self.janela)
                if self.street_ground.rect[1] >= 240:
                    self.street_ground = Street_Ground()
                    self.objects_group.add(self.street_ground)
                    self.street_ground.rect[1] = -30
                if self.street_ground.rect[1] >=740:
                    self.objects_group.remove(street_ground)
                
                if self.tree.rect[1] >= 30:
                    self.tree = Trees()
                    self.objects_group.add(self.tree)
                    self.tree.rect[1] = -150
                if self.tree.rect[1] >=740:
                    self.objects_group.remove(self.tree)
                    
                if self.tree2.rect[1] >= 50:
                    self.tree2 = Trees2()
                    self.objects_group.add(self.tree2)
                    self.tree2.rect[1] = -150
                if self.tree2.rect[1] >=740:
                    self.objects_group.remove(self.tree2)

                if self.red_car.rect[1] == 790:
                    self.red_car = Red_Car()
                    self.cars_group.add(self.red_car)
                    self.red_car.rect[1] = -200
                if self.red_car.rect[1] >=800:
                    self.cars_group.remove(self.red_car)
                
                if self.white_car.rect[1] == 790:
                    self.white_car = White_Car()
                    self.cars_group.add(self.white_car)
                    self.white_car.rect[1] = -500
                if self.white_car.rect[1] >=800:
                    self.cars_group.remove(self.white_car)
                
                if self.black_car.rect[1] == 790:
                    self.black_car = Black_Car()
                    self.cars_group.add(self.black_car)
                    self.black_car.rect[1] = -800
                if self.black_car.rect[1] >=800:
                    self.cars_group.remove(self.black_car)
                
                if self.red_car.rect[1] == 650 or self.white_car.rect[1] == 650 or self.black_car.rect[1] == 650:
                    pygame.mixer.Channel(1).play(self.sucess, 0)
                    self.get_points += 1
                if self.get_points > 20:
                    self.level = 2
                    self.velocidade_carros = 2
                if self.get_points > 60:
                    self.level = 3
                    self.velocidade_carros = 3
                if self.get_points > 100:
                    self.level = 4
                    self.velocidade_carros = 4
                if self.get_points > 150:
                    self.level = 5
                    self.velocidade_carros = 5
                if self.get_points > 200:
                    self.level = 6
                    self.velocidade_carros = 6
                if self.get_points > 400:
                    self.level = 7
                    self.velocidade_carros = 7
                if self.get_points > 600:
                    self.level = 8
                    self.velocidade_carros = 8
                if self.get_points > 800:
                    self.level = 9
                    self.velocidade_carros = 9
                if self.get_points > 1000:
                    self.level == "FINAL LEVEL"
                    self.velocidade_carros = 10
                if self.get_points == 2000:
                    self.winner = True
                
            
                self.cars_group.draw(self.janela)
                self.cars_group.update(self.velocidade_carros)    
                self.player_group.draw(self.janela)
                self.player_group.update()
                self.objects_group.update()
                
                for layer in self.mapa.mapa_data.visible_layers:
                    if isinstance(layer,pytmx.TiledObjectGroup):
                                if layer.name == "collider":
                                    for obj in layer:
                                        if pygame.Rect(obj.x, obj.y, obj.width, obj.height).colliderect(self.player.rect) == True:
                                            if self.move_left:
                                                self.player.rect[0] += self.player.velocidade
                                            if self.move_right:
                                                self.player.rect[0] -= self.player.velocidade
            
            self.points_text = self.arcade_font.render("PONTOS : " + str(self.get_points),1,(255,0,0))
            self.janela.blit(self.points_text,(260,25))
            self.level_text = self.arcade_font.render("LEVEL : " + str(self.level),1,(255,255,0))
            self.janela.blit(self.level_text,(260,50))
            
            if self.game_over:
                self.gaming = False
                self.janela.fill((0,0,0))
                self.game_over_text = self.game_font.render("VOCE PERDEU",1,(255,255,255))
                self.game_over_text2 = self.game_font.render("PRESSIONE 'R' PARA RECOMECAR ",1,(255,255,255))
                self.janela.blit(self.game_over_text,(200,300))
                self.janela.blit(self.game_over_text2,(90,500))
                
            if self.winner:
                self.gaming = False
                self.janela.fill((0,0,0))
                self.game_over_text = self.game_font.render("PARABENS, VOCE VENCEU!",1,(255,255,255))
                self.game_over_text2 = self.game_font.render("PRESSIONE 'R' PARA RECOMECAR ",1,(255,255,255))
                self.janela.blit(self.game_over_text,(200,300))
                self.janela.blit(self.game_over_text2,(90,500))
                
            
            #mask para deixar a colisao bem proxima    
            if (pygame.sprite.groupcollide(self.player_group, self.cars_group,False,False,pygame.sprite.collide_mask)):
                self.game_over = True
                      
            pygame.display.update()
Game()
