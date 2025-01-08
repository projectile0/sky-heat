import sys

import pygame


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
        pygame.init()
        screen = pygame.display.set_mode((settings['win_width'], settings['win_height']))
    except TypeError:
        print('config error')
        pygame.quit()
    all_sprites = pygame.sprite.Group()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()  # TODO scoreboard вместо quit


if __name__ == '__main__':
    main()
