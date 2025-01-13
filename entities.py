import pygame as pg


class Entity(pg.sprite.Sprite):  # Базовый класс сущности
    def __init__(self, size: tuple, image: str, groups):
        try:
            if type(groups) != tuple:
                groups = tuple(groups)
            super().__init__(*groups)
            self.image = pg.Surface(size, pg.SRCALPHA, 32)
            self.mask = pg.mask.from_surface(self.image)
        except Exception as e:
            print(e)

# TODO Общий класс врагов, класс Player