import os
import random
import pygame

WORK_DIR = os.path.split(os.path.abspath(__file__))[0]
DATA_DIR = os.path.join(WORK_DIR, 'data')
print('Work dir:', WORK_DIR)

pygame.init()
screen = pygame.display.set_mode((400, 640))
pygame.display.set_caption('Super Gra Grzesia')

def load_image(filename):
    filepath = os.path.join(DATA_DIR, filename)
    surface = pygame.image.load(filepath)
    return surface

def load_font(filename, size):
    filepath = os.path.join(DATA_DIR, filename)
    font = pygame.font.Font(filepath, size)
    return font

background = load_image('background.png')
elements_names = ['python_logo.png', 'pyladies_head.png', 'ninja.png', 'moon.png']
elements = [load_image(i) for i in elements_names]
font_nokia = load_font('nokiafc22.ttf', 128)
font_game_over = load_font('nokiafc22.ttf', 32)

class Ring:
    values = [0, 1, 2, 3]
    pair = [0, 1]

    def __init__(self):
        self.new_level()

    def new_level(self):
        arr = [0, 1, 2, 3]
        first = random.choice(arr)
        arr.remove(first)
        second = random.choice(arr)
        self.pair = [first, second]

    def rotate_ccw(self):
        self.values = self.values[1:] + [self.values[0]]

    def rotate_cw(self):
        self.values = [self.values[-1]] + self.values[:-1]

    def swap_top(self):
        # a, b = b, a
        self.values[0], self.values[1] = self.values[1], self.values[0]

    def match(self):
        return self.pair == self.values[0:2]

    def debug_print(self):
        print(self.pair, '?', self.values)

ring = Ring()
ring.debug_print()
mainloop = True
score = 0
clock = pygame.time.Clock()
level_time = 0
max_level_time = 2500  # ms
game_over = False

RING_X = 100
RING_Y = 400
TILE = 90
GAP = 16

while mainloop:

    miliseconds = clock.tick(60)  # FPS = 60

    if not game_over:
        level_time = level_time + miliseconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                mainloop = False
            elif event.key == pygame.K_UP:
                ring.swap_top()
                ring.debug_print()
            elif event.key == pygame.K_LEFT:
                ring.rotate_ccw()
                ring.debug_print()
            elif event.key == pygame.K_RIGHT:
                ring.rotate_cw()
                ring.debug_print()
            elif event.key == pygame.K_r:
                if game_over:
                    game_over = False
                    ring.new_level()
                    level_time = 0

    # update
    if level_time > max_level_time:
        level_time = level_time - max_level_time
        if ring.match():
            score += 10
            print('Good!', score)
        else:
            score = 0
            print('You suck...')
            game_over = True
        ring.new_level()
        ring.debug_print()

    time_prop = level_time / max_level_time

    score_txt = str(score)
    score_size = font_nokia.size(score_txt)
    score_x = 400 // 2 - score_size[0] // 2
    score_y = 640 // 2 - score_size[1] // 2

    red = 55 + int(200 * time_prop)
    score_surface = font_nokia.render(score_txt, True, (red, 200, 220))
    shadow_surface = font_nokia.render(score_txt, True, (100, 100, 120))

    # blity
    screen.blit(background, (0, 0))

    if not game_over:
        screen.blit(shadow_surface, (score_x + 8, score_y + 8))
        screen.blit(score_surface, (score_x, score_y))

        # np: ring.values → 0, 2, 1, 3
        # elements = [surf, surf, surf, surf]
        screen.blit(elements[ring.values[0]], (RING_X,              RING_Y))
        screen.blit(elements[ring.values[1]], (RING_X + TILE + GAP, RING_Y))
        screen.blit(elements[ring.values[2]], (RING_X + TILE + GAP, RING_Y + TILE + GAP))
        screen.blit(elements[ring.values[3]], (RING_X,              RING_Y + TILE + GAP))

        # 0 → RING_Y
        pos_y = RING_Y * time_prop
        screen.blit(elements[ring.pair[0]], (RING_X, pos_y))
        screen.blit(elements[ring.pair[1]], (RING_X + TILE + GAP, pos_y))
    else:
        game_over_surface = font_game_over.render('GAME OVER', True, (200, 200, 200))
        screen.blit(game_over_surface, (40, 40))

    info = font_game_over.render('Q - quit', True, (0, 220, 30))
    screen.blit(info, (100, 0))

    pygame.display.flip()

pygame.quit()
