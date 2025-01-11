import sys

import pygame as pg


def get_config():  # Считывает настройки из файла config
    try:
        with open('config.cfg', 'r') as f:
            settings = {}
            for i in f.read().split('\n'):
                i = i.split(' = ')
                settings[i[0]] = int(i[1])
            return settings
    except FileNotFoundError:
        print('config.cfg not found')
        sys.exit()  # TODO Сделать восстановление cfg при повреждении/утрате


def main():
    settings = get_config()
    try:
        pg.init()
        screen = pg.display.set_mode((settings['win_width'], settings['win_height']))
    except TypeError:
        print('config error')
        pg.quit()
    all_sprites = pg.sprite.Group()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

    pg.quit()  # TODO scoreboard вместо quit


if __name__ == '__main__':
    main()
