#!/usr/bin/python3

import os
import random
import pygame

MAIN_DIR = os.path.split(os.path.abspath(__file__))[0]

CONFIG = {
    'game_size': (400, 640),
    'fps': 60,
    'max_level_time': 2500,
    'text_color': (200, 200, 220),
    'text_shadow': (100, 100, 100)
}

ELEM_SIZE = 90
ELEM_GAP = 16

RING_X = (CONFIG['game_size'][0] - (2 * ELEM_SIZE + ELEM_GAP)) // 2
RING_Y = CONFIG['game_size'][1] - 2 * ELEM_SIZE - 4 * ELEM_GAP

ELEM_POSITION = (
    (RING_X, RING_Y),
    (RING_X + ELEM_GAP + ELEM_SIZE, RING_Y),
    (RING_X + ELEM_GAP + ELEM_SIZE, RING_Y + ELEM_GAP + ELEM_SIZE),
    (RING_X, RING_Y + ELEM_GAP + ELEM_SIZE)
)

def load_image(filename):
    filepath = os.path.join(MAIN_DIR, 'data', filename)
    surface = pygame.image.load(filepath)
    return surface

def load_images(*filenames):
    images = []
    for filename in filenames:
        images.append(load_image(filename))
    return images

def load_font(filename, size):
    filepath = os.path.join(MAIN_DIR, 'data', filename)
    font = pygame.font.Font(filepath, size)
    return font


class Ring:
    def __init__(self):
        self.values = [0, 1, 2, 3]
        self.pair = (0, 1)
        self.new_level()

    def new_level(self):
        arr = [0, 1, 2, 3]
        first = random.choice(arr)
        arr.remove(first)
        second = random.choice(arr)
        self.pair = (first, second)

    def rotate_cw(self):
        self.values = [self.values[-1]] + self.values[:-1]

    def rotate_ccw(self):
        self.values = self.values[1:] + [self.values[0]]

    def swap_top(self):
        self.values[0], self.values[1] = self.values[1], self.values[0]

    def match(self):
        return list(self.pair) == self.values[0:2]

    def debug_print(self):
        print(self.pair, '?', self.values)


class PyDrop:
    def __init__(self):
        self.ring = Ring()
        self.score = 0
        self.ring.debug_print()
        self.mainloop = True

        pygame.init()
        pygame.display.set_caption('PyDrop')

    def __del__(self):
        pygame.quit()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Quit')
                self.mainloop = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                print('You pressed Q')
                self.mainloop = False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.ring.swap_top()
                self.ring.debug_print()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.ring.rotate_cw()
                self.ring.debug_print()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.ring.rotate_ccw()
                self.ring.debug_print()

    def run(self):
        level_time = 0
        clock = pygame.time.Clock()
        font_nokia = load_font('nokiafc22.ttf', 128)
        background = load_image('background.png')
        elements = load_images('python_logo.png', 'pyladies_head.png', 'ninja.png', 'moon.png')
        screen = pygame.display.set_mode(CONFIG['game_size'])

        while self.mainloop:

            miliseconds = clock.tick(CONFIG['fps'])
            level_time = level_time + miliseconds

            self.event_loop()

            if level_time >= CONFIG['max_level_time']:
                if not self.ring.match():
                    print('Bad...')
                    self.score = 0
                else:
                    print('Good!')
                    self.score = self.score + 1
                level_time = 0
                self.ring.new_level()
                self.ring.debug_print()

            screen.blit(background, (0, 0))

            score_txt = '{}'.format(self.score)
            score_size = font_nokia.size(score_txt)
            score_x = (CONFIG['game_size'][0] - score_size[0]) // 2
            score_y = (CONFIG['game_size'][1] - score_size[1]) // 3
            score_surface = font_nokia.render(score_txt, True, CONFIG['text_color'])
            score_shadow_surface = font_nokia.render(score_txt, True, CONFIG['text_shadow'])

            screen.blit(score_shadow_surface, (score_x + 8, score_y + 8))
            screen.blit(score_surface, (score_x, score_y))

            for i in range(4):
                elem_index = self.ring.values[i]
                screen.blit(elements[elem_index], ELEM_POSITION[i])

            first, second = self.ring.pair
            pair_pos_y = RING_Y * (level_time / CONFIG['max_level_time'])
            screen.blit(elements[first], (ELEM_POSITION[0][0], pair_pos_y))
            screen.blit(elements[second], (ELEM_POSITION[1][0], pair_pos_y))

            pygame.display.flip()


PyDrop().run()
