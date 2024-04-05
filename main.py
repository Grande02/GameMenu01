import button
import pygame
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Science Academy")

menu_state = "menu"  #game variables
clock = pygame.time.Clock()
FPS = 30

#define
font = pygame.font.SysFont("arial black", 40)
TEXT_COL = (255, 255, 255)

#load images
start_img = pygame.image.load('assets/button_start.png').convert_alpha()
resume_img = pygame.image.load("assets/button_start.png").convert_alpha()
options_img = pygame.image.load("assets/button_option.png").convert_alpha()
quit_img = pygame.image.load("assets/button_quit.png").convert_alpha()
music_img = pygame.image.load('assets/button_music.png').convert_alpha()
sound_img = pygame.image.load('assets/button_sound.png').convert_alpha()
keys_img = pygame.image.load('assets/button_key.png').convert_alpha()
back_img = pygame.image.load('assets/button_back.png').convert_alpha()
title_img = pygame.image.load('assets/title.png').convert_alpha()
bg = pygame.image.load("assets/bg.png").convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()

scroll = 0
tiles = math.ceil(SCREEN_WIDTH/ bg_width) + 1

#create button instances
start_button = button.Button(320, 275, start_img, 0.5)
options_button = button.Button(320, 375, options_img, 0.5)
quit_button = button.Button(320, 475, quit_img, 0.5)
resume_button = button.Button(320, 125, resume_img, 0.5)
music_button = button.Button(320, 75, music_img, 0.5)
sound_button = button.Button(320, 200, sound_img, 0.5)
keys_button = button.Button(320, 325, keys_img, 0.5)
back_button = button.Button(320, 450, back_img, 0.5)
title_button = button.Button(280, 30, title_img, 0.5)
back_button2 = button.Button(220, 330, back_img, 0.5)
quit_button2 = button.Button(420, 330, quit_img, 0.5)


def draw_text(text, fonts, text_col, x, y):
    img = fonts.render(text, True, text_col)
    screen.blit(img, (x, y))


#game loop
run = True
while run:

    clock.tick(FPS)

    # draw scrolling background
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))
        bg_rect.x = i * bg_width + scroll

    # scroll background
    scroll -= 5

    # reset scroll
    if abs(scroll) > bg_width:
        scroll = 0
    #screen.fill((202, 228, 241))

    if menu_state == "menu":
        if title_button.draw(screen):
            pass
        if start_button.draw(screen):
            menu_state = "start"
        if options_button.draw(screen):
            menu_state = "options"
        if quit_button.draw(screen):
            menu_state = "quit"

    if menu_state == "start":
        draw_text("START", font, TEXT_COL, 335, 250)
        if back_button.draw(screen):
            menu_state = "menu"

    if menu_state == "options":
        if music_button.draw(screen):
            menu_state = "music"
        if sound_button.draw(screen):
            menu_state = "sound"
        if keys_button.draw(screen):
            menu_state = "keys"
        if back_button.draw(screen):
            menu_state = "menu"

    if menu_state == "sound":
        draw_text("Sound Effects Setting", font, TEXT_COL, 200, 250)
        if back_button.draw(screen):
            menu_state = "options"

    if menu_state == "music":
        draw_text("BackGround Music", font, TEXT_COL, 200, 250)
        if back_button.draw(screen):
            menu_state = "options"

    if menu_state == "keys":
        draw_text("Change Key Binds", font, TEXT_COL, 200, 250)
        if back_button.draw(screen):
            menu_state = "options"

    if menu_state == "pause":
        # draw pause screen buttons
        draw_text("press \"esc\" key to continue", font, TEXT_COL, 100, 250)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                menu_state = "start"

    if menu_state == "quit":
        draw_text("Are you sure you wanna quit?", font, TEXT_COL, 100, 250)
        if back_button2.draw(screen):
            menu_state = "menu"
        if quit_button2.draw(screen):
            run = False

    #events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu_state = "pause"
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
