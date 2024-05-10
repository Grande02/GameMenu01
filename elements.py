import pygame, sys
import math
import button


WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

#bg variables
bg = pygame.image.load("assets/bg.png").convert()
clock = pygame.time.Clock()
FPS = 30
scroll = 0
bg_width = bg.get_width()
bg_rect = bg.get_rect()
tiles = math.ceil(WIDTH / bg_width) + 1


def bgRoll():
    clock.tick(FPS)

    # draw scrolling background
    for i in range(0, tiles):
        global scroll
        SCREEN.blit(bg, (i * bg_width + scroll, 0))
        bg_rect.x = i * bg_width + scroll

    # scroll background
    scroll -= 5

    # reset scroll
    if abs(scroll) > bg_width:
        scroll = 0
    # screen.fill((202, 228, 241))


def draw_text(text, fonts, text_col, x, y):
    img = fonts.render(text, True, text_col)
    SCREEN.blit(img, (x, y))
