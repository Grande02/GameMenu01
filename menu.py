import pygame
import button

#create display window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()
options_img = pygame.image.load('start_btn.png').convert_alpha()
#create button instances
start_button = button.Button(290, 300, start_img, 0.5)
exit_button = button.Button(300, 400, exit_img, 0.5)
options_button = button.Button(300, 500, options_img, 0.5)
#game loop
run = True


def game():
    pass
def options():
    pass


while run:

    screen.fill((202, 228, 241))

    if start_button.draw(screen):
        game()
    if exit_button.draw(screen):
        run = False
    if options_button.draw(screen):
        options()
    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

def game():
    running = True
    while running:
        screen.fill((202, 228, 241))

        if start_button.draw(screen):
            game()

        if options_button.draw(screen):
            options()
            # event handler
        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()


def options():
    running = True
    while running:
        screen.fill((202, 228, 241))

    if exit_button.draw(screen):
        run = False
    if options_button.draw(screen):
        options()
        # event handler
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

    pygame.quit()
