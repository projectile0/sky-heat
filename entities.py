import pygame as pg
class Entity(pg.sprite.Sprite):
    def __init__(self, size: tuple, image: string):
        try:
            super().__init__(all_sprites)
            self.image = pg.Surface