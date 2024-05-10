import pygame, button
from elements import WIDTH, HEIGHT

#immageloads
start_img = pygame.image.load('assets/button_start.png').convert_alpha()
title_img = pygame.image.load('assets/title.png').convert_alpha()
back_img = pygame.image.load('assets/button_back.png').convert_alpha()
quit_img = pygame.image.load("assets/button_quit.png").convert_alpha()
options_img = pygame.image.load("assets/button_option.png").convert_alpha()
music_img = pygame.image.load('assets/button_music.png').convert_alpha()
resume_img = pygame.image.load("assets/button_resume.png").convert_alpha()

#lvlpics
lec_1 = pygame.image.load("assets/Lec1.png").convert_alpha()
lec_2 = pygame.image.load("assets/Lec2.png").convert_alpha()
sum_1 = pygame.image.load("assets/Sum1.png").convert_alpha()
sum_2 = pygame.image.load("assets/Sum2.png").convert_alpha()
exam_1 = pygame.image.load("assets/exam1.png").convert_alpha()

save_1 = pygame.image.load("assets/save1.png").convert_alpha()
save_2 = pygame.image.load("assets/save2.png").convert_alpha()
save_3 = pygame.image.load("assets/save3.png").convert_alpha()
pause = pygame.image.load("assets/pause.png").convert_alpha()



#button instances
music_button = button.Button(320, 250, music_img, 0.5)
back_button = button.Button(320, 450, back_img, 0.5)
back_button2 = button.Button(320, 350, back_img, 0.5)
back_button3 = button.Button(680, 0, back_img, 0.35)
start_button = button.Button(320, 275, start_img, 0.5)
title_button = button.Button(280, 30, title_img, 0.5)
quit_button = button.Button(320, 475, quit_img, 0.5)
options_button = button.Button(320, 375, options_img, 0.5)

pause_button = button.Button(680, 0, pause, 0.5)

resume_button = button.Button(320, 275, resume_img, 0.5)

savefile_button1 = button.Button(120, 375, save_1, 0.5)
savefile_button2 = button.Button(320, 375, save_2, 0.5)
savefile_button3 = button.Button(520, 375, save_3, 0.5)



#levels
lec1_button = button.Button(100, 170, lec_1, 0.25)
sum1_button = button.Button(230, 170, sum_1, 0.25)
lec2_button = button.Button(360, 170, lec_2, 0.25)
sum2_button = button.Button(490, 170, sum_2, 0.25)
exam1_button = button.Button(620, 170, exam_1, 0.25)

#game bgs
bg = pygame.image.load("assets/bg.png").convert()
bg2 = pygame.image.load("assets/bg2.jpg").convert()
bg3 = pygame.image.load("assets/past.jpg").convert()
bg4 = pygame.image.load("assets/LVLbg.png").convert()
gameBg = pygame.image.load("assets/gameBG.jpg").convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()

game_background = pygame.transform.scale(gameBg, (WIDTH, HEIGHT))
game_background2 = pygame.transform.scale(bg3, (WIDTH / 0.5, HEIGHT / 0.5))
lvl_background = pygame.transform.scale(bg4, (WIDTH, HEIGHT))
