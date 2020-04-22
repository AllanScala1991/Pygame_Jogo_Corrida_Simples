import pygame
from pygame.locals import *
import pytmx
from pytmx import TiledImageLayer
from pytmx import TiledObjectGroup
from pytmx import TiledTileLayer
from pytmx.util_pygame import load_pygame


class Mapa():
    def __init__(self):
        self.mapa = load_pygame("sprites/street.tmx") # LE O MAPA
        self.mapa_width = self.mapa.width * self.mapa.tilewidth # DEFINE SEU WIDTH
        self.mapa_height = self.mapa.height * self.mapa.tileheight # DEFINE SEU HEIGHT
        self.mapa_data = self.mapa # DEFINI SUA DATA
        
    def render(self, surface): # FUNCAO PARA RENDERIZAR O MAPA
        ti = self.mapa_data.get_tile_image_by_gid
        for layer in self.mapa_data.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile,(x * self.mapa_data.tilewidth, y*self.mapa_data.tileheight))
            
    def make_map(self): # FUNCAO PARA DESENHAR O MAPA
        temp_surface = pygame.Surface((self.mapa_width, self.mapa_height))
        self.render(temp_surface)
        return temp_surface