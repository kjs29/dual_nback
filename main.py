import sys
import datetime
import time
import secrets
import json
import pygame
import os
from buttons import Buttons

# initialize pygame module
pygame.init()

# screen
screenwidth = 1000
screenheight = 1000
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("N-Back Expert")

icon = pygame.image.load("img/logo.png")
pygame.display.set_icon(icon)

# FPS
fps_clock = pygame.time.Clock()
fps = 60

# color
color = {"black" : (0, 0, 0), "white" : (255, 255, 255), "green" : (0, 255, 0),
         "grey" : (175, 173, 169), "red" : (255, 0, 0), "light green" : (144, 238, 144),
         "sky blue" : (50, 130, 230), "light red" : (255, 127, 127), 
         "blue" : (0, 0, 255), "purple" : (201, 71, 245), "dark grey" : (120, 120, 120),
         "yellow" : (255, 255, 0), "dark green" : (9, 148, 65), "dark dark grey" : (35, 35, 35),
         "pastel green" : (193, 225, 193), "orange" : (255, 165, 0), "light grey" : (188, 188, 188),
         "not too bright white" : (235, 235, 235), "brown" : (101, 67, 33)
        }

# font
font18 = pygame.font.Font("font/gameplay.ttf", 18)
font37 = pygame.font.Font("font/fragmentcore.otf", 37)
font70 = pygame.font.Font("font/cleanfont.ttf", 70)
font60_clean = pygame.font.Font("font/fragmentcore.otf", 60)
font_banknumbers = pygame.font.Font("font/F25_bank_Printer.otf",50)
font70_clean = pygame.font.Font("font/fragmentcore.otf", 70)
font100 = pygame.font.Font("font/cleanfont.ttf", 100)
font150_number = pygame.font.Font("font/fragmentcore.otf", 150)

# game control
"""
main menu: 0, game screen: 1, scorescreen(afterthegameplay): 2, settings: 3, scoreboard : 4, howtoplay : 5
"""
game = 0


def multiline_text(screen,size,text,color,coor,linespace = 10, fontname = "font/sketched.ttf"):
    
    text_list = text.splitlines()
    for i,e in enumerate(text_list):
        font = pygame.font.Font(fontname, size)
        message_content = font.render(e, True, color)
        message_content_rect = message_content.get_rect()
        message_content_rect.center = coor[0], coor[1] + size * i + (i * linespace)
        screen.blit(message_content,message_content_rect)

def show_text(screen, text, coor, color, size, fontname, centered_position = True):
    if centered_position == True:
        font = pygame.font.Font(fontname, size)
        content = font.render(text, True, color)
        content_rect = content.get_rect()
        content_rect.center = coor[0],coor[1]
        screen.blit(content,content_rect)
    else:
        font = pygame.font.Font(fontname, size)
        content = font.render(text, True, color)
        content_rect = content.get_rect()
        content_rect.x, content_rect.y = coor[0], coor[1]
        screen.blit(content,content_rect)

clickedflag = False
def clicked(rect):
    
    global clickedflag
    if rect.collidepoint(pygame.mouse.get_pos()):
        if clickedflag == False and pygame.mouse.get_pressed()[0]:
            clickedflag = True
            return True
        elif clickedflag == True and pygame.mouse.get_pressed()[0] == False:
            clickedflag = False

def hovered(rect):
    if rect.collidepoint(pygame.mouse.get_pos()):
        return True
    return False

def reposition_imgs():
    global imgs3_rect, imgs2_rect, imgs1_rect
    imgs3_rect = {}
    imgs2_rect = {}
    imgs1_rect = {}
    for n in range(9, 0, -1):
        if n == 9:
            imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (30 + 150, 30 + 150))
            imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (30 + 150, 30 + 150))
            imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (30 + 150, 30 + 150))
        elif n == 8:
            imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (350 + 150, 30 + 150))
            imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (350 + 150, 30 + 150))
            imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (350 + 150, 30 + 150))
        elif n == 7:
            imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (670 + 150, 30 + 150))
            imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (670 + 150, 30 + 150))
            imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (670 + 150, 30 + 150))
        elif n == 6:
            imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (30 + 150, 350 + 150))
            imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (30 + 150, 350 + 150))
            imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (30 + 150, 350 + 150))
        elif n == 5:
            imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (350 + 150, 350 + 150))
            imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (350 + 150, 350 + 150))
            imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (350 + 150, 350 + 150))
        elif n == 4:
            imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (670 + 150, 350 + 150))
            imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (670 + 150, 350 + 150))
            imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (670 + 150, 350 + 150))
        elif n == 3:
            imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (30 + 150, 670 + 150))
            imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (30 + 150, 670 + 150))
            imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (30 + 150, 670 + 150))
        elif n == 2:
            imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (350 + 150, 670 + 150))
            imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (350 + 150, 670 + 150))
            imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (350 + 150, 670 + 150))
        elif n == 1:
            imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (670 + 150, 670 + 150))
            imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (670 + 150, 670 + 150))
            imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (670 + 150, 670 + 150))
            
def regenerate_sequence():
    """Regenerate new sequence of questions"""
    global  questions_location, questions_numbers, questions_numbers_rendered_content_lst, questions_number_rect_lst, answer_location, answer_numbers, user_answer_location, user_answer_numbers, choices_numbers, choices_positions, level_flag
    randomNumbers = secrets.SystemRandom()
    questions_location = []
    questions_numbers = []
    questions_numbers_rendered_content_lst = []
    questions_number_rect_lst = []

    for i in range(the_number_of_questions):
        questions_numbers.append(randomNumbers.randint(1, choices_numbers))
        questions_location.append(randomNumbers.randint(1, choices_positions))
        each_content_1 = font150_number.render(str(questions_numbers[i]), True, color["green"])
        each_rect_1 = each_content_1.get_rect(center = (-200, -200))
        questions_numbers_rendered_content_lst.append(each_content_1)
        questions_number_rect_lst.append(each_rect_1)

    answer_location = []
    answer_numbers = []

    for i in range(len(questions_location)):
        if i >= current_nback:
            if questions_location[i] == questions_location[i - current_nback]:
                answer_location.append("O")
            else:
                answer_location.append("X")
            if questions_numbers[i] == questions_numbers[i - current_nback]:
                answer_numbers.append("O")
            else:
                answer_numbers.append("X")

    user_answer_location = [" " for _ in range(len(answer_location))]
    user_answer_numbers = [" " for _ in range(len(answer_numbers))]

    level_flag = False


def play_sound(filename = None, volume = 1, loop = False, channel = -1):

    if channel == -1:

        sound = pygame.mixer.Sound(filename)
        if volume != 1:
            sound.set_volume(volume)
        if loop:
            sound.play(-1)
        else:
            sound.play()
            

# tiles

first = []
second = []
third = []

for n in range(3):
    first.append(pygame.Rect((30 + n * 300 + n * 20, 30, 300, 300)))
    second.append(pygame.Rect((30 + n * 300 + n * 20, 350, 300, 300)))
    third.append(pygame.Rect((30 + n * 300 + n * 20, 670, 300, 300)))

tile_location = first + second + third

number_location = [[180, 180], [500, 180], [820, 180], [180, 500], [500, 500], [820, 500], [180, 820], [500, 820], [820, 820]]

# Time flag
start_count = time.time()
new_start_count = pygame.time.get_ticks()
questions_start = False
game_start_flag = False
one_tenth_seconds = 0

# game screen start
start_count_game_screen = False

button1 = Buttons(30 + 150, 30 + 150, 300, 300, color["black"], alpha = 255)
button2 = Buttons(350 + 150, 30 + 150, 300, 300, color["black"], alpha = 255)
button3 = Buttons(670 + 150, 30 + 150, 300, 300, color["black"], alpha = 255)
button4 = Buttons(30 + 150, 350 + 150, 300, 300, color["black"], alpha = 255)
button5 = Buttons(350 + 150, 350 + 150, 300, 300, color["black"], alpha = 255)
button6 = Buttons(670 + 150, 350 + 150, 300, 300, color["black"], alpha = 255)
button7 = Buttons(30 + 150, 670 + 150, 300, 300, color["black"], alpha = 255)
button8 = Buttons(350 + 150, 670 + 150, 300, 300, color["black"], alpha = 255)
button9 = Buttons(670 + 150, 670 + 150, 300, 300, color["black"], alpha = 255)
buttonlist = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

# scale original image size to 300,300
imgs3 = {}
imgs2 = {}
imgs1 = {}
for n in range(9, 0, -1):
    imgs3[f"img{n}"] = pygame.image.load(f"img/3/{n}.png")
    imgs3[f"img{n}"] = pygame.transform.scale(imgs3[f"img{n}"], (300, 300))
    imgs2[f"img{n}"] = pygame.image.load(f"img/2/{n}.png")
    imgs2[f"img{n}"] = pygame.transform.scale(imgs2[f"img{n}"], (300, 300))
    imgs1[f"img{n}"] = pygame.image.load(f"img/1/{n}.png")
    imgs1[f"img{n}"] = pygame.transform.scale(imgs1[f"img{n}"], (300, 300))


imgs3_rect = {}
imgs2_rect = {}
imgs1_rect = {}
for n in range(9, 0, -1):
    if n == 9:
        imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (30 + 150, 30 + 150))
        imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (30 + 150, 30 + 150))
        imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (30 + 150, 30 + 150))
    elif n == 8:
        imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (350 + 150, 30 + 150))
        imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (350 + 150, 30 + 150))
        imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (350 + 150, 30 + 150))
    elif n == 7:
        imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (670 + 150, 30 + 150))
        imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (670 + 150, 30 + 150))
        imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (670 + 150, 30 + 150))

    elif n == 6:
        imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (30 + 150, 350 + 150))
        imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (30 + 150, 350 + 150))
        imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (30 + 150, 350 + 150))

    elif n == 5:
        imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (350 + 150, 350 + 150))
        imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (350 + 150, 350 + 150))
        imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (350 + 150, 350 + 150))

    elif n == 4:
        imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (670 + 150, 350 + 150))
        imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (670 + 150, 350 + 150))
        imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (670 + 150, 350 + 150))

    elif n == 3:
        imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (30 + 150, 670 + 150))
        imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (30 + 150, 670 + 150))
        imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (30 + 150, 670 + 150))

    elif n == 2:
        imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (350 + 150, 670 + 150))
        imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (350 + 150, 670 + 150))
        imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (350 + 150, 670 + 150))

    elif n == 1:
        imgs3_rect[f"img{n}_rect"] = imgs3[f"img{n}"].get_rect(center = (670 + 150, 670 + 150))
        imgs2_rect[f"img{n}_rect"] = imgs2[f"img{n}"].get_rect(center = (670 + 150, 670 + 150))
        imgs1_rect[f"img{n}_rect"] = imgs1[f"img{n}"].get_rect(center = (670 + 150, 670 + 150))


# text

# main menu screen
main_menu_flag = False
sound_main_menu_intro_flag = False
texts_mainmenu = ["Dual\nN back", "How\nto\nplay", "Exit", "Game\nsettings", "Score\nboard" ]

# game screen
texts_in_game = {"Start!":[screenwidth / 2, 500],                 
                }
lst_texts_in_game = list(texts_in_game)
current_nback = 1
choices_positions = 9
choices_numbers = 9
the_number_of_questions = 10
the_duration_between_each_number = 5
counter = 0

# Game screen
button_position = pygame.image.load("img/tile.png")
#$%^
button_position_rect = button_position.get_rect(center = (1145  , 745))
button_numbers = pygame.image.load("img/verification.png")
#$%^
button_numbers_rect = button_numbers.get_rect(center = (1140, 100))
text_current_nback = font37.render(f"{current_nback} back", True, color["white"])
#$%^
text_current_nback_rect = text_current_nback.get_rect(center = (1200 , 400))
text_progress = font37.render(str(counter + 1)+" / " + str(the_number_of_questions), True, color["white"])
#$%^
text_progress_rect = text_progress.get_rect(center = (1200, 400))
text_position = font18.render("Position", True, color["white"])
text_numbers = font18.render("Number", True, color["white"])
#$%^
text_numbers_rect = text_numbers.get_rect(center = (1140, 150))
#$%^
text_position_rect = text_position.get_rect(center = (1140, 800))




text_pause = font18.render("Pause", True, color["white"])
text_pause_rect = text_pause.get_rect(center = (screenwidth+140-65, 610))
text_stop = font18.render("Stop", True, color["white"])
text_stop_rect = text_stop.get_rect(center = (screenwidth+140+60, 610))
stop_flag = False

button_position_O = pygame.image.load("img/o.png")
button_position_O_rect = button_position_O.get_rect(center = (-200, -200))
button_position_X = pygame.image.load("img/x.png")
button_position_X_rect = button_position_X.get_rect(center = (-200, -200))

button_numbers_O = pygame.image.load("img/o1.png")
button_numbers_O_rect = button_numbers_O.get_rect(center = (-200, -200))
button_numbers_X = pygame.image.load("img/x1.png")
button_numbers_X_rect = button_numbers_X.get_rect(center = (-200, -200))

button_key1 = pygame.image.load("img/one.png")
button_key2 = pygame.image.load("img/two.png")
button_key3 = pygame.image.load("img/three.png")
button_key4 = pygame.image.load("img/four.png")
button_key1_rect = button_key1.get_rect(center = (-200, -200))
button_key2_rect = button_key2.get_rect(center = (-200, -200))
button_key3_rect = button_key3.get_rect(center = (-200, -200))
button_key4_rect = button_key4.get_rect(center = (-200, -200))


sound_countdown_flag = False
sound_number_appear_flag = False
sound_countdown_3 = False
sound_countdown_2 = False
sound_countdown_1 = False
sound_start_flag = False

game_pause_flag = False
texts_pause_screen = [
                        "Paused",
                        "Resume",
                        "Main menu",
                        "Press P to resume",
                        "Press M to return to the Main menu"
                     ]

# How to play screen
texts_how_to_play = [
                        "How to play",
                        "N back is a game\nwhere you remember the number n-th event ago.\n\nFor example,\nif the sequence is   ,  ,  ,  ,  \nthe current event number is 3,\nbecause it's the most recent number.\n1 back number would be 2,\n2 back number would be 4,\n3 back number would be 8, and so on.\nLet's say that you are playing 1 back,\nevery time a new number occurs, you check if\nthe current event number is the same number as\n1 back event number.\nIf the numbers are the same click O, if they're not click X.\n\nSimilarly, the sequence will also include the positions of tiles.\nWe will walk you through how to play the game in the tutorial.",
                        "Main menu",
                        "(press 'm')"
                    ]
description_flag = True
tutorial_flag = False
arrow_tutorial = pygame.image.load("img/gototutorial.png")
texts_tutorials = ["\n\n"," "]
texts_tutorials_coordinates = [[-200,-200],[-200,-200]]
tutorial_time_flag = False
tutorial_current_time = time.time()
tutorial_start_time = time.time()
img_o_numbers = pygame.image.load("img/o.png")
img_x_numbers = pygame.image.load("img/x.png")
img_o_positions = pygame.image.load("img/o1.png")
img_x_positions = pygame.image.load("img/x1.png")
img_o_numbers_rect = img_o_numbers.get_rect(center=(567-50,690))
img_x_numbers_rect = img_x_numbers.get_rect(center=(567+50,690))
img_o_positions_rect = img_o_positions.get_rect(center = (813-50,690))
img_x_positions_rect = img_x_positions.get_rect(center = (813+50,690))
tutorial_answer= [" "," "]


# Score screen
score_flag = False
button_save_result_flag = False
correct_number_of_questions_location = 0
correct_number_of_questions_numbers = 0
score_for_numbers = 0
score_for_numbers = 0
practice_the_same_sequence_flag = False
texts_score = [
                "Result",
                0,
                0,
                "Numbers",
                "Positions",
                "Save result as text",
                "Practice the same sequence",
                "New game",
                "Main menu"
              ]
button_play_with_the_same_sequence = Buttons(screenwidth / 2, 700, 480, 64, alpha = 255)
button_save_result = Buttons(screenwidth / 2, 770, 480, 64, alpha = 255)
button_new_game = Buttons(screenwidth / 2, 840, 480, 64, alpha = 255)
button_main_menu = Buttons(screenwidth / 2, 910, 480, 64, alpha = 255)
text_score_helper = f"Increase the number of events to {current_nback * 3}\nto earn a '{current_nback} back' point!"

# Game settings screen
texts_game_settings = [
                        "Game settings","# N", "Choices <numbers>",
                        "Choices <positions>", "# of events",
                        "Time intervals(s)", "Main menu", "(Press 'm')",
                        "(1 ~ 9, default : 1)","(2 ~ 9, default : 9)",
                        "(2 ~ 9, default : 9)", "(Current N + 1 ~ 99, default : 10)",
                        "(2 ~ 99, default : 5)"
                      ]
user_nback = str(current_nback)
user_choices_numbers = str(choices_numbers)
user_choices_positions = str(choices_positions)
user_number_of_questions = str(the_number_of_questions)
user_the_duration_between_each_number = str(the_duration_between_each_number)
user_input_n_rect = pygame.Rect(775, 198, 80, 70)
user_input_choices_numbers_rect = pygame.Rect(775, 350 - 32, 80, 70)
user_input_choices_positions_rect = pygame.Rect(775, 470 - 32, 80, 70)
user_input_number_of_questions_rect = pygame.Rect(775, 590 - 32, 80, 70)
user_input_time_intervals_rect = pygame.Rect(775, 710 - 32, 80, 70)
game_settings_main_menu_rect = pygame.Rect(340, 850, 320, 100)
user_input_n_flag = False
user_input_choices_numbers_flag = False
user_input_choices_positions_flag = False
user_input_number_of_questions_flag = False
user_input_time_intervals_flag = False
user_main_menu_flag = False
mouse_cursor = pygame.draw.line(screen, color["white"], (837, 208), (837, 258))
mouse_cursor_time_flag = 0
mouse_cursor_time = time.time()



# level system

level_flag = False
current_level = 0
level_correct_number_of_numbers = 0
level_correct_number_of_positions = 0
n1_exp = 0
n2_exp = 0
n3_exp = 0
n4_exp = 0
n5_exp = 0
n6_exp = 0
n7_exp = 0
n8_exp = 0
n9_exp = 0

level_system = {
                "tries" : 0,
                "n1_exp" : n1_exp,
                "n2_exp" : n2_exp,
                "n3_exp" : n3_exp,
                "n4_exp" : n4_exp,
                "n5_exp" : n5_exp,
                "n6_exp" : n6_exp,
                "n7_exp" : n7_exp,
                "n8_exp" : n8_exp,
                "n9_exp" : n9_exp,
              }

# if level file exists, open, and save it as level_system.
if os.path.isfile("level.txt"):
    with open("level.txt") as levelfile:
        level_system = json.load(levelfile)

# Score board
texts_scoreboard = ["Your Rank\nis"]

run = True
while run:
 
    # main menu screen
    if game == 0:
        screen.fill(color["black"])
        mouse_point = pygame.mouse.get_pos()
        current_count = time.time()
        if main_menu_flag == False:
            if current_count - start_count > 0.5:
                if sound_main_menu_intro_flag == False:
                    sound_main_menu_intro_flag = True
                    play_sound("sound/rome.mp3",volume = 0.3)
            if 1 < current_count - start_count < 1.3:
                pygame.draw.rect(screen, color["red"], first[0], border_radius = 5)
            if 1.2 < current_count - start_count < 1.5:
                pygame.draw.rect(screen, color["orange"], first[1], border_radius = 5)
            if 1.4 < current_count - start_count < 1.7:
                pygame.draw.rect(screen, color["yellow"], first[2], border_radius = 5)
            if 1.6 < current_count - start_count < 1.9:
                pygame.draw.rect(screen, color["green"], second[0], border_radius = 5)
            if 1.8 < current_count - start_count < 2.1:
                pygame.draw.rect(screen, color["light green"], second[1], border_radius = 5)        
            if 2 < current_count - start_count < 2.3:
                pygame.draw.rect(screen, color["sky blue"], second[2], border_radius = 5)
            if 2.2 < current_count - start_count < 2.5:
                pygame.draw.rect(screen, color["blue"], third[0], border_radius = 5)
            if 2.4 < current_count - start_count < 2.7:
                pygame.draw.rect(screen, color["brown"], third[1], border_radius = 5)        
            if 2.6 < current_count - start_count < 2.9:
                pygame.draw.rect(screen, color["dark dark grey"], third[2], border_radius = 5)
            if 3 < current_count - start_count < 3.2:
                for n in range(3):
                    pygame.draw.rect(screen, color["white"], first[n], border_radius = 5)
                    pygame.draw.rect(screen, color["white"], third[n], border_radius = 5)
                pygame.draw.rect(screen, color["white"], second[0], border_radius = 5)
                pygame.draw.rect(screen, color["white"], second[2], border_radius = 5)
                multiline_text(screen, 74, texts_mainmenu[0], color["white"], (350 + 150, 350 + 100), 10,"font/sketched.ttf")
            if 0 < current_count - start_count < 2.9:
                show_text(screen, "Press enter to skip", (screenwidth / 2, screenheight / 2),color["white"], 25, "font/cleanfont.ttf")
                if clicked(button5.surface_rect):
                    main_menu_flag = True

        if current_count - start_count >= 3.2 or main_menu_flag == True:
            for i in range(len(tile_location)):
                if tile_location[i].collidepoint(mouse_point):
                    pygame.draw.rect(screen, color["green"], tile_location[i], width = 10, border_radius = 10)
                else:
                    pygame.draw.rect(screen, color["white"], tile_location[i], width = 3, border_radius = 5)
            
            if clicked(button1.surface_rect):
                play_sound("sound/click1.wav")
                game = 5

            if clicked(button3.surface_rect):
                play_sound("sound/click1.wav")
                game = 4

            if clicked(button5.surface_rect):
                game = 1
                screenwidth = 1300
                screen = pygame.display.set_mode((screenwidth, screenheight))
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                play_sound("sound/playbutton.wav")
                regenerate_sequence()

            if clicked(button7.surface_rect):
                play_sound("sound/click1.wav")
                game = 3

            if clicked(button9.surface_rect):
                run = False

            show_text(screen, "1", (305, 55), color["light grey"], 20, "font/F25_bank_Printer.otf")
            show_text(screen, "2", (625, 55), color["light grey"], 20, "font/F25_bank_Printer.otf")
            show_text(screen, "3", (945, 55), color["light grey"], 20, "font/F25_bank_Printer.otf")
            show_text(screen, "4", (305, 375), color["light grey"], 20, "font/F25_bank_Printer.otf")
            show_text(screen, "5", (625, 375), color["light grey"], 20, "font/F25_bank_Printer.otf")
            show_text(screen, "6", (945, 375), color["light grey"], 20, "font/F25_bank_Printer.otf")
            show_text(screen, "7", (305, 695), color["light grey"], 20, "font/F25_bank_Printer.otf")
            show_text(screen, "8", (625, 695), color["light grey"], 20, "font/F25_bank_Printer.otf")
            show_text(screen, "9", (945, 695), color["light grey"], 20, "font/F25_bank_Printer.otf")
            if tile_location[4].collidepoint(mouse_point) == False:
                texts_mainmenu[0] = "Dual\nN back"
                multiline_text(screen, 74, texts_mainmenu[0], color["white"], (350 + 150, 350 + 100), 10, "font/sketched.ttf")
            else:
                texts_mainmenu[0] = "Play"
                show_text(screen, texts_mainmenu[0],(350 + 150, 350 + 150, 300), color["white"], 74, "font/sketched.ttf")
            multiline_text(screen, 70, texts_mainmenu[1], color["yellow"], (30 + 150, 20 + 80), 1)
            multiline_text(screen, 65, texts_mainmenu[3], color["green"], (30 + 150, 670 + 110), 1)
            multiline_text(screen, 70, texts_mainmenu[4], color["sky blue"], (670 + 150, 140))
            show_text(screen, texts_mainmenu[2], (670 + 150, 670 + 150), color["red"], 90, "font/sketched.ttf")

    # game screen
    elif game == 1:
        screen.fill(color["black"])

        # Count down 3 2 1
        if questions_start == False:
            current_count = time.time()
            
            if start_count_game_screen == False:
                start_count_game_screen = True
                start_count = time.time()

            if 0.5 < current_count - start_count < 1.5:
                for n in range(9, 0, -1):
                    screen.blit(imgs3[f"img{n}"], imgs3_rect[f"img{n}_rect"])
                if sound_countdown_flag == False:
                    sound_countdown_flag = True
                    play_sound("sound/countdown.wav")
            if 1.5 < current_count - start_count < 2.5:
                sound_countdown_flag = False
                for n in range(9, 0, -1):
                    screen.blit(imgs2[f"img{n}"], imgs2_rect[f"img{n}_rect"])
            if 2.5 < current_count - start_count < 3.5:
                for n in range(9, 0, -1):
                    screen.blit(imgs1[f"img{n}"], imgs1_rect[f"img{n}_rect"])
            if 3.5 < current_count - start_count:
                if sound_start_flag == False:
                    sound_start_flag = True
                    play_sound("sound/countdown_start.wav",volume = 0.5)
                for n in range(9, 0, -1):
                    imgs1_rect[f"img{n}_rect"].center = - 200, -200
                    imgs2_rect[f"img{n}_rect"].center = - 200, -200
                    imgs3_rect[f"img{n}_rect"].center = - 200, -200
                show_text(screen, lst_texts_in_game[0], texts_in_game["Start!"], color["white"], 90,"font/sketched.ttf")
                for i in range(len(tile_location)):
                    pygame.draw.rect(screen, color["white"], tile_location[i], width = 3, border_radius = 5)
            
            if 5 < current_count - start_count :
                lst_texts_in_game[0] = " "
                start_count = 0
                questions_start = True
        
        # After count down : Game begins
        else:

            # Paused
            if game_pause_flag == True:
                screen.fill(color["black"])
                
                show_text(screen, texts_pause_screen[0], (screenwidth / 2, 400), color["white"], 70, "font/sketched.ttf")
                show_text(screen,texts_pause_screen[1], (screenwidth / 2, 550), color["white"], 50, "font/sketched.ttf")
                show_text(screen, texts_pause_screen[2], (screenwidth / 2, 700), color["white"], 50, "font/sketched.ttf")
                if hovered(pygame.Rect(375+150, 500, 250, 100)):
                    pygame.draw.rect(screen, color["white"], (375+150, 500, 250, 100), width = 3, border_radius = 2)
                    show_text(screen, texts_pause_screen[3], (screenwidth / 2, 620), color["white"], 30,"font/cleanfont.ttf")
                if clicked(pygame.Rect(375+150, 500, 250, 100)):
                    game_pause_flag = False
                if hovered(pygame.Rect(330+150, 655, 340, 100)):
                    pygame.draw.rect(screen, color["white"], (330+150, 655, 340, 100), width = 3, border_radius = 2)
                    show_text(screen, texts_pause_screen[4], (screenwidth / 2, 775), color["white"], 30, "font/cleanfont.ttf")
                if clicked(pygame.Rect(330+150, 655, 340, 100)):
                    screenwidth = 1000
                    screen = pygame.display.set_mode((screenwidth, screenheight))
                    questions_start = False
                    start_count_game_screen = False
                    one_tenth_seconds = 0
                    game_pause_flag = False
                    counter = 0
                    questions_start = False
                    score_flag = False
                    button_save_result_flag = False
                    start_count_game_screen = False
                    correct_number_of_questions_location = 0
                    correct_number_of_questions_numbers = 0
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    reposition_imgs()
                    lst_texts_in_game[0] = "Start!"
                    button_position_O_rect.center = -200, -200
                    button_position_X_rect.center = -200, -200
                    button_numbers_O_rect.center = -200, -200
                    button_numbers_X_rect.center = -200, -200
                    button_key1_rect.center = -200, -200
                    button_key2_rect.center = -200, -200
                    button_key3_rect.center = -200, -200
                    button_key4_rect.center = -200, -200
                    main_menu_flag = True
                    game = 0

            # Not paused
            elif game_pause_flag == False:

                # Reflect json file on level_system
                if os.path.isfile("level.txt"):
                    with open("level.txt") as file:
                        level_system = json.load(file)

                # level appearing
                # god
                if level_system["n9_exp"] >= 100:
                    pygame.draw.rect(screen, color["dark dark grey"], (1020, 525, 220, 35), border_radius= 2)
                    starimg = pygame.image.load("img/star.png")
                    starimg = pygame.transform.scale(starimg,(20, 20))
                    starimg_rect = starimg.get_rect(center = (1020+110, 540))
                    starimg_rect2 = starimg.get_rect(center = (1020+110-70, 540))
                    starimg_rect3 = starimg.get_rect(center = (1020+110+70, 540))
                    screen.blit(starimg, starimg_rect)
                    screen.blit(starimg, starimg_rect2)
                    screen.blit(starimg, starimg_rect3)
                # grand master
                elif level_system["n8_exp"] >= 100:
                    pygame.draw.rect(screen, color["dark dark grey"], (1020, 525, 220, 35), border_radius= 2)
                    starimg = pygame.image.load("img/star.png")
                    starimg = pygame.transform.scale(starimg, (20, 20))
                    starimg_rect = starimg.get_rect(center = (1020+110-30, 540))
                    starimg_rect2 = starimg.get_rect(center = (1020+110+30, 540))
                    screen.blit(starimg, starimg_rect)
                    screen.blit(starimg, starimg_rect2)
                # master
                elif level_system["n7_exp"] >= 100:
                    pygame.draw.rect(screen, color["dark dark grey"], (1020, 525, 220, 35), border_radius= 2)
                    starimg = pygame.image.load("img/star.png")
                    starimg = pygame.transform.scale(starimg, (20, 20))
                    starimg_rect = starimg.get_rect(center = (1020+110, 540))
                    screen.blit(starimg, starimg_rect)
                # black
                elif (100 <= level_system["tries"] and level_system["n6_exp"] >= 30) or level_system["n6_exp"] >= 60:
                    pygame.draw.rect(screen, color["dark dark grey"], (1200, 520, 35, 35), border_radius = 2)
                    # Level text appearing
                    show_text(screen, "Rank :", (1050, 540), color["white"], 20, "font/F25_bank_Printer.otf")
                # red
                elif (100 <= level_system["tries"] and level_system["n5_exp"] >= 25) or level_system["n5_exp"] >= 50:
                    pygame.draw.rect(screen, color["red"], (1200, 520, 35, 35), border_radius = 2)
                    # Level text appearing
                    show_text(screen, "Rank :", (1050, 540), color["white"], 20, "font/F25_bank_Printer.otf")
                # brown
                elif (80 <= level_system["tries"] and level_system["n4_exp"] >= 20) or level_system["n4_exp"] >= 40:
                    pygame.draw.rect(screen, color["brown"], (1200, 520, 35, 35), border_radius = 2)
                    # Level text appearing
                    show_text(screen, "Rank :", (1050, 540), color["white"], 20, "font/F25_bank_Printer.otf")
                # green
                elif (50 <= level_system["tries"] and level_system["n3_exp"] >= 15) or level_system["n3_exp"] >= 30:
                    pygame.draw.rect(screen, color["green"], (1200, 520, 35, 35), border_radius = 2)
                    # Level text appearing
                    show_text(screen, "Rank :", (1050, 540), color["white"], 20, "font/F25_bank_Printer.otf")
                # blue
                elif (50 <= level_system["tries"] and level_system["n2_exp"] >= 10) or level_system["n2_exp"] >= 20:
                    pygame.draw.rect(screen, color["sky blue"], (1200, 520, 35, 35), border_radius = 2)
                    # Level text appearing
                    show_text(screen, "Rank :", (1050, 540), color["white"], 20, "font/F25_bank_Printer.otf")
                # yellow
                elif (50 <= level_system["tries"] and level_system["n1_exp"] >= 5) or level_system["n1_exp"] >= 10:
                    pygame.draw.rect(screen, color["yellow"], (1200, 520, 35, 35), border_radius = 2)
                    # Level text appearing
                    show_text(screen, "Rank :", (1050, 540), color["white"], 20, "font/F25_bank_Printer.otf")
                # white
                elif 0 <= level_system["tries"] <= 49:
                    #$%^
                    pygame.draw.rect(screen, color["white"], (1200, 520, 35, 35), border_radius = 2)
                    # Level text appearing
                    #$%^
                    show_text(screen, "Rank :", (1050, 540), color["white"], 20, "font/F25_bank_Printer.otf")
                else:
                    #$%^
                    pygame.draw.rect(screen, color["white"], (1200, 520, 35, 35), border_radius = 2)
                    # Level text appearing
                    #$%^
                    show_text(screen, "Rank :", (1050, 540), color["white"], 20, "font/F25_bank_Printer.otf")

                # N back text appearing
                #$%^
                show_text(screen, f"{current_nback} back",(1050, 400), color["white"], 20, "font/F25_bank_Printer.otf")
                
                # Time left appearing
                #$%^
                show_text(screen,"Time left :", (1085, 465), color["white"], 20, "font/F25_bank_Printer.otf")

                # Progress text appearing
                text_progress = font37.render(f"{counter+1} / {the_number_of_questions}", True, color["white"])
                screen.blit(text_progress, text_progress_rect)
                screen.blit(button_position, button_position_rect)
                screen.blit(button_numbers, button_numbers_rect)
                button_position = pygame.transform.scale(button_position, (50, 50))
                screen.blit(text_position, text_position_rect)
                screen.blit(text_numbers, text_numbers_rect)
                screen.blit(text_pause, text_pause_rect)
                #$%^
                # show_text(screen, "(P)ause", (1050, 600), color["not too bright white"], 30, "font/cleanfont.ttf")
                # #$%^
                # show_text(screen, "(S)top", (1230, 600), color["not too bright white"], 30, "font/cleanfont.ttf")
                screen.blit(text_stop, text_stop_rect)
                screen.blit(button_position_O, button_position_O_rect)
                screen.blit(button_position_X, button_position_X_rect)
                screen.blit(button_numbers_O, button_numbers_O_rect)
                screen.blit(button_numbers_X, button_numbers_X_rect)
                screen.blit(button_key1, button_key1_rect)
                screen.blit(button_key2, button_key2_rect)
                screen.blit(button_key3, button_key3_rect)
                screen.blit(button_key4, button_key4_rect)
                
                # Tiles appearing
                for i in range(len(tile_location)):
                    pygame.draw.rect(screen, color["white"], tile_location[i], width = 3, border_radius = 5)

                # pause button clicked
                if clicked(pygame.Rect(1020, 585, 110, 50)):
                    sound_countdown_flag = False
                    sound_start_flag = False
                    game_pause_flag = True

                # stop button clicked -> main menu
                if clicked(pygame.Rect(1155, 585, 85, 50)):
                    screenwidth = 1000
                    screen = pygame.display.set_mode((screenwidth, screenheight))
                    # stop_flag is for the description in score screen
                    stop_flag = True
                    sound_countdown_flag = False
                    sound_start_flag = False
                    questions_number_rect_lst[counter].center = -200, -200
                    game = 2

                # mouse hover over effect on pause
                if hovered(pygame.Rect(1020, 585, 110, 50)):
                    pygame.draw.rect(screen, color["not too bright white"], (1020, 585, 110, 50), 3, 2)
                
                # mouse hover over effect on stop
                if hovered(pygame.Rect(1155, 585, 85, 50)):
                    pygame.draw.rect(screen, color["not too bright white"], (1155, 585, 85, 50), 3, 2)
                
                new_current_count = pygame.time.get_ticks()
                # every 0.1 second                
                if new_current_count - new_start_count > 100:
                    one_tenth_seconds += 0.1
                    one_tenth_seconds = round(one_tenth_seconds, 2)
                    rem = round(one_tenth_seconds % the_duration_between_each_number, 1)
                    new_start_count = new_current_count
                    counter = int(one_tenth_seconds // the_duration_between_each_number)

                # bliting numbers on the screen - all the time
                for i in range(the_number_of_questions):
                    screen.blit(questions_numbers_rendered_content_lst[i], questions_number_rect_lst[i])

                # positions appearing, disappearing - default x,y = -200, -200
                if 0 < rem <= the_duration_between_each_number - 0.1:
                    for i in range(9):
                        if questions_location[int(counter)] == i+1:
                            try:
                                with open("level.txt") as file:
                                    level_system = json.load(file)
                            except:
                                pass
                            
                            if os.path.isfile("level.txt"):
                                # god
                                if level_system["n9_exp"] >= 100:
                                    pygame.draw.rect(screen, color["dark dark grey"], tile_location[i], width = 18, border_radius = 5)   
                                # grand master
                                elif level_system["n8_exp"] >= 100:
                                    pygame.draw.rect(screen, color["dark dark grey"], tile_location[i], width = 18, border_radius = 5)
                                # master
                                elif level_system["n7_exp"] >= 100:
                                    pygame.draw.rect(screen, color["dark dark grey"], tile_location[i], width = 18, border_radius = 5)   
                                # black
                                elif (100 <= level_system["tries"] and level_system["n6_exp"] >= 30) or level_system["n6_exp"] >= 60:
                                    pygame.draw.rect(screen, color["dark dark grey"], tile_location[i], width = 18, border_radius = 5)   
                                # red
                                elif (100 <= level_system["tries"] and level_system["n5_exp"] >= 25) or level_system["n5_exp"] >= 50:
                                    pygame.draw.rect(screen, color["red"], tile_location[i], width = 18, border_radius = 5)  
                                # brown
                                elif (80 <= level_system["tries"] and level_system["n4_exp"] >= 20) or level_system["n4_exp"] >= 40:
                                    pygame.draw.rect(screen, color["brown"], tile_location[i], width = 18, border_radius = 5)  
                                # green
                                elif (50 <= level_system["tries"] and level_system["n3_exp"] >= 15) or level_system["n3_exp"] >= 30:
                                    pygame.draw.rect(screen, color["green"], tile_location[i], width = 18, border_radius = 5)  
                                # blue
                                elif (50 <= level_system["tries"] and level_system["n2_exp"] >= 10) or level_system["n2_exp"] >= 20:
                                    pygame.draw.rect(screen, color["sky blue"], tile_location[i], width = 18, border_radius = 5)  
                                # yellow
                                elif (50 <= level_system["tries"] and level_system["n1_exp"] >= 5) or level_system["n1_exp"] >= 10:
                                    pygame.draw.rect(screen, color["yellow"], tile_location[i], width = 18, border_radius = 5)  
                                # white
                                elif 0 <= level_system["tries"] <= 49:
                                    pygame.draw.rect(screen, color["white"], tile_location[i], width = 18, border_radius = 5)  
                                else:
                                    pygame.draw.rect(screen, color["white"], tile_location[i], width = 18, border_radius = 5)  
                            else:
                                pygame.draw.rect(screen, color["white"], tile_location[i], width = 18, border_radius = 5)                    
                    questions_number_rect_lst[counter].center = number_location[questions_location[counter] - 1]
 
                # numbers disappearing
                if the_duration_between_each_number - 0.2 < rem < the_duration_between_each_number:
                    questions_number_rect_lst[counter].center = -200, -200
                
                # Countdown appearing
                if the_duration_between_each_number - 3 <= rem < the_duration_between_each_number - 2:
                    show_text(screen,"3", (1205, 465), color["white"], 30, "font/fragmentcore.otf")
                if the_duration_between_each_number - 2 <= rem < the_duration_between_each_number - 1:
                    show_text(screen,"2", (1205, 465), color["white"], 30, "font/fragmentcore.otf")
                if the_duration_between_each_number - 1 <= rem < the_duration_between_each_number - 0:
                    show_text(screen,"1", (1205, 465), color["white"], 30, "font/fragmentcore.otf")
                
                # number appearing sound
                if rem == 0.1 and sound_number_appear_flag == False:
                    sound_number_appear_flag = True
                    play_sound("sound/number_appear.mp3")
                if rem == 1:
                    sound_number_appear_flag = False
                
                # countdown sound
                if the_duration_between_each_number >= 4:
                    if rem == the_duration_between_each_number - 3 and sound_countdown_3 == False:
                        sound_countdown_3 = True
                        sound_countdown_1 = False
                        sound_countdown_2 = False
                        play_sound("sound/clock_tick.wav")

                if the_duration_between_each_number >= 3:
                    if rem == the_duration_between_each_number - 2 and sound_countdown_2 == False:
                        sound_countdown_2 = True
                        sound_countdown_1 = False
                        sound_countdown_3 = False
                        play_sound("sound/clock_tick.wav")

                if the_duration_between_each_number >= 2:
                    if rem == the_duration_between_each_number - 1 and sound_countdown_1 == False:
                        sound_countdown_1 = True
                        sound_countdown_2 = False
                        sound_countdown_3 = False
                        play_sound("sound/clock_tick.wav")
                    if rem == the_duration_between_each_number - 0.5:
                        sound_countdown_1 = False

                # O,X buttons for positions and numbers
                if counter < the_number_of_questions:
                    if counter >= current_nback:
                        
                        #$%^
                        button_position_O_rect.center = 1055, 250
                        button_position_X_rect.center = 1215, 250
                        button_numbers_O_rect.center = 1055, 900
                        button_numbers_X_rect.center = 1215, 900
                        
                        button_key1_rect.center = 1055, 220
                        button_key2_rect.center = 1215, 220

                        button_key3_rect.center = 1055, 870
                        button_key4_rect.center = 1215, 870

                        # numbers O button
                        if clicked(pygame.Rect(1010, 200, 100, 100)):
                            if user_answer_numbers[counter - current_nback] == " ":
                                user_answer_numbers[counter - current_nback] = "O"
                            elif user_answer_numbers[counter - current_nback] == "O":
                                user_answer_numbers[counter - current_nback] = " "
                            elif user_answer_numbers[counter - current_nback] == "X":
                                user_answer_numbers[counter - current_nback] = "O"
                            play_sound("sound/mouseclicko.wav",volume = 0.5)

                        # numbers X button
                        if clicked(pygame.Rect(1175, 200, 100, 100)):
                            if user_answer_numbers[counter - current_nback] == " ":
                                user_answer_numbers[counter - current_nback] = "X"
                            elif user_answer_numbers[counter - current_nback] == "X":
                                user_answer_numbers[counter - current_nback] = " "
                            elif user_answer_numbers[counter - current_nback] == "O":
                                user_answer_numbers[counter - current_nback] = "X"
                            play_sound("sound/mouseclickx.wav",volume = 0.5)

                        # positions O button
                        if clicked(pygame.Rect(1010, 850, 100, 100)):
                            if user_answer_location[counter - current_nback] == " ":
                                user_answer_location[counter - current_nback] = "O"
                            elif user_answer_location[counter - current_nback] == "O":
                                user_answer_location[counter - current_nback] = " "
                            elif user_answer_location[counter - current_nback] == "X":
                                user_answer_location[counter - current_nback] = "O"
                            play_sound("sound/mouseclicko.wav",volume = 0.5)
                        
                        # positions X button
                        if clicked(pygame.Rect(1175, 850, 100, 100)):
                            if user_answer_location[counter - current_nback] == " ":
                                user_answer_location[counter - current_nback] = "X"
                            elif user_answer_location[counter - current_nback] == "X":
                                user_answer_location[counter - current_nback] = " "
                            elif user_answer_location[counter - current_nback] == "O":
                                user_answer_location[counter - current_nback] = "X"
                            play_sound("sound/mouseclickx.wav",volume = 0.5)

                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False
                            if event.type == pygame.KEYDOWN:

                                # when press p in game
                                if event.key == pygame.K_p and game_pause_flag == False:
                                    sound_countdown_flag = False
                                    sound_start_flag = False
                                    game_pause_flag = True

                                # when press p again in paused screen
                                elif event.key == pygame.K_p and game_pause_flag == True:
                                    game_pause_flag = False

                                if event.key == pygame.K_s:
                                    screenwidth = 1000
                                    screen = pygame.display.set_mode((screenwidth, screenheight))
                                    # stop_flag is for the description in score screen
                                    stop_flag = True
                                    sound_countdown_flag = False
                                    sound_start_flag = False
                                    questions_number_rect_lst[counter].center = -200, -200
                                    game = 2

                                if event.key == pygame.K_1 or event.key == pygame.K_KP_1:
                                    if user_answer_numbers[counter - current_nback] == " ":
                                        user_answer_numbers[counter - current_nback] = "O"
                                    elif user_answer_numbers[counter - current_nback] == "O":
                                        user_answer_numbers[counter - current_nback] = " "
                                    elif user_answer_numbers[counter - current_nback] == "X":
                                        user_answer_numbers[counter - current_nback] = "O"
                                    play_sound("sound/mouseclicko.wav",volume = 0.5)
                                    
                                if event.key == pygame.K_2 or event.key == pygame.K_KP_2:
                                    if user_answer_numbers[counter - current_nback] == " ":
                                        user_answer_numbers[counter - current_nback] = "X"
                                    elif user_answer_numbers[counter - current_nback] == "X":
                                        user_answer_numbers[counter - current_nback] = " "
                                    elif user_answer_numbers[counter - current_nback] == "O":
                                        user_answer_numbers[counter - current_nback] = "X"
                                    play_sound("sound/mouseclickx.wav",volume = 0.5)
                                    
                                if event.key == pygame.K_3 or event.key == pygame.K_KP_3:
                                    if user_answer_location[counter - current_nback] == " ":
                                        user_answer_location[counter - current_nback] = "O"
                                    elif user_answer_location[counter - current_nback] == "O":
                                        user_answer_location[counter - current_nback] = " "
                                    elif user_answer_location[counter - current_nback] == "X":
                                        user_answer_location[counter - current_nback] = "O"
                                    play_sound("sound/mouseclicko.wav",volume = 0.5)
                                    
                                if event.key == pygame.K_4 or event.key == pygame.K_KP_4:
                                    if user_answer_location[counter - current_nback] == " ":
                                        user_answer_location[counter - current_nback] = "X"
                                    elif user_answer_location[counter - current_nback] == "X":
                                        user_answer_location[counter - current_nback] = " "
                                    elif user_answer_location[counter - current_nback] == "O":
                                        user_answer_location[counter - current_nback] = "X"
                                    play_sound("sound/mouseclickx.wav",volume = 0.5)
                                    
                                if event.key == pygame.K_ESCAPE:
                                    run = False
                        #$%^
                        # when user submits each answer for number
                        if user_answer_numbers[counter - current_nback] == "O":
                            pygame.draw.rect(screen, color["green"], (990, 37, 290, 290), 5, border_radius = 5)
                        elif user_answer_numbers[counter - current_nback] == "X":
                            pygame.draw.rect(screen, color["red"], (990, 37, 290, 290), 5, border_radius = 5)
                        #$%^
                        # when user submits each answer for position
                        if user_answer_location[counter - current_nback] == "O":
                            pygame.draw.rect(screen, color["green"], (990, 677, 290, 290), 5, border_radius = 5)
                        elif user_answer_location[counter - current_nback] == "X":
                            pygame.draw.rect(screen, color["red"], (990, 677, 290,290), 5, border_radius = 5)
                        

                # if counter goes above the number of questions, aka if no question is left   
                elif counter >= the_number_of_questions:
                    new_start_count = new_current_count
                    #$%^
                    screenwidth = 1000
                    screen = pygame.display.set_mode((screenwidth, screenheight))
                    one_tenth_seconds = 0
                    level_system["tries"] += 1

                    # Make the file visible (if it is invisible, it can't be read), if it exists
                    if os.path.isfile("level.txt"):
                        if sys.platform == "win32":
                            os.system("attrib -h level.txt")
                        elif sys.platform == "darwin":
                            os.system("chflags nohidden level.txt")
                        elif sys.platform.startswith("linux"):
                            os.system("sudo chattr -i level.txt")
                    
                    # Make the file editable again if it it exists
                    if os.path.isfile("level.txt"):
                        if sys.platform == "win32":
                            os.system("attrib -r level.txt")
                        elif sys.platform == "darwin":
                            os.chmod("level.txt", 0o644)
                        elif sys.platform.startswith("linux"):
                            os.chmod("level.txt", 0o644)

                    # save the data into the textfile
                    with open("level.txt", "w") as levelfile:
                        json.dump(level_system, levelfile)        

                    if level_flag == False:
                        for n in range(the_number_of_questions - current_nback):
                            if answer_location[n] == user_answer_location[n]:
                                level_correct_number_of_positions += 1
                            if answer_numbers[n] == user_answer_numbers[n]:
                                level_correct_number_of_numbers += 1
                        score_for_numbers = round((level_correct_number_of_numbers / (the_number_of_questions-current_nback) * 100), 2)
                        score_for_positions = round((level_correct_number_of_positions / (the_number_of_questions-current_nback) * 100), 2)
                        
                        if current_nback == 1:
                            if score_for_numbers >= 90 and score_for_positions >= 90 and the_number_of_questions >= current_nback * 3:
                                level_system["n1_exp"] += 1
                        if current_nback == 2:
                            if score_for_numbers >= 90 and score_for_positions >= 90 and the_number_of_questions >= current_nback * 3:
                                level_system["n2_exp"] += 1
                        if current_nback == 3:
                            if score_for_numbers >= 90 and score_for_positions >= 90 and the_number_of_questions >= current_nback * 3:
                                level_system["n3_exp"] += 1
                        if current_nback == 4:
                            if score_for_numbers >= 90 and score_for_positions >= 90 and the_number_of_questions >= current_nback * 3:
                                level_system["n4_exp"] += 1
                        if current_nback == 5:
                            if score_for_numbers >= 90 and score_for_positions >= 90 and the_number_of_questions >= current_nback * 3:
                                level_system["n5_exp"] += 1
                        if current_nback == 6:
                            if score_for_numbers >= 90 and score_for_positions >= 90 and the_number_of_questions >= current_nback * 3:
                                level_system["n6_exp"] += 1
                        if current_nback == 7:
                            if score_for_numbers >= 90 and score_for_positions >= 90 and the_number_of_questions >= current_nback * 3:
                                level_system["n7_exp"] += 1
                        if current_nback == 8:
                            if score_for_numbers >= 90 and score_for_positions >= 90 and the_number_of_questions >= current_nback * 3:
                                level_system["n8_exp"] += 1
                        if current_nback == 9:
                            if score_for_numbers >= 90 and score_for_positions >= 90 and the_number_of_questions >= current_nback * 3:
                                level_system["n9_exp"] += 1

                        # Make the file visible
                        if os.path.isfile("level.txt"):
                            # For Windows
                            if sys.platform == "win32":
                                os.system("attrib -h level.txt")
                            # For MacOS
                            elif sys.platform == "darwin":
                                os.system("chflags nohidden level.txt")
                            # For Linux
                            if sys.platform == "linux" or sys.platform == "linux2":
                                os.system("chmod 644 level.txt")

                        # Make the file editable again if it it exists
                        if os.path.isfile("level.txt"):
                            if sys.platform == "win32":
                                os.system("attrib -r level.txt")
                            elif sys.platform == "darwin":
                                os.chmod("level.txt", 0o644)
                            elif sys.platform.startswith("linux"):
                                os.chmod("level.txt", 0o644)

                        # Save the data into the textfile
                        with open("level.txt", "w") as levelfile:
                            json.dump(level_system, levelfile)
                    
                    # # Make the file invisible
                    # os.system("attrib +h level.txt")

                    # # Make the file uneditable. Change the file to Read-Only.
                    # os.chmod("level.txt", S_IREAD)

                    # Make the file invisible, if it exists
                    if os.path.isfile("level.txt"):
                        if sys.platform == "win32":
                            os.system("attrib +h level.txt")
                        elif sys.platform == "darwin":
                            os.system("chflags hidden level.txt")
                        elif sys.platform.startswith("linux"):
                            os.system("sudo chattr +i level.txt")

                    # Make the file uneditable. Change the file to Read-Only.
                    if os.path.isfile("level.txt"):
                        if sys.platform == "win32":
                            os.system("attrib +r level.txt")
                        elif sys.platform == "darwin":
                            os.chmod("level.txt", 0o444)
                        elif sys.platform.startswith("linux"):
                            os.chmod("level.txt", 0o444)

                    level_correct_number_of_positions, level_correct_number_of_numbers = 0, 0
                    # level_flag = False
                    game = 2

    # score screen
    elif game == 2:
        screen.fill(color["black"])
        current_count = time.time()
        
        if score_flag == False:
            score_flag = True
            for i in range(the_number_of_questions - current_nback):
                if answer_location[i] == user_answer_location[i]:
                    correct_number_of_questions_location += 1
                if answer_numbers[i] == user_answer_numbers[i]:
                    correct_number_of_questions_numbers += 1
            texts_score[1] = round((correct_number_of_questions_location / (the_number_of_questions-current_nback) * 100), 2)
            texts_score[2] = round((correct_number_of_questions_numbers / (the_number_of_questions-current_nback) * 100), 2)
            now = datetime.datetime.now()
            a = f"\nN back Report - {datetime.datetime(now.year, now.month, now.day,now.hour, now.minute, now.second)}\nCurrent N : {current_nback} Back / Intervals : {the_duration_between_each_number}s"
            b = f"----------------------------------------\nPositions :\n|1|2|3|\n|4|5|6| <- Position grid\n|7|8|9|\nQuestions, Correct answers, your answers (below)"
            c = ""
            for cc in range(len(questions_location)):
                if cc != len(questions_location) - 1:
                    c += f"|{questions_location[cc]}"
                else:
                    c += f"|{questions_location[cc]}|"
            d = " " * 2 * current_nback
            for dd in range(len(answer_location)):
                if dd != len(answer_location) - 1:
                    d += f"|{answer_location[dd]}"
                else:
                    d += f"|{answer_location[dd]}|"
            e = " " * 2 * current_nback
            for ee in range(len(user_answer_location)):
                if ee != len(user_answer_location) - 1:
                    e += f"|{user_answer_location[ee]}"
                else:
                    e += f"|{user_answer_location[ee]}|"
            f = f"----------------------------------------\nNumbers :\nQuestions, Correct answers, your answers (below)"
            g = ""
            for gg in range(len(questions_numbers)):
                if gg != len(questions_numbers) - 1:
                    g += f"|{questions_numbers[gg]}"
                else:
                    g += f"|{questions_numbers[gg]}|"
            h = " " * 2 * current_nback
            for hh in range(len(answer_numbers)):
                if hh != len(answer_numbers) - 1:
                    h += f"|{answer_numbers[hh]}"
                else:
                    h += f"|{answer_numbers[hh]}|"
            i = " " * 2 * current_nback
            for ii in range(len(user_answer_numbers)):
                if ii != len(user_answer_numbers) - 1:
                    i += f"|{user_answer_numbers[ii]}"
                else:
                    i += f"|{user_answer_numbers[ii]}|"
            j = f"----------------------------------------\nScore for numbers : {round(texts_score[2], 2)} %"
            k = f"Score for positions : {round(texts_score[1], 2)} %\nContact creator : jsk.jinsung@gmail.com "
            result_textfile = [a, f, g, h, i, b, c, d, e, j, k]
            for each in result_textfile:
                print(each)
            
        if texts_score[2] >= 90:
            show_text(screen, str(texts_score[2]) + "%", (screenwidth / 4, 450), color["green"], 80, "font/sketched.ttf")
        elif texts_score[2] >= 50:
            show_text(screen, str(texts_score[2]) + "%", (screenwidth / 4, 450), color["white"], 80, "font/sketched.ttf")
        elif texts_score[2] >= 30:
            show_text(screen, str(texts_score[2]) + "%", (screenwidth / 4, 450), color["yellow"], 80, "font/sketched.ttf")
        else:
            show_text(screen, str(texts_score[2]) + "%", (screenwidth / 4, 450), color["red"], 80, "font/sketched.ttf")

        if texts_score[1] >= 90:
            show_text(screen, str(texts_score[1]) + "%", (screenwidth / 4 * 3, 450), color["green"], 80, "font/sketched.ttf")
        elif texts_score[1] >= 50:
            show_text(screen, str(texts_score[1]) + "%", (screenwidth / 4 * 3, 450), color["white"], 80, "font/sketched.ttf")
        elif texts_score[1] >= 30:
            show_text(screen, str(texts_score[1]) + "%", (screenwidth / 4 *3, 450), color["yellow"], 80, "font/sketched.ttf")
        else:
            show_text(screen, str(texts_score[1]) + "%", (screenwidth / 4 * 3, 450), color["red"], 80, "font/sketched.ttf")
        show_text(screen, texts_score[0], (screenwidth / 2, 100), color["white"], 100, "font/sketched.ttf")
        show_text(screen,f"Current N : {current_nback} back", (screenwidth / 2, 220), color["white"], 30, "font/F25_bank_Printer.otf")
        show_text(screen,f"The number of events : {the_number_of_questions}", (screenwidth / 2, 260), color["white"], 30, "font/F25_bank_Printer.otf")
        show_text(screen, texts_score[3], (screenwidth / 4, 350), color["white"], 50, "font/F25_bank_Printer.otf")
        show_text(screen, texts_score[4], (screenwidth / 4 * 3, 350), color["white"], 50, "font/F25_bank_Printer.otf")
        show_text(screen,texts_score[5], (screenwidth / 2, 770), color["white"], 25, "font/F25_bank_Printer.otf")
        show_text(screen, texts_score[6], (screenwidth / 2, 700), color["white"], 25, "font/F25_bank_Printer.otf")
        show_text(screen, texts_score[7], (screenwidth / 2, 840), color["white"], 30, "font/F25_bank_Printer.otf")
        show_text(screen, texts_score[8], (screenwidth / 2, 910), color["white"], 30, "font/F25_bank_Printer.otf")
        
 
        if the_number_of_questions < current_nback * 3:
            text_score_helper = f"Increase the number of events to {current_nback * 3}\nto earn a '{current_nback} back' point!"
            show_text(screen, text_score_helper, (screenwidth / 2, 580), color["white"], 15, "font/F25_bank_Printer.otf")
            if (texts_score[2] < 90) or (texts_score[1] < 90):
                show_text(screen, f"Score 90 percent or higher to earn a '{current_nback} back' point!", (screenwidth / 2, 620), color["white"], 15, "font/F25_bank_Printer.otf")
        elif the_number_of_questions >= current_nback * 3:
            if (texts_score[2] < 90) or (texts_score[1] < 90):
                show_text(screen, f"Score 90 percent or higher to earn a '{current_nback} back' point!", (screenwidth / 2, 620), color["white"], 15, "font/F25_bank_Printer.otf")
            else:
                if stop_flag == True:
                    show_text(screen, "Because you stopped the game, you can't earn a point", (screenwidth / 2, 590), color["white"], 15, "font/F25_bank_Printer.otf")
                elif level_flag == True:
                    show_text(screen, "Good job! Play new game to earn a point!", (screenwidth / 2, 590), color["white"], 15, "font/F25_bank_Printer.otf")
                else:
                    show_text(screen, f"{current_nback} back point earned!", (screenwidth / 2, 590), color["white"], 15, "font/F25_bank_Printer.otf")
        

        if button_play_with_the_same_sequence.surface_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, color["sky blue"], (260, 668, 480, 64), width = 5)
            show_text(screen, "Press 1", (785,700),color["white"],15,"font/F25_bank_Printer.otf")
        else:
            pygame.draw.rect(screen, color["dark grey"], (260, 668, 480, 64), width = 5)

        if button_save_result.surface_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, color["white"], (260, 738, 480, 64), width = 5)
            show_text(screen, "Press 2", (785,770),color["white"],15,"font/F25_bank_Printer.otf")
        else:
            pygame.draw.rect(screen, color["dark grey"], (260, 738, 480, 64), width = 5)
        
        if button_new_game.surface_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, color["green"], (260, 808, 480, 64), width = 5)
            show_text(screen, "Press 3", (785,840),color["white"],15,"font/F25_bank_Printer.otf")
        else:
            pygame.draw.rect(screen, color["dark grey"], (260, 808, 480, 64), width = 5)

        if button_main_menu.surface_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, color["yellow"], (260, 878, 480, 64), width = 5)
            show_text(screen, "Press 4", (785,910),color["white"],15,"font/F25_bank_Printer.otf")
        else:
            pygame.draw.rect(screen, color["dark grey"], (260, 878, 480, 64), width = 5)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    screenwidth = 1300
                    screen = pygame.display.set_mode((screenwidth, screenheight))
                    counter = 0
                    questions_start = False
                    user_answer_location = [" " for _ in range(len(answer_location))]
                    user_answer_numbers = [" " for _ in range(len(answer_numbers))]
                    for i in range(len(user_answer_location)):
                        questions_number_rect_lst[i].center = -200, -200
                    score_flag = False
                    button_save_result_flag = False
                    start_count_game_screen = False
                    stop_flag = False
                    level_flag = True
                    correct_number_of_questions_location = 0
                    correct_number_of_questions_numbers = 0
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    reposition_imgs()
                    sound_start_flag = False
                    lst_texts_in_game[0] = "Start!"
                    button_position_O_rect.center = -200, -200
                    button_position_X_rect.center = -200, -200
                    button_numbers_O_rect.center = -200, -200
                    button_numbers_X_rect.center = -200, -200
                    button_key1_rect.center = -200, -200
                    button_key2_rect.center = -200, -200
                    button_key3_rect.center = -200, -200
                    button_key4_rect.center = -200, -200
                    one_tenth_seconds = 0
                    game = 1
                if (event.key == pygame.K_2 and button_save_result_flag == False) or (event.key == pygame.K_KP2 and button_save_result_flag == False):
                    button_save_result_flag = True
                    with open(f"N back Result({now.date()}).txt", "a", encoding = "utf-8") as file:
                        for line in result_textfile:
                            file.writelines(line)
                            file.write("\n")
                        file.write("\n")
                
                # New game
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    screenwidth = 1300
                    screen = pygame.display.set_mode((screenwidth, screenheight))
                    counter = 0
                    questions_start = False
                    regenerate_sequence()
                    score_flag = False
                    button_save_result_flag = False
                    start_count_game_screen = False
                    stop_flag = False
                    practice_the_same_sequence_flag = False
                    correct_number_of_questions_location = 0
                    correct_number_of_questions_numbers = 0
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    reposition_imgs()
                    sound_start_flag = False
                    lst_texts_in_game[0] = "Start!"
                    button_position_O_rect.center = -200, -200
                    button_position_X_rect.center = -200, -200
                    button_numbers_O_rect.center = -200, -200
                    button_numbers_X_rect.center = -200, -200
                    button_key1_rect.center = -200, -200
                    button_key2_rect.center = -200, -200
                    button_key3_rect.center = -200, -200
                    button_key4_rect.center = -200, -200
                    one_tenth_seconds = 0
                    game = 1
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    counter = 0
                    questions_start = False
                    score_flag = False
                    button_save_result_flag = False
                    start_count_game_screen = False
                    stop_flag = False
                    correct_number_of_questions_location = 0
                    correct_number_of_questions_numbers = 0
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    reposition_imgs()
                    sound_start_flag = False
                    lst_texts_in_game[0] = "Start!"
                    button_position_O_rect.center = -200, -200
                    button_position_X_rect.center = -200, -200
                    button_numbers_O_rect.center = -200, -200
                    button_numbers_X_rect.center = -200, -200
                    button_key1_rect.center = -200, -200
                    button_key2_rect.center = -200, -200
                    button_key3_rect.center = -200, -200
                    button_key4_rect.center = -200, -200
                    main_menu_flag = True
                    one_tenth_seconds = 0
                    game = 0
        # when user clicks 'practice the same sequence' button
        if clicked(button_play_with_the_same_sequence.surface_rect):
            screenwidth = 1300
            screen = pygame.display.set_mode((screenwidth, screenheight))
            counter = 0
            questions_start = False
            user_answer_location = [" " for _ in range(len(answer_location))]
            user_answer_numbers = [" " for _ in range(len(answer_numbers))]
            for i in range(len(user_answer_location)):
                questions_number_rect_lst[i].center = -200, -200
            score_flag = False
            button_save_result_flag = False
            start_count_game_screen = False
            stop_flag = False
            level_flag = True
            correct_number_of_questions_location = 0
            correct_number_of_questions_numbers = 0
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            reposition_imgs()
            sound_start_flag = False
            lst_texts_in_game[0] = "Start!"
            button_position_O_rect.center = -200, -200
            button_position_X_rect.center = -200, -200
            button_numbers_O_rect.center = -200, -200
            button_numbers_X_rect.center = -200, -200
            button_key1_rect.center = -200, -200
            button_key2_rect.center = -200, -200
            button_key3_rect.center = -200, -200
            button_key4_rect.center = -200, -200
            one_tenth_seconds = 0
            game = 1
        
        # when user clicks 'Save result as text' button
        if clicked(button_save_result.surface_rect) and button_save_result_flag == False:
            button_save_result_flag = True
            print(f'The file is saved!\nFile name : N back Result({now.date()}).txt')
            with open(f"N back Result({now.date()}).txt", "a", encoding = "utf-8") as file:
                for line in result_textfile:
                    file.writelines(line)
                    file.write("\n")
                file.write("\n")
        
        # when user clicks 'New game' button
        if clicked(button_new_game.surface_rect):
            screenwidth = 1300
            screen = pygame.display.set_mode((screenwidth, screenheight))
            counter = 0
            questions_start = False
            regenerate_sequence()
            score_flag = False
            button_save_result_flag = False
            start_count_game_screen = False
            stop_flag = False
            correct_number_of_questions_location = 0
            correct_number_of_questions_numbers = 0
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            reposition_imgs()
            sound_start_flag = False
            lst_texts_in_game[0] = "Start!"
            button_position_O_rect.center = -200, -200
            button_position_X_rect.center = -200, -200
            button_numbers_O_rect.center = -200, -200
            button_numbers_X_rect.center = -200, -200
            button_key1_rect.center = -200, -200
            button_key2_rect.center = -200, -200
            button_key3_rect.center = -200, -200
            button_key4_rect.center = -200, -200
            one_tenth_seconds = 0
            game = 1
        
        # when user clicks 'Main menu' button
        if clicked(button_main_menu.surface_rect):
            counter = 0
            questions_start = False
            score_flag = False
            button_save_result_flag = False
            start_count_game_screen = False
            stop_flag = False
            correct_number_of_questions_location = 0
            correct_number_of_questions_numbers = 0
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            reposition_imgs()
            sound_start_flag = False
            lst_texts_in_game[0] = "Start!"
            button_position_O_rect.center = -200, -200
            button_position_X_rect.center = -200, -200
            button_numbers_O_rect.center = -200, -200
            button_numbers_X_rect.center = -200, -200
            button_key1_rect.center = -200, -200
            button_key2_rect.center = -200, -200
            button_key3_rect.center = -200, -200
            button_key4_rect.center = -200, -200
            main_menu_flag = True
            one_tenth_seconds = 0
            game = 0

    # game settings
    elif game == 3:
        screen.fill(color["black"])

        """
        texts_game_settings = [
                                "Game settings","# N", "Choices <numbers>",
                                "Choices <positions>", "# of events",
                                "Time intervals(s)", "Main menu", "(Press 'm')",
                                "(1 ~ 9, default : 1)","(2 ~ 9, default : 9)",
                                "(2 ~ 9, default : 9)", "(Current N + 1 ~ 99, default : 10)",
                                "(2 ~ 99, default : 5)"
                              ]
        """
        show_text(screen, texts_game_settings[0], (screenwidth / 2, 110), color["green"], 70, "font/sketched.ttf")
        show_text(screen, texts_game_settings[1], (152, 230-18), color["white"], 33, "font/F25_bank_Printer.otf",False)
        show_text(screen, texts_game_settings[2], (152, 340-18), color["white"], 33, "font/F25_bank_Printer.otf",False)
        show_text(screen, texts_game_settings[3],(152, 470-18), color["white"], 33, "font/F25_bank_Printer.otf",False)
        show_text(screen,texts_game_settings[4], (152, 590-18), color["white"], 33, "font/F25_bank_Printer.otf",False)
        show_text(screen,texts_game_settings[5], (152, 710-18), color["white"], 33, "font/F25_bank_Printer.otf",False)
        show_text(screen, texts_game_settings[6], (screenwidth / 2, 890), color["white"], 50, "font/sketched.ttf")
        show_text(screen,texts_game_settings[7], (screenwidth / 2, 930), color["not too bright white"], 15, "font/F25_bank_Printer.otf")
        show_text(screen, texts_game_settings[8], (675, 230), color["not too bright white"], 25, "font/cleanfont.ttf")
        show_text(screen, texts_game_settings[9], (670, 340), color["not too bright white"], 25, "font/cleanfont.ttf")
        show_text(screen, texts_game_settings[10], (670, 470), color["not too bright white"], 25, "font/cleanfont.ttf")
        show_text(screen, texts_game_settings[11], (615, 590), color["not too bright white"], 25, "font/cleanfont.ttf")
        show_text(screen, texts_game_settings[12], (665, 710), color["not too bright white"], 25, "font/cleanfont.ttf")
        show_text(screen, "Choose how many different numbers will appear in a game", (screenwidth / 2 - 100, 390), color["light grey"], 25, "font/cleanfont.ttf")
        show_text(screen,"For example, if you choose 5, then only numbers 1 to 5 may appear", (screenwidth / 2 - 65, 420), color["light grey"], 25, "font/cleanfont.ttf")
        show_text(screen, "Choose how many different tile positions will appear in a game", (screenwidth / 2 - 85, 512), color["light grey"], 25, "font/cleanfont.ttf")
        show_text(screen,"Length of time each number and tile will appear on the screen",(screenwidth / 2 - 82, 750), color["light grey"], 25, "font/cleanfont.ttf")
        
        """
        a : nback                       ex) 2 => 2 back
                                        ex) 6 => 6 back
        b : choice of numbers.          ex) 5 => display numbers between 1~5
                                        ex) 9 => display numbers between 1~9
        c : choice of positions.        ex) 5 => display position tile between 1~5
        d : number of questions.        ex) 12 => 12 different (number, position) pair will show up
        e : duration between questions. ex) 5 => each (number, position) pair shows up for 5 seconds
        """
        a = font_banknumbers.render(user_nback, True, color["not too bright white"])
        b = font_banknumbers.render(user_choices_numbers, True, color["not too bright white"])
        c = font_banknumbers.render(user_choices_positions, True, color["not too bright white"])
        d = font_banknumbers.render(user_number_of_questions, True, color["not too bright white"])
        e = font_banknumbers.render(user_the_duration_between_each_number, True, color["not too bright white"])
        screen.blit(a, (800,210))
        screen.blit(b, (800,330))
        screen.blit(c, (800,450))
        if len(user_number_of_questions) == 2:
            screen.blit(d, (780,570))
        elif len(user_number_of_questions) == 1:
            screen.blit(d, (800,570))
        if len(user_the_duration_between_each_number) == 2:
            screen.blit(e, (780,690))
        elif len(user_the_duration_between_each_number) == 1:
            screen.blit(e, (800,690))


        if hovered(game_settings_main_menu_rect) or user_main_menu_flag == True:
            pygame.draw.rect(screen,color["green"],(340,850,320,100),3,2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if user_input_n_rect.collidepoint(event.pos):
                    play_sound("sound/key.wav")
                    user_input_n_flag = True
                else:
                    user_input_n_flag = False
                if user_input_choices_numbers_rect.collidepoint(event.pos):
                    play_sound("sound/key.wav")
                    user_input_choices_numbers_flag = True
                else:
                    user_input_choices_numbers_flag = False
                if user_input_choices_positions_rect.collidepoint(event.pos):
                    play_sound("sound/key.wav")
                    user_input_choices_positions_flag = True
                else:
                    user_input_choices_positions_flag = False
                if user_input_number_of_questions_rect.collidepoint(event.pos):
                    play_sound("sound/key.wav")
                    user_input_number_of_questions_flag = True
                else:
                    user_input_number_of_questions_flag = False
                if user_input_time_intervals_rect.collidepoint(event.pos):
                    play_sound("sound/key.wav")
                    user_input_time_intervals_flag = True
                else:
                    user_input_time_intervals_flag = False
                if game_settings_main_menu_rect.collidepoint(event.pos):
                    play_sound("sound/click1.wav")
                    user_main_menu_flag = True
                    game = 0
                else:
                    user_main_menu_flag = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_BACKSPACE:
                    
                    if not (user_input_n_flag or user_input_choices_numbers_flag or user_input_choices_positions_flag or user_input_number_of_questions_flag or user_input_time_intervals_flag):
                        play_sound("sound/click1.wav")
                        game = 0
                    else:
                        play_sound("sound/key.wav")
                if event.key == pygame.K_RETURN:
                    play_sound("sound/click1.wav")
                    if user_main_menu_flag == True:
                        game = 0
                if event.key == pygame.K_m:
                    play_sound("sound/click1.wav")
                    if (user_input_n_flag == True and user_nback == "") or (user_input_n_flag == True and int(user_nback) == 0):
                        user_nback = "1"
                        current_nback = 1
                    elif (user_input_choices_numbers_flag == True and user_choices_numbers == "") or (user_input_choices_numbers_flag == True and (int(user_choices_numbers) == 0 or int(user_choices_numbers) == 1)):
                        user_choices_numbers = "9"
                        choices_numbers = 9
                    elif (user_input_choices_positions_flag == True and user_choices_positions == "") or (user_input_choices_positions_flag == True and (int(user_choices_positions) == 0 or int(user_choices_positions) == 1)):
                        user_choices_positions = "9"
                        choices_positions = 9
                    elif (user_input_number_of_questions_flag == True and user_number_of_questions == "") or (user_input_number_of_questions_flag == True and int(user_number_of_questions) == 0) or (user_input_number_of_questions_flag == True and int(user_number_of_questions)<=current_nback):
                        user_number_of_questions = str(10)
                        the_number_of_questions = 10
                    elif (user_input_time_intervals_flag == True and user_the_duration_between_each_number == "") or (user_input_time_intervals_flag == True and (int(user_the_duration_between_each_number) == 0 or int(user_the_duration_between_each_number) == 1)):
                        user_the_duration_between_each_number = "5"
                        the_duration_between_each_number = 5
                    else:
                        game = 0
                if event.key == pygame.K_TAB:
                    play_sound("sound/key.wav")
                    if user_input_n_flag == False and user_input_choices_numbers_flag == False and user_input_choices_positions_flag == False and user_input_number_of_questions_flag == False and user_input_time_intervals_flag == False and user_main_menu_flag == False:
                        user_input_n_flag = True 
                    elif user_input_n_flag == True:
                        user_input_n_flag = False
                        user_input_choices_numbers_flag = True
                    elif user_input_choices_numbers_flag == True:
                        user_input_choices_numbers_flag = False
                        user_input_choices_positions_flag = True
                    elif user_input_choices_positions_flag == True:
                        user_input_choices_positions_flag = False
                        user_input_number_of_questions_flag = True
                    elif user_input_number_of_questions_flag == True:
                        user_input_number_of_questions_flag = False
                        user_input_time_intervals_flag = True
                    elif user_input_time_intervals_flag == True:
                        user_input_time_intervals_flag = False
                        user_main_menu_flag = True

                    elif user_main_menu_flag == True:
                        user_main_menu_flag = False
                        user_input_n_flag = True
                        

                if user_input_n_flag == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_nback = user_nback[:-1]
                        if user_nback != "":
                            current_nback = int(user_nback)
                        else:
                            current_nback = 1
                    else:
                        if event.unicode.isdigit():
                            play_sound("sound/key.wav")
                            if (0 <= len(user_nback) < 1):
                            
                                user_nback += event.unicode
                                current_nback = int(user_nback)

                if user_input_choices_numbers_flag == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_choices_numbers = user_choices_numbers[:-1]
                    else:
                        
                        if event.unicode.isdigit():
                            play_sound("sound/key.wav")
                            if (0 <= len(user_choices_numbers) < 1):
                            
                                user_choices_numbers += event.unicode
                                choices_numbers = int(user_choices_numbers)
                if user_input_choices_positions_flag == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_choices_positions = user_choices_positions[:-1]
                    else:
                        
                        if event.unicode.isdigit():
                            play_sound("sound/key.wav")
                            if (0 <= len(user_choices_positions) < 1):
                            
                                user_choices_positions += event.unicode
                                choices_positions = int(user_choices_positions)
                if user_input_number_of_questions_flag == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_number_of_questions = user_number_of_questions[:-1]
                    else:
                        
                        if event.unicode.isdigit():
                            play_sound("sound/key.wav")
                            if (0 <= len(user_number_of_questions) <= 1):
                            
                                user_number_of_questions += event.unicode
                                the_number_of_questions = int(user_number_of_questions)
                if user_input_time_intervals_flag == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_the_duration_between_each_number = user_the_duration_between_each_number[:-1]
                    else:
                        
                        if event.unicode.isdigit():
                            play_sound("sound/key.wav")
                            if (0 <= len(user_the_duration_between_each_number) <= 1):
                            
                                user_the_duration_between_each_number += event.unicode
                                the_duration_between_each_number = int(user_the_duration_between_each_number)
                                
                if user_main_menu_flag == True:
                    pygame.draw.rect(screen, color["green"], (340, 850, 320, 100), 3, 2)
                
        # user input box color, width changes upon clicking, and mouse cursor appears
        cursor_current_time = time.time()
        if user_input_n_flag == False:
            pygame.draw.rect(screen, color["light grey"], user_input_n_rect, 2)
        else:
            pygame.draw.rect(screen, color["white"], user_input_n_rect, 4)
            if mouse_cursor_time_flag == 0:
                mouse_cursor_time_flag = 1
                cursor_start_time = time.time()
            if cursor_current_time - cursor_start_time > 1.6:
                cursor_start_time = cursor_current_time
            if 0 < cursor_current_time - cursor_start_time < 0.8:
                if len(user_nback) == 1:
                    pygame.draw.line(screen, color["white"], (837, 208), (837, 258))
                elif len(user_nback) == 0:
                    pygame.draw.line(screen,color["white"], (792, 208), (792, 258))

        if user_input_choices_numbers_flag == False:
            pygame.draw.rect(screen, color["light grey"], user_input_choices_numbers_rect, 2)
        else:
            pygame.draw.rect(screen, color["white"], user_input_choices_numbers_rect, 4)
            if mouse_cursor_time_flag == 0:
                mouse_cursor_time_flag = 2
                cursor_start_time = time.time()
            if cursor_current_time - cursor_start_time > 1.6:
                cursor_start_time = cursor_current_time
            if 0 < cursor_current_time - cursor_start_time < 0.8:    
                if len(user_choices_numbers) == 1:
                    pygame.draw.line(screen, color["white"], (837, 328), (837, 378))
                elif len(user_choices_numbers) == 0:
                    pygame.draw.line(screen, color["white"], (797, 328), (797, 378))
        
        if user_input_choices_positions_flag == False:
            pygame.draw.rect(screen, color["light grey"], user_input_choices_positions_rect, 2)
        else:
            pygame.draw.rect(screen, color["white"], user_input_choices_positions_rect, 4)
            if mouse_cursor_time_flag == 0:
                mouse_cursor_time_flag = 3
                cursor_start_time = time.time()
            if cursor_current_time - cursor_start_time > 1.6:
                cursor_start_time = cursor_current_time
            if 0 < cursor_current_time - cursor_start_time < 0.8:    
                if len(user_choices_positions) == 1:
                    pygame.draw.line(screen, color["white"], (837, 448), (837, 498))
                elif len(user_choices_positions) == 0:
                    pygame.draw.line(screen,color["white"], (797, 448), (797, 498))

        if user_input_number_of_questions_flag == False:
            pygame.draw.rect(screen, color["light grey"], user_input_number_of_questions_rect, 2)
        else:
            pygame.draw.rect(screen, color["white"], user_input_number_of_questions_rect, 4)
            if mouse_cursor_time_flag == 0:
                mouse_cursor_time_flag = 4
                cursor_start_time = time.time()
            if cursor_current_time - cursor_start_time > 1.6:
                cursor_start_time = cursor_current_time
            if 0 < cursor_current_time - cursor_start_time < 0.8:    
                if len(user_number_of_questions) == 2:
                    pygame.draw.line(screen, color["white"], (846, 568), (846, 618))
                elif len(user_number_of_questions) == 1:
                    pygame.draw.line(screen, color["white"], (837, 568), (837, 618))
                elif len(user_number_of_questions) == 0:
                    pygame.draw.line(screen, color["white"], (797, 568), (797, 618))
        
        if user_input_time_intervals_flag == False:
            pygame.draw.rect(screen, color["light grey"], user_input_time_intervals_rect, 2)
        else:
            pygame.draw.rect(screen, color["white"], user_input_time_intervals_rect, 4)
            if mouse_cursor_time_flag == 0:
                mouse_cursor_time_flag = 5
                cursor_start_time = time.time()
            if cursor_current_time - cursor_start_time > 1.6:
                cursor_start_time = cursor_current_time
            if 0 < cursor_current_time - cursor_start_time < 0.8:    
                if len(user_the_duration_between_each_number) == 2:
                    pygame.draw.line(screen, color["white"], (846, 688), (846, 738))
                elif len(user_the_duration_between_each_number) == 1:
                    pygame.draw.line(screen, color["white"], (837, 688), (837, 738))
                elif len(user_the_duration_between_each_number) == 0:
                    pygame.draw.line(screen, color["white"], (797, 688), (797, 738))

        # just in case users put inappropriate input
        if (user_input_n_flag == False and user_nback == "") or (user_input_n_flag == False and int(user_nback) == 0):
            user_nback = "1"
            current_nback = 1
        
        if (user_input_choices_numbers_flag == False and user_choices_numbers == "") or (user_input_choices_numbers_flag == False and (int(user_choices_numbers) == 0 or int(user_choices_numbers) == 1)):
            user_choices_numbers = "9"
            choices_numbers = 9
        
        if (user_input_choices_positions_flag == False and user_choices_positions == "") or (user_input_choices_positions_flag == False and (int(user_choices_positions) == 0 or int(user_choices_positions) == 1)):
            user_choices_positions = "9"
            choices_positions = 9
        
        if (user_input_number_of_questions_flag == False and user_number_of_questions == "") or (user_input_number_of_questions_flag == False and int(user_number_of_questions) == 0) or (user_input_number_of_questions_flag == False and int(user_number_of_questions)<=current_nback):
            user_number_of_questions = "10"
            the_number_of_questions = 10
        
        if (user_input_time_intervals_flag == False and user_the_duration_between_each_number == "") or (user_input_time_intervals_flag == False and (int(user_the_duration_between_each_number) == 0 or int(user_the_duration_between_each_number) == 1)):
            user_the_duration_between_each_number = "5"
            the_duration_between_each_number = 5

    # scoreboard
    elif game == 4:
        screen.fill(color["dark dark grey"])
        multiline_text(screen, 80, texts_scoreboard[0], color["white"], (screenwidth / 2, 140), 20)
        try:
            with open("level.txt") as file:
                level_system = json.load(file)
        except:
            pass
        
        if level_system["n9_exp"] >= 100:
            pygame.draw.rect(screen, color["black"], (200, 355, 600, 50), border_radius = 2)
            starimg = pygame.image.load("img/star.png")
            starimg_rect = starimg.get_rect(center = (screenwidth / 2 - 45, 380))
            starimg_rect2 = starimg.get_rect(center = (screenwidth / 2, 380))
            starimg_rect3 = starimg.get_rect(center = (screenwidth / 2 + 45, 380))
            screen.blit(starimg, starimg_rect)
            screen.blit(starimg, starimg_rect2)
            screen.blit(starimg, starimg_rect3)
            show_text(screen, "God", (screenwidth / 2, 470), color["white"], 50, "font/F25_bank_Printer.otf")
        elif level_system["n8_exp"] >= 100:
            pygame.draw.rect(screen, color["black"], (200, 355, 600, 50), border_radius = 2)
            starimg = pygame.image.load("img/star.png")
            starimg_rect = starimg.get_rect(center = (screenwidth / 2 - 25, 380))
            starimg_rect2 = starimg.get_rect(center = (screenwidth / 2 + 25, 380))
            screen.blit(starimg, starimg_rect)
            screen.blit(starimg, starimg_rect2)
            show_text(screen,"Grand Master", (screenwidth / 2, 470), color["white"], 50, "font/F25_bank_Printer.otf")
        elif level_system["n7_exp"] >= 100:
            pygame.draw.rect(screen, color["black"], (200, 355, 600, 50), border_radius = 2)
            starimg = pygame.image.load("img/star.png")
            starimg_rect = starimg.get_rect(center = (screenwidth / 2, 380))
            screen.blit(starimg, starimg_rect)
            show_text(screen, "Master", (screenwidth / 2, 470), color["white"], 50, "font/F25_bank_Printer.otf")
        elif (100 <= level_system["tries"] and level_system["n6_exp"] >= 30) or level_system["n6_exp"] >= 60:
            pygame.draw.rect(screen, color["black"], (200, 355, 600, 50), border_radius = 2)
            show_text(screen, "black", (screenwidth / 2, 470), color["black"], 50, "font/F25_bank_Printer.otf")
        elif (100 <= level_system["tries"] and level_system["n5_exp"] >= 25) or level_system["n5_exp"] >= 50:
            pygame.draw.rect(screen, color["red"], (200, 355, 600, 50), border_radius = 2)
            show_text(screen, "red", (screenwidth / 2, 470), color["red"], 50, "font/F25_bank_Printer.otf")
        elif (80 <= level_system["tries"] and level_system["n4_exp"] >= 20) or level_system["n4_exp"] >= 40:
            pygame.draw.rect(screen, color["brown"], (200, 355, 600, 50), border_radius = 2)
            show_text(screen, "brown", (screenwidth / 2, 470), color["brown"], 50, "font/F25_bank_Printer.otf")
        elif (50 <= level_system["tries"] and level_system["n3_exp"] >= 15) or level_system["n3_exp"] >= 30:
            pygame.draw.rect(screen, color["dark green"], (200, 355, 600, 50), border_radius = 2)
            show_text(screen,"green", (screenwidth / 2, 470), color["dark green"], 50, "font/F25_bank_Printer.otf")
        elif (50 <= level_system["tries"] and level_system["n2_exp"] >= 10) or level_system["n2_exp"] >= 20:
            pygame.draw.rect(screen, color["sky blue"], (200, 355, 600,50), border_radius = 2)
            show_text(screen, "blue", (screenwidth / 2, 470), color["sky blue"], 50, "font/F25_bank_Printer.otf")
        elif (50 <= level_system["tries"] and level_system["n1_exp"] >= 5) or level_system["n1_exp"] >= 10:
            pygame.draw.rect(screen, color["yellow"], (200, 355, 600, 50), border_radius = 2)
            show_text(screen, "yellow", (screenwidth / 2, 470), color["yellow"], 50, "font/F25_bank_Printer.otf")
        elif 0 <= level_system["tries"] <= 49:
            pygame.draw.rect(screen, color["white"], (200, 355, 600, 50), border_radius = 2)
            show_text(screen, "white", (screenwidth / 2, 470), color["white"], 50, "font/F25_bank_Printer.otf")
        else:
            pygame.draw.rect(screen, color["white"], (200, 355, 600, 50), border_radius = 2)
            show_text(screen, "white", (screenwidth / 2, 470), color["white"], 50, "font/F25_bank_Printer.otf")
        
        # show completed games
        show_text(screen,f"Completed games : {level_system['tries']}", (screenwidth / 2, 735), color["white"], 15, "font/F25_bank_Printer.otf")
        show_text(screen,"<Points>", (screenwidth / 2, 765), color["white"], 15, "font/F25_bank_Printer.otf")
        show_text(screen,f"1 back : {level_system['n1_exp']}   /   2 back : {level_system['n2_exp']}   /   3 back : {level_system['n3_exp']}", (screenwidth / 2, 795), color["white"], 15, "font/F25_bank_Printer.otf")
        show_text(screen,f"4 back : {level_system['n4_exp']}   /   5 back : {level_system['n5_exp']}   /   6 back : {level_system['n6_exp']}", (screenwidth / 2, 815), color["white"], 15, "font/F25_bank_Printer.otf")
        show_text(screen,f"7 back : {level_system['n7_exp']}   /   8 back : {level_system['n8_exp']}   /   9 back : {level_system['n9_exp']}", (screenwidth / 2, 835), color["white"], 15, "font/F25_bank_Printer.otf")

        if hovered(pygame.draw.circle(screen, color["white"], (screenwidth / 2 - (70 * 4) - 35, 560), 20)):
            multiline_text(screen, 15, "<White belt>\n\nEveryone starts here\nA humble beginner", color["white"], (screenwidth / 2, 610), 10, "font/F25_bank_Printer.otf")
        
        if hovered(pygame.draw.circle(screen, color["yellow"], (screenwidth / 2 - (70 * 3) - 35, 560), 20)):
            multiline_text(screen, 15, "<Yellow belt>\n\nRequirements:\n\nComplete games 50 times & 1 back point : 5\nOr\n1 back point : 10", color["white"], (screenwidth / 2, 610), 1, "font/F25_bank_Printer.otf")
            
        if hovered(pygame.draw.circle(screen, color["sky blue"], (screenwidth / 2 - (70 * 2) - 35, 560), 20)):
            multiline_text(screen, 15, "<Blue belt>\n\nRequirements:\n\nComplete games 50 times & 2 back point : 10\nOr\n2 back point : 20", color["white"], (screenwidth/2,610), 1, "font/F25_bank_Printer.otf")
        
        if hovered(pygame.draw.circle(screen, color["green"], (screenwidth / 2 - (70 * 1) - 35, 560), 20)):
            multiline_text(screen, 15, "<Green belt>\n\nRequirements:\n\nComplete games 50 times & 3 back point : 15\nOr\n3 back point : 30", color["white"], (screenwidth / 2, 610), 1, "font/F25_bank_Printer.otf")
        
        if hovered(pygame.draw.circle(screen, color["brown"], (screenwidth / 2 + (70 * 0) - 35, 560), 20)):
            multiline_text(screen, 15, "<Brown belt>\n\nRequirements:\n\nComplete games 80 times & 4 back point : 20\nOr\n4 back point : 40", color["white"], (screenwidth / 2, 610), 1, "font/F25_bank_Printer.otf")
        
        if hovered(pygame.draw.circle(screen, color["red"],(screenwidth / 2 + (70 * 0) + 35, 560), 20)):
            multiline_text(screen, 15, "<Red belt>\n\nRequirements:\n\nComplete games 100 times & 5 back point : 25\nOr\n5 back point : 50", color["white"], (screenwidth / 2, 610), 1, "font/F25_bank_Printer.otf")
        
        if hovered(pygame.draw.circle(screen, color["black"], (screenwidth / 2 + (70 * 1) + 35, 560), 20)):
            multiline_text(screen, 15, "<Black belt>\n\nRequirements:\n\nComplete games 100 times & 6 back point : 30\nOr\n6 back point : 60", color["white"], (screenwidth / 2, 610), 1, "font/F25_bank_Printer.otf")

        if level_system["tries"] >= 50:
            pygame.draw.circle(screen, color["black"], (screenwidth / 2 + (70 * 2) + 35, 560), 20)
            starimg = pygame.image.load("img/star.png")
            starimg = pygame.transform.scale(starimg, (10, 10))
            starimg_rect = starimg.get_rect(center = (screenwidth / 2 + (70 * 2) + 35, 559))
            screen.blit(starimg, starimg_rect)
            if hovered(pygame.Rect(655, 540, 40, 40)):
                multiline_text(screen, 15, "<Master>\n\nRequirements:\n\n7 back point : 100", color["white"], (screenwidth / 2, 610), 1, "font/F25_bank_Printer.otf")
                
        else:
            pygame.draw.circle(screen, color["light grey"], (screenwidth / 2 + (70 * 2) + 35, 560), 20)
            if hovered(pygame.Rect(655, 540, 40, 40)):
                multiline_text(screen, 15, "Locked\nComplete 50 games to unlock", color["white"], (screenwidth / 2, 610), 25, "font/F25_bank_Printer.otf")
                

        if level_system["tries"] >= 75:
            pygame.draw.circle(screen, color["black"], (screenwidth / 2 + (70 * 3) + 35, 560), 20)
            starimg = pygame.image.load("img/star.png")
            starimg = pygame.transform.scale(starimg, (10, 10))
            starimg_rect = starimg.get_rect(center = (screenwidth / 2 + (70 * 3) + 35 - 8, 559))
            starimg_rect2 = starimg.get_rect(center = (screenwidth/2 + (70 * 3) + 35 + 8, 559))
            screen.blit(starimg, starimg_rect)
            screen.blit(starimg, starimg_rect2)
            if hovered(pygame.Rect(725, 540, 40, 40)):
                multiline_text(screen, 15, "<Grand Master>\n\nRequirements:\n\n8 back point : 100", color["white"], (screenwidth / 2, 610), 1, "font/F25_bank_Printer.otf")
                
        else:
            pygame.draw.circle(screen, color["light grey"], (screenwidth / 2 + (70 * 3) + 35, 560), 20)
            if hovered(pygame.Rect(725, 540, 40, 40)):
                multiline_text(screen, 15, "Locked\nComplete 75 games to unlock", color["white"], (screenwidth / 2, 610), 25, "font/F25_bank_Printer.otf")
                
        
        if level_system["tries"] >= 100:
            pygame.draw.circle(screen, color["black"], (screenwidth / 2 + (70 * 4) + 35, 560), 20)
            starimg = pygame.image.load("img/star.png")
            starimg = pygame.transform.scale(starimg, (10, 10))
            starimg_rect = starimg.get_rect(center = (screenwidth / 2 + (70 * 4) + 35 - 8, 555))
            starimg_rect2 = starimg.get_rect(center = (screenwidth / 2 + (70 * 4) + 35 + 8, 555))
            starimg_rect3 = starimg.get_rect(center = (screenwidth / 2 + (70 *4 ) + 35, 565))
            screen.blit(starimg, starimg_rect)
            screen.blit(starimg, starimg_rect2)
            screen.blit(starimg, starimg_rect3)
            if hovered(pygame.Rect(795, 540, 40, 40)):
                multiline_text(screen, 15, "<God>\n\nRequirements:\n\n9 back point : 100", color["white"], (screenwidth / 2, 610), 1, "font/F25_bank_Printer.otf")
        else:
            pygame.draw.circle(screen, color["light grey"], (screenwidth / 2 + (70 * 4) + 35, 560), 20)
            if hovered(pygame.Rect(795, 540, 40, 40)):
                multiline_text(screen, 15, "Locked\nComplete 100 games to unlock", color["white"], (screenwidth / 2, 610), 25, "font/F25_bank_Printer.otf")
                
        show_text(screen, "Main menu", (screenwidth / 2, 890), color["white"], 50, "font/sketched.ttf")
        show_text(screen, "(Press 'm')", (screenwidth / 2, 930), color["white"], 15, "font/F25_bank_Printer.otf")
        
        if hovered(pygame.Rect(340, 850, 320, 100)):
            pygame.draw.rect(screen, color["green"], (340, 850, 320, 100), 3, 2)
        
        if clicked(pygame.Rect(340, 850, 320, 100)):
            play_sound("sound/click1.wav")
            game = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m or event.key == pygame.K_BACKSPACE:
                    play_sound("sound/click1.wav")
                    game = 0
                if event.key == pygame.K_ESCAPE:
                    run = False

    # how to play
    elif game == 5:
        screen.fill(color["black"])
        show_text(screen,texts_how_to_play[0], (screenwidth / 2, 70), color["yellow"], 75, "font/sketched.ttf")
        show_text(screen,"1. Description",(315,160),color["white"],30,"font/F25_bank_Printer.otf")
        show_text(screen,"2. Tutorial",(685,160),color["white"],30,"font/F25_bank_Printer.otf")
        
        # click description
        if clicked(pygame.Rect(130, 130, 370, 60)):
            tutorial_time_flag = False
            description_flag = True
            tutorial_flag = False
            tutorial_answer = [" "," "]
            texts_tutorials = ["\n\n"," "]
            texts_tutorials_coordinates[0] = [-2000,-2000]
            texts_tutorials_coordinates[1] = [-2000,-2000]
            play_sound("sound/click1.wav")

        # click tutorial
        if clicked(pygame.Rect(500, 130, 370, 60)) and description_flag == True:
            tutorial_time_flag = False
            texts_tutorials = ["\n\n"," "]
            texts_tutorials_coordinates[0] = [-2000,-2000]
            texts_tutorials_coordinates[1] = [-2000,-2000]
            tutorial_answer = [" "," "]
            tutorial_flag = True
            description_flag = False
            play_sound("sound/click1.wav")
            
        if description_flag == True:
            pygame.draw.rect(screen,color["white"],(130, 130, 370, 60),2)
            multiline_text(screen, 30, texts_how_to_play[1], color["white"], (screenwidth / 2, 230), 1, "font/cleanfont.ttf")
            show_text(screen,"7 8 4 2 3", (592,354), color["green"],30,"font/cleanfont.ttf")
            show_text(screen, "Go to tutorial", (770,800),color["white"],30,"font/cleanfont.ttf")
            screen.blit(arrow_tutorial,(850,785))
            
            # when 'Go to tutorial' is hovered
            if hovered(pygame.Rect(700,775,180,40)):
                show_text(screen, "Go to tutorial", (770,800),color["green"],30,"font/cleanfont.ttf")
            
            # click go to tutorial
            if clicked(pygame.Rect(700,775,180,40)):
                tutorial_time_flag = False
                texts_tutorials = ["\n\n"," "]
                texts_tutorials_coordinates[0] = [-200,-200]
                texts_tutorials_coordinates[1] = [-200,-200]
                tutorial_answer = [" "," "]
                tutorial_flag = True
                description_flag = False
                play_sound("sound/click1.wav")
            show_text(screen, "Main menu", (screenwidth / 2, 890),color["white"], 50, "font/sketched.ttf")
            show_text(screen, "(Press 'm')", (screenwidth / 2, 930), color["white"], 15, "font/F25_bank_Printer.otf")
            if hovered(pygame.Rect(340, 850, 320, 100)):
                pygame.draw.rect(screen, color["green"], (340, 850, 320, 100), 3, 2)
            if clicked(pygame.Rect(340, 850, 320, 100)):
                play_sound("sound/click1.wav")
                game = 0
    
        if tutorial_flag == True:
            
            pygame.draw.rect(screen, color["white"], (500, 130, 370, 60), 2)
            pygame.draw.rect(screen, color["white"], (210 - 80 - 10, 250, 80, 80), 2, 2)
            pygame.draw.rect(screen, color["white"], (210, 250, 80, 80), 2, 2)
            pygame.draw.rect(screen, color["white"], (250 + 40 + 10, 250, 80, 80), 2, 2)
            pygame.draw.rect(screen, color["white"], (210 - 80 - 10, 340, 80, 80), 2, 2)
            pygame.draw.rect(screen, color["white"], (210, 340, 80, 80), 2, 2)
            pygame.draw.rect(screen, color["white"], (250 + 40 + 10, 340, 80, 80), 2, 2)
            pygame.draw.rect(screen, color["white"], (210 - 80 - 10, 430, 80, 80), 2, 2)
            pygame.draw.rect(screen, color["white"], (210, 430, 80, 80), 2, 2)
            pygame.draw.rect(screen, color["white"], (250 + 40 + 10, 430, 80, 80), 2, 2)
            multiline_text(screen, 30 ,texts_tutorials[0],color["white"], texts_tutorials_coordinates[0],1, "font/cleanfont.ttf")
            show_text(screen,texts_tutorials[1],texts_tutorials_coordinates[1],color["white"],30,"font/F25_bank_Printer.otf")
            
            if tutorial_time_flag == False:
                tutorial_time_flag = True
                tutorial_start_time = time.time()
                tutorial_next_flag = 0
            tutorial_current_time = time.time()

            if tutorial_next_flag == 0:
                
                if 1 < tutorial_current_time - tutorial_start_time :
                    texts_tutorials[0] = "\n\n\nThere are 9 different tiles on the left hand side."
                    texts_tutorials_coordinates[0] = [700, 280]
                
                if 2 < tutorial_current_time - tutorial_start_time < 2.2:
                    pygame.draw.rect(screen, color["white"], (210 - 80 - 10, 250, 80, 80), border_radius = 2)
                
                if 2.2 < tutorial_current_time - tutorial_start_time < 2.4:
                    pygame.draw.rect(screen, color["white"], (210, 250, 80, 80), border_radius = 2)
                
                if 2.4 < tutorial_current_time - tutorial_start_time < 2.6:
                    pygame.draw.rect(screen, color["white"], (250 + 40 + 10, 250, 80, 80), border_radius = 2)
                
                if 2.6 < tutorial_current_time - tutorial_start_time < 2.8:
                    pygame.draw.rect(screen, color["white"], (210 - 80 - 10, 340, 80, 80), border_radius = 2)
                
                if 2.8 < tutorial_current_time - tutorial_start_time < 3:
                    pygame.draw.rect(screen, color["white"], (210, 340, 80, 80), border_radius = 2)
                
                if 3 < tutorial_current_time - tutorial_start_time < 3.2:
                    pygame.draw.rect(screen, color["white"], (250 + 40 + 10, 340, 80, 80), border_radius = 2)
                
                if 3.2 < tutorial_current_time - tutorial_start_time < 3.4:
                    pygame.draw.rect(screen, color["white"], (210 - 80 - 10, 430, 80, 80), border_radius = 2)
                
                if 3.4 < tutorial_current_time - tutorial_start_time < 3.6:
                    pygame.draw.rect(screen, color["white"], (210, 430, 80, 80), border_radius = 2)
                
                if 3.6 < tutorial_current_time - tutorial_start_time < 3.8:
                    pygame.draw.rect(screen, color["white"], (250 + 40 + 10, 430, 80, 80), border_radius = 2)
                
                if 4.4 < tutorial_current_time - tutorial_start_time:
                    texts_tutorials[0] = "\n\nThere are 9 different tiles on the left hand side.\n\nClick the arrow below to proceed."
                
                if 4.4 < tutorial_current_time - tutorial_start_time and tutorial_next_flag == 0:
                    screen.blit(arrow_tutorial,(684,500))
                    
                    if clicked(pygame.Rect(684,500,32,32)):
                        play_sound("sound/click1.wav")
                        tutorial_next_flag = 1
                        tutorial_start_time = tutorial_current_time

            if tutorial_next_flag == 1:
                
                if 0 < tutorial_current_time - tutorial_start_time:
                    texts_tutorials[0] = "\nIn the previous description,\n\nwe talked about the sequence\n\nwhich consists of only numbers."
                
                screen.blit(arrow_tutorial,(684,500))
                
                if clicked(pygame.Rect(684,500,32,32)):
                    play_sound("sound/click1.wav")
                    tutorial_next_flag = 2
                    tutorial_start_time = tutorial_current_time
            
            if tutorial_next_flag == 2:
                
                if 0 < tutorial_current_time - tutorial_start_time :
                    texts_tutorials[0] = "\nBut also,\n\neach tile position makes up\n\na new sequence."
                
                screen.blit(arrow_tutorial,(684,500))
                
                if clicked(pygame.Rect(684,500,32,32)):
                    play_sound("sound/click1.wav")
                    tutorial_next_flag = 3
                    tutorial_start_time = tutorial_current_time
            
            if tutorial_next_flag == 3:
                
                if 0 < tutorial_current_time - tutorial_start_time < 2:
                    texts_tutorials[0] = "\nIn 3 seconds,\n\n3 different tiles will be illuminated\n\none after the other."
                
                screen.blit(arrow_tutorial,(684,500))
                
                if clicked(pygame.Rect(684,500,32,32)):
                    play_sound("sound/click1.wav")
                    tutorial_next_flag = 4
                    tutorial_start_time = tutorial_current_time
            
            if tutorial_next_flag == 4:
                
                if 0 < tutorial_current_time - tutorial_start_time < 1:
                    texts_tutorials[0] = "\n\n\n3"
                
                if 1 < tutorial_current_time - tutorial_start_time < 2:
                    texts_tutorials[0] = "\n\n\n2"
                
                if 2 < tutorial_current_time - tutorial_start_time < 3:
                    texts_tutorials[0] = "\n\n\n1"
                
                if 3 <tutorial_current_time - tutorial_start_time :
                    texts_tutorials[0] = "\n\n"
                
                if 3.5 < tutorial_current_time - tutorial_start_time < 4.1:
                    # position 6
                    pygame.draw.rect(screen, color["white"], (250 + 40 + 10, 340, 80, 80), border_radius =  2)

                if 4.2 < tutorial_current_time - tutorial_start_time < 4.8:
                    # position 1
                    pygame.draw.rect(screen, color["white"], (210 - 80 - 10, 250, 80, 80),  border_radius =  2)
                
                if 4.9 < tutorial_current_time - tutorial_start_time < 5.5:
                    # position 8
                    pygame.draw.rect(screen, color["white"], (210, 430, 80, 80), border_radius =  2)
                
                if 6 < tutorial_current_time - tutorial_start_time:
                    show_text(screen, "1",(250-80-10, 290),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "2",(250, 290),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "3",(250+80+10, 290),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "4",(250-80-10, 290+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "5",(250, 290+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "6",(250+80+10, 290+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "7",(250-80-10, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "8",(250, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "9",(250+80+10, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                
                if 7 < tutorial_current_time - tutorial_start_time:
                    texts_tutorials[0] = "\n\nEach tile is assigned a number\n\nWhat was the sequence of the tile positions?"
                    screen.blit(arrow_tutorial,(684,500))
                    if clicked(pygame.Rect(684,500,32,32)):
                        play_sound("sound/click1.wav")
                        tutorial_next_flag = 5
                        tutorial_start_time = tutorial_current_time
            
            if tutorial_next_flag == 5:
                
                if 0 < tutorial_current_time - tutorial_start_time:
                    show_text(screen, "1",(250-80-10, 290),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "2",(250, 290),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "3",(250+80+10, 290),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "4",(250-80-10, 290+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "5",(250, 290+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "6",(250+80+10, 290+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "7",(250-80-10, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "8",(250, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "9",(250+80+10, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    texts_tutorials[0] = "\n\nThe answer is\n\n6, 1, 8."
                
                screen.blit(arrow_tutorial,(684,500))
                
                if clicked(pygame.Rect(684,500,32,32)):
                    play_sound("sound/click1.wav")
                    tutorial_next_flag = 6
                    tutorial_start_time = tutorial_current_time
            
            if tutorial_next_flag == 6:
                
                if 0 < tutorial_current_time - tutorial_start_time:
                    show_text(screen, "1",(250-80-10, 290),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "2",(250, 290),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "3",(250+80+10, 290),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "4",(250-80-10, 290+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "5",(250, 290+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "6",(250+80+10, 290+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "7",(250-80-10, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "8",(250, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "9",(250+80+10, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    texts_tutorials[0] = "Sequence for tile positions : 6, 1, 8\n\nLet's say we are currently playing\n1 back game,\n\nthe tile position one event ago is 1."
                
                screen.blit(arrow_tutorial,(684,500))
                
                if clicked(pygame.Rect(684,500,32,32)):
                    play_sound("sound/click1.wav")
                    tutorial_next_flag = 7
                    tutorial_start_time = tutorial_current_time
            
            if tutorial_next_flag == 7:
                
                if 0 < tutorial_current_time - tutorial_start_time:
                    show_text(screen, "1",(250-80-10, 290),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "2",(250, 290),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "3",(250+80+10, 290),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "4",(250-80-10, 290+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "5",(250, 290+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "6",(250+80+10, 290+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "7",(250-80-10, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "8",(250, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "9",(250+80+10, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    texts_tutorials[0] = "Sequence for tile positions : 6, 1, 8\n\nOr let's say\nwe are playing 2 back game,\n\nthe tile position two events ago is 6."
                
                screen.blit(arrow_tutorial,(684,500))
                
                if clicked(pygame.Rect(684,500,32,32)):
                    play_sound("sound/click1.wav")
                    tutorial_next_flag = 8
                    tutorial_start_time = tutorial_current_time
            
            if tutorial_next_flag == 8:
                
                if 0 < tutorial_current_time - tutorial_start_time:
                    show_text(screen, "1",(250-80-10, 290),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "2",(250, 290),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "3",(250+80+10, 290),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "4",(250-80-10, 290+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "5",(250, 290+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "6",(250+80+10, 290+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "7",(250-80-10, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "8",(250, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen, "9",(250+80+10, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    texts_tutorials[0] = "Sequence for tile positions : 6, 1, 8\n\nIf we are playing 2 back game,\nthe answer for the tile position would be 'X',\n\nbecause the tile position two events ago (6) is different\nfrom the current tile position (8)."
                    
                    screen.blit(arrow_tutorial,(684,500))
                    
                    if clicked(pygame.Rect(684,500,32,32)):
                        play_sound("sound/click1.wav")
                        tutorial_next_flag = 9
                        tutorial_start_time = tutorial_current_time
            
            if tutorial_next_flag == 9:
                
                if 0 < tutorial_current_time - tutorial_start_time < 2:
                    texts_tutorials[0] = "\n\n\nNow let's play a simple game."
                
                if 2 < tutorial_current_time - tutorial_start_time :
                    texts_tutorials[0] = "It will be a 1 back game (N = 1).\n\nTry to remember the number and the tile position\none event ago.\n\nThe number and the tile position will appear\nfor 5 seconds each."
                    
                    screen.blit(arrow_tutorial,(684,500))
                    
                    if clicked(pygame.Rect(684,500,32,32)):
                        play_sound("sound/click1.wav")
                        tutorial_next_flag = 10
                        tutorial_start_time = tutorial_current_time
            
            if tutorial_next_flag == 10:
                
                if 0 < tutorial_current_time - tutorial_start_time < 1:
                    texts_tutorials[0] = "\n\n\n3"
                
                if 1 < tutorial_current_time - tutorial_start_time < 2:
                    texts_tutorials[0] = "\n\n\n2"
                
                if 2 < tutorial_current_time - tutorial_start_time < 3:
                    texts_tutorials[0] = "\n\n\n1"
                
                if 3 < tutorial_current_time - tutorial_start_time < 8:
                    # number 1, position 7
                    show_text(screen, "1",(250-80-10, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    pygame.draw.rect(screen, color["white"], (210 - 80 - 10, 430, 80, 80),5, border_radius = 2)
                    
                    screen.blit(arrow_tutorial,(684,500))
                    
                    if clicked(pygame.Rect(684,500,32,32)):
                        play_sound("sound/click1.wav")
                        texts_tutorials[0] = " "
                        tutorial_next_flag = 11
                        tutorial_start_time = tutorial_current_time
                
                if 3 < tutorial_current_time - tutorial_start_time < 4:    
                    texts_tutorials[0] = "Time left : 5 seconds"
                
                if 4 < tutorial_current_time - tutorial_start_time < 5:    
                    texts_tutorials[0] = "Time left : 4 seconds"
                
                if 5 < tutorial_current_time - tutorial_start_time < 6:    
                    texts_tutorials[0] = "Time left : 3 seconds"
                
                if 6 < tutorial_current_time - tutorial_start_time < 7:    
                    texts_tutorials[0] = "Time left : 2 seconds"
                
                if 7 < tutorial_current_time - tutorial_start_time < 8:    
                    texts_tutorials[0] = "Time left : 1 second"
                
                if 8 < tutorial_current_time - tutorial_start_time:
                    tutorial_next_flag = 11
                    tutorial_start_time = tutorial_current_time

            if tutorial_next_flag == 11:
                
                if 0 < tutorial_current_time - tutorial_start_time < 5:
                    # number 1, position 9
                    show_text(screen, "1",(250+80+10, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    pygame.draw.rect(screen, color["white"], (250 + 40 + 10, 430, 80, 80),5, border_radius = 2)
                
                if 0 < tutorial_current_time - tutorial_start_time < 1:    
                    texts_tutorials[0] = "Time left : 5 seconds"
                
                if 1 < tutorial_current_time - tutorial_start_time < 2:    
                    texts_tutorials[0] = "Time left : 4 seconds"
                
                if 2 < tutorial_current_time - tutorial_start_time < 3:    
                    texts_tutorials[0] = "Time left : 3 seconds"
                
                if 3 < tutorial_current_time - tutorial_start_time < 4:    
                    texts_tutorials[0] = "Time left : 2 seconds"
                
                if 4 < tutorial_current_time - tutorial_start_time < 5:    
                    texts_tutorials[0] = "Time left : 1 second"
                
                if 5 < tutorial_current_time - tutorial_start_time:
                    # number 1, position 9
                    show_text(screen, "1",(250+80+10, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                    pygame.draw.rect(screen, color["white"], (250 + 40 + 10, 430, 80, 80),5, border_radius = 2)
                    
                    texts_tutorials[0] = "Do you remember\n\nthe number and the tile position\n\none event ago?"
                    show_text(screen,"No",(700-50,470),color["white"],30,"font/F25_bank_Printer.otf")
                    show_text(screen,"Yes",(700+50,470),color["white"],30,"font/F25_bank_Printer.otf")
                    
                    if hovered(pygame.Rect(624,447,50,40)):
                        pygame.draw.rect(screen,color["white"],(624,447,50,40),width = 2,border_radius = 2)
                    
                    if hovered(pygame.Rect(716,447,66,40)):
                        pygame.draw.rect(screen,color["white"],(716,447,66,40),width = 2,border_radius = 2)
                    
                    # click no
                    if clicked(pygame.Rect(624,447,50,40)):
                        play_sound("sound/click1.wav")
                        tutorial_next_flag = 10
                        tutorial_start_time = tutorial_current_time
                    
                    # click yes
                    if clicked(pygame.Rect(716,447,66,40)):
                        play_sound("sound/click1.wav")
                        tutorial_next_flag = 12
                        tutorial_start_time = tutorial_current_time
            
            if tutorial_next_flag == 12:
                
                # number 1, position 9
                show_text(screen, "1",(250+80+10, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                pygame.draw.rect(screen, color["white"], (250 + 40 + 10, 430, 80, 80),5, border_radius = 2)

                texts_tutorials[0] = "If the current number is the same as\nthe number one event ago, click O under numbers.\n\nIf they are not the same, click X.\n\nSimilarly, if the current tile position is the same as\nthe tile position one event ago, click O under positions.\n\nIf they are not the same, click X."
                
                show_text(screen,"Numbers    Positions",(700,610),color["white"],30,"font/F25_bank_Printer.otf")
                show_text(screen,"Submit",(690,780),color["green"],25,"font/F25_bank_Printer.otf")
                screen.blit(img_o_numbers,img_o_numbers_rect)
                screen.blit(img_x_numbers,img_x_numbers_rect)
                screen.blit(img_o_positions,img_o_positions_rect)
                screen.blit(img_x_positions,img_x_positions_rect)
                
                if clicked(img_o_numbers_rect):
                    if tutorial_answer[0] == " ":
                        tutorial_answer[0] = "O"
                    elif tutorial_answer[0] == "O":
                        tutorial_answer[0] = " "
                    elif tutorial_answer[0] == "X":
                        tutorial_answer[0] = "O"
                    play_sound("sound/click1.wav")
                    
                if clicked(img_x_numbers_rect):
                    if tutorial_answer[0] == " ":
                        tutorial_answer[0] = "X"
                    elif tutorial_answer[0] == "X":
                        tutorial_answer[0] = " "
                    elif tutorial_answer[0] == "O":
                        tutorial_answer[0] = "X"
                    play_sound("sound/click1.wav")
                    
                if clicked(img_o_positions_rect):
                    if tutorial_answer[1] == " ":
                        tutorial_answer[1] = "O"
                    elif tutorial_answer[1] == "O":
                        tutorial_answer[1] = " "
                    elif tutorial_answer[1] == "X":
                        tutorial_answer[1] = "O"
                    play_sound("sound/click1.wav")
                    
                if clicked(img_x_positions_rect):
                    if tutorial_answer[1] == " ":
                        tutorial_answer[1] = "X"
                    elif tutorial_answer[1] == "X":
                        tutorial_answer[1] = " "
                    elif tutorial_answer[1] == "O":
                        tutorial_answer[1] = "X"
                    play_sound("sound/click1.wav")
                    
                if tutorial_answer[0] == "O":
                    pygame.draw.rect(screen,color["green"],(567-50-32-10,690-32-10,84,84),width = 3,border_radius = 2)
                if tutorial_answer[0] == "X":
                    pygame.draw.rect(screen,color["red"],(567+50-32-10,690-32-10,84,84),width = 3,border_radius = 2)

                if tutorial_answer[1] == "O":
                    pygame.draw.rect(screen,color["green"],(813-50-32-10,690-32-10,84,84),width = 3,border_radius = 2)
                if tutorial_answer[1] == "X":
                    pygame.draw.rect(screen,color["red"],(813+50-32-10,690-32-10,84,84),width = 3,border_radius = 2)

                # hover over submit button
                if hovered(pygame.Rect(633,760,112,38)):
                    pygame.draw.line(screen,color["green"],(633,760+40),(745,760+40),width= 2)
                
                # click submit button
                if clicked(pygame.Rect(633,760,112,38)):
                    play_sound("sound/click1.wav")
                    tutorial_next_flag = 13
                    tutorial_start_time = tutorial_current_time
            
            if tutorial_next_flag == 13:
                # number 1, position 9
                show_text(screen, "1",(250+80+10, 290+90+90),color["white"],30,"font/F25_bank_Printer.otf")
                pygame.draw.rect(screen, color["white"], (250 + 40 + 10, 430, 80, 80),5, border_radius = 2)

                # number 1, position 7
                show_text(screen, "1",(250-80-10, 290+90+90),color["grey"],30,"font/F25_bank_Printer.otf")
                pygame.draw.rect(screen, color["grey"], (210 - 80 - 10, 430, 80, 80),5, border_radius = 2)
                img_arrow = pygame.image.load("img/arrow.png")
                img_biggerarrow = pygame.image.load("img/uparrow.png")
                img_biggerarrow = pygame.transform.scale(img_biggerarrow,(180,180))
                screen.blit(img_arrow,(300,524))
                screen.blit(img_biggerarrow,(70,524))
                multiline_text(screen,23,"<The current Event>\nNumber : 1\nTile position : 9",color["white"],(300,620),1,"font/cleanfont.ttf")
                multiline_text(screen,23,"<The previous Event>\nNumber : 1\nTile position : 7",color["not too bright white"],(170,732),1,"font/cleanfont.ttf")
                
                # if tutorial answer is correct
                if tutorial_answer == ["O","X"]:
                    texts_tutorials[0] = "Correct answer!\nNumber : O\nPosition : X\n\n<Explanation>\nThe number one event ago is 1.\nThe current number is 1.\nThey are the same number, so the answer is O\n\nThe tile position one event ago is 7.\nThe current tile position is 9.\nThey are different tile positions, so the answer is X\n\n\nNow let's play the game!"

                # if tutorial answer is incorrect
                else:
                    texts_tutorials[0] = f"Wrong answer!\n\nYou chose...Number : {tutorial_answer[0]}, Position : {tutorial_answer[1]}\n\n<Explanation>\nThe number one event ago is 1.\nThe current number is 1.\nThey are the same number, so the answer is O\n\nThe tile position one event ago is 7.\nThe current tile position is 9.\nThey are different tile positions, so the answer is X"
                    show_text(screen,"Try again",(700,700),color["white"],30,"font/F25_bank_Printer.otf")
                    
                    # hover over try again
                    if hovered(pygame.Rect(600,670,200,60)):
                        pygame.draw.rect(screen,color["white"],(600,670,200,60),3,2)
                    
                    # click try again
                    if clicked(pygame.Rect(600,670,200,60)):
                        tutorial_answer = [" ", " "]
                        play_sound("sound/click1.wav")
                        tutorial_next_flag = 10
                        tutorial_start_time = tutorial_current_time
            
            # Main menu button
            show_text(screen, "Main menu", (screenwidth / 2, 890),color["white"], 50, "font/sketched.ttf")
            show_text(screen, "(Press 'm')", (screenwidth / 2, 930), color["white"], 15, "font/F25_bank_Printer.otf")
            if hovered(pygame.Rect(340, 850, 320, 100)):
                pygame.draw.rect(screen, color["green"], (340, 850, 320, 100), 3, 2)
            
            # click main menu 
            if clicked(pygame.Rect(340, 850, 320, 100)):
                tutorial_time_flag = False
                description_flag = True
                tutorial_flag = False
                tutorial_answer = [" "," "]
                texts_tutorials = ["\n\n"," "]
                texts_tutorials_coordinates[0] = [-2000,-2000]
                texts_tutorials_coordinates[1] = [-2000,-2000]
                play_sound("sound/click1.wav")
                game = 0

    # Key controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if game == 0:
                if event.key == pygame.K_RETURN:
                    main_menu_flag = True

                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    play_sound("sound/click1.wav")
                    sound_main_menu_intro_flag = True
                    main_menu_flag = True
                    game = 5

                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    play_sound("sound/click1.wav")
                    sound_main_menu_intro_flag = True
                    main_menu_flag = True
                    game = 4

                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    screenwidth = 1300
                    screen = pygame.display.set_mode((screenwidth, screenheight))
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    play_sound("sound/playbutton.wav")
                    regenerate_sequence()
                    game = 1
                
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    play_sound("sound/click1.wav")
                    sound_main_menu_intro_flag = True
                    main_menu_flag = True
                    game = 3

                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    run = False
            
            if game == 1 and event.key == pygame.K_p and game_pause_flag == False:
                sound_countdown_flag = False
                sound_start_flag = False
                game_pause_flag = True
            elif game == 1 and event.key == pygame.K_p and game_pause_flag == True:
                game_pause_flag = False
            
            if game == 1 and game_pause_flag == True and event.key == pygame.K_m:
                screenwidth = 1000
                screen = pygame.display.set_mode((screenwidth, screenheight))
                counter = 0
                questions_start = False
                score_flag = False
                button_save_result_flag = False
                start_count_game_screen = False
                game_pause_flag = False
                correct_number_of_questions_location = 0
                correct_number_of_questions_numbers = 0
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                reposition_imgs()
                lst_texts_in_game[0] = "Start!"
                button_position_O_rect.center = -200, -200
                button_position_X_rect.center = -200, -200
                button_numbers_O_rect.center = -200, -200
                button_numbers_X_rect.center = -200, -200
                button_key1_rect.center = -200, -200
                button_key2_rect.center = -200, -200
                button_key3_rect.center = -200, -200
                button_key4_rect.center = -200, -200
                main_menu_flag = True
                one_tenth_seconds = 0
                game = 0
            
            if game == 1 and event.key == pygame.K_s:
                screenwidth = 1000
                screen = pygame.display.set_mode((screenwidth, screenheight))
                sound_countdown_flag = False
                sound_start_flag = False
                game = 2
            
            if game == 5 and event.key == pygame.K_m:
                play_sound("sound/click1.wav")
                game = 0
                
                
    fps_clock.tick(fps)
    pygame.display.flip()
if os.path.isfile("level.txt"):
    if sys.platform == "win32":
        os.system("attrib +h level.txt")
    elif sys.platform == "darwin":
        os.system("chflags hidden level.txt")
    elif sys.platform.startswith("linux"):
        os.system("chattr +i level.txt")
sys.exit()
