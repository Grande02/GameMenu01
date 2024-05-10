import json, os, pygame, sys
import elements, initiate
from elements import SCREEN

pygame.init()

#game set up
pygame.display.set_caption('SCIENCE')
font = pygame.font.SysFont("arial black", 40)
TEXT_COL = (255, 255, 255)

savename = None

#game condition checker/lvl unlocker/SAVE
data = {
    'lvl_checker': 0
}

with open('load_info') as load_file:
    data = json.load(load_file)


#with open('load_info', 'w') as load_file:
#      json.dump(data, load_file)

# Save function
def save_game(data, save_name):
    with open(f"{save_name}.json", "w") as load_file:
        json.dump(data, load_file)


# Load function
def load_game(save_name):
    save_file = f"{save_name}.json"
    if os.path.exists(save_file):
        with open(save_file, "r") as load_file:
            data = json.load(load_file)
        return data
    else:
        print(f"Save file '{save_name}' not found.")
        return None


#background for the main game
def bgGame():
    SCREEN.blit(initiate.game_background, (0, 0))


#def bgGame2():
# SCREEN.blit(game_background2, (225, 200))


def event_handler():
    for event in pygame.event.get():
        from pygame import QUIT
        if event.type == QUIT:
            with open('load_info', 'w') as load_file:
                json.dump(data, load_file)
            pygame.quit()
            sys.exit()

    pygame.display.update()


def BgLvl():
    SCREEN.blit(initiate.lvl_background, (0, 0))


def lecture1():
    running = True
    while running:

        BgLvl()
        elements.draw_text("LECTURE I BUTANGANAN", font, TEXT_COL, 150, 75)

        initiate.resume_button.draw(SCREEN)
        if initiate.resume_button.clicker(SCREEN):
            print("Lecture I Complete")

            data['lvl_checker'] += 1
            print("Lvl_checker value: ", data['lvl_checker'])

        initiate.back_button3.draw(SCREEN)
        if initiate.back_button3.clicker(SCREEN):
            running = False
        event_handler()


def lecture2():
    running = True
    while running:
        BgLvl()
        elements.draw_text("LECTURE II BUTANGANAN", font, TEXT_COL, 150, 75)

        initiate.resume_button.draw(SCREEN)
        if initiate.resume_button.clicker(SCREEN):
            print("Lecture II Complete")

            data['lvl_checker'] += 1

        initiate.back_button3.draw(SCREEN)
        if initiate.back_button3.clicker(SCREEN):
            running = False
        event_handler()


def summative1():
    running = True
    while running:
        BgLvl()
        elements.draw_text("SUMMATIVE I BUTANGANAN", font, TEXT_COL, 150, 75)

        initiate.resume_button.draw(SCREEN)
        if initiate.resume_button.clicker(SCREEN):
            print("SUMMATIVE I Complete")

            data['lvl_checker'] += 1
            print("level Checker:", data['lvl_checker'])

        initiate.back_button3.draw(SCREEN)
        if initiate.back_button3.clicker(SCREEN):
            running = False
        event_handler()


def summative2():
    running = True
    while running:
        BgLvl()
        elements.draw_text("SUMMATIVE II BUTANGANAN", font, TEXT_COL, 150, 75)
        initiate.resume_button.draw(SCREEN)
        if initiate.resume_button.clicker(SCREEN):
            print("SUMMATIVE II Complete")

            data['lvl_checker'] += 1
        initiate.back_button3.draw(SCREEN)
        if initiate.back_button3.clicker(SCREEN):
            running = False
        event_handler()


def exam1():
    running = True
    while running:
        BgLvl()
        elements.draw_text("EXAM BUTANGANAN", font, TEXT_COL, 150, 75)
        initiate.resume_button.draw(SCREEN)
        if initiate.resume_button.clicker(SCREEN):
            print("EXAM I Complete")

            data['lvl_checker'] += 1
        initiate.back_button3.draw(SCREEN)
        if initiate.back_button3.clicker(SCREEN):
            running = False
        event_handler()


def lectures():
    global savename
    running = True
    while running:
        bgGame()
        initiate.lec1_button.draw(SCREEN)
        initiate.back_button3.draw(SCREEN)

        # LVL UNLOCKER CONDITION
        if initiate.lec1_button.clicker(SCREEN):
            lecture1()
        else:
            pass

        if data['lvl_checker'] >= 1:
            initiate.sum1_button.draw(SCREEN)
            if initiate.sum1_button.clicker(SCREEN):
                summative1()
            else:
                pass
        else:
            pass
        if data['lvl_checker'] >= 2:
            initiate.lec2_button.draw(SCREEN)
            if initiate.lec2_button.clicker(SCREEN):
                lecture2()
            else:
                pass
        else:
            pass
        if data['lvl_checker'] >= 3:
            initiate.sum2_button.draw(SCREEN)
            if initiate.sum2_button.clicker(SCREEN):
                summative2()
            else:
                pass
        else:
            pass
        if data['lvl_checker'] >= 4:
            initiate.exam1_button.draw(SCREEN)
            if initiate.exam1_button.clicker(SCREEN):
                exam1()
            else:
                pass
        else:
            pass

        if data['lvl_checker'] >= 5:
            elements.draw_text("FINISH!", font, TEXT_COL, 320, 375)
        else:
            pass

        if initiate.back_button3.clicker(SCREEN):
            save_game(data, savename)
            running = False
        else:
            pass

        event_handler()


def Music():
    running = True
    while running:
        elements.bgRoll()

        elements.draw_text("MUSIC", font, TEXT_COL, 335, 250)
        initiate.back_button3.draw(SCREEN)
        if initiate.back_button3.clicker(SCREEN):
            running = False


def Option():
    running = True
    while running:
        elements.bgRoll()

        elements.draw_text("Option", font, TEXT_COL, 335, 75)
        if initiate.music_button.draw(SCREEN):
            Music()
        initiate.back_button3.draw(SCREEN)
        if initiate.back_button3.clicker(SCREEN):
            running = False

        event_handler()


def Start_Game():
    running = True
    while running:

        elements.bgRoll()
        initiate.title_button.draw(SCREEN)

        initiate.savefile_button1.draw(SCREEN)
        initiate.savefile_button2.draw(SCREEN)
        initiate.savefile_button3.draw(SCREEN)
        initiate.back_button3.draw(SCREEN)

        if initiate.savefile_button1.clicker(SCREEN):
           # savename = 'save1'
           # load_game('save1')
            lectures()
        elif initiate.savefile_button2.clicker(SCREEN):
           #  savename = 'save2'
           #  load_game('save2')
            lectures()
        elif initiate.savefile_button3.clicker(SCREEN):
           #  savename = 'save3'
           # load_game('save3')
            lectures()
        elif initiate.back_button3.clicker(SCREEN):
            running = False
        else:
            pass
        event_handler()


def Main_Menu():
    #running state
    running = True
    while running:
        elements.bgRoll()
        initiate.title_button.draw(SCREEN)

        initiate.start_button.draw(SCREEN)
        initiate.options_button.draw(SCREEN)
        initiate.quit_button.draw(SCREEN)

        if initiate.start_button.clicker(SCREEN):
            print("Lvl_checker value: ", data['lvl_checker'])
            Start_Game()
        else:
            pass

        if initiate.options_button.clicker(SCREEN):
            Option()
        else:
            pass

        if initiate.quit_button.clicker(SCREEN):
            running = False
        else:
            pass
        event_handler()


#Where the program starts
Main_Menu()
