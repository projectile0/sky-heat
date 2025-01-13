import pygame as pg
from utils import load_image


class Entity(pg.sprite.Sprite):  # Базовый класс сущности
    def __init__(self, size: tuple, image: str, groups):
        try:
            if type(groups) != tuple:
                groups = tuple(groups)
            super().__init__(*groups)
            self.image = pg.Surface(size, pg.SRCALPHA, 32)
            self.mask = pg.mask.from_surface(self.image)
            self.image = load_image(image, colorkey=-1)
        except Exception as e:
            print(e)


class Plane(Entity):
    def __init__(self, size: tuple, image: str, groups, fire_rate=1):
        super().__init__(size, image, groups)
        self.fire_rate = fire_rate


class Player(Plane):
    def __init__(self, size: tuple, image: str, groups, fire_rate=1):
        super().__init__(size, image, groups, fire_rate)
    # TODO Общий класс врагов, класс Player
