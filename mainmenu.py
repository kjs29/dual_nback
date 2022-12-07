# import pygame, time
# from buttons import Buttons

# # color
# color = {"black" : (0, 0, 0), "white" : (255, 255, 255), "green" : (0, 255, 0),
#          "grey" : (175, 173, 169), "red" : (255, 0, 0), "light green" : (144, 238, 144),
#          "sky blue" : (50, 130, 230), "light red" : (255, 127, 127), "light green" : (144, 238, 144),
#          "blue" : (0, 0, 255), "purple" : (201, 71, 245), "dark grey" : (120, 120, 120),
#          "yellow" : (255, 255, 0), "dark green" : (9, 46, 32), "dark dark grey" : (25, 25, 25),
#          "pastel green" : (193, 225, 193), "orange" : (255, 165, 0)
#         }
# start_count = time.time()
# screenwidth = 1000
# screenheight = 1000
# screen = pygame.display.set_mode((screenwidth, screenheight))
# screen.fill(color["black"])
# texts_mainmenu = ["N back", "How\nto\nplay", "Exit", "Game\nsettings", "Score\nboard" ]


# first = []
# second = []
# third = []

# for n in range(3):
#     first.append(pygame.Rect((30 + n * 300 + n * 20, 30, 300, 300)))
#     second.append(pygame.Rect((30 + n * 300 + n * 20, 350, 300, 300)))
#     third.append(pygame.Rect((30 + n * 300 + n * 20, 670, 300, 300)))

# tile_location = first + second + third

# current_nback = 2
# button1 = Buttons(30 + 150, 30 + 150, 300, 300, color["black"],alpha = 255)
# button2 = Buttons(350 + 150, 30 + 150, 300, 300, color["black"],alpha = 255)
# button3 = Buttons(670 + 150, 30 + 150, 300, 300, color["black"],alpha = 255)
# button4 = Buttons(30 + 150, 350 + 150, 300, 300, color["black"],alpha = 255)
# button5 = Buttons(350 + 150, 350 + 150, 300, 300, color["black"],alpha = 255)
# button6 = Buttons(670 + 150, 350 + 150, 300, 300, color["black"],alpha = 255)
# button7 = Buttons(30 + 150, 670 + 150, 300, 300, color["black"],alpha = 255)
# button8 = Buttons(350 + 150, 670 + 150, 300, 300, color["black"],alpha = 255)
# button9 = Buttons(670 + 150, 670 + 150, 300, 300, color["black"],alpha = 255)
# buttonlist = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

# def multiline_text(screen,size,text,color,coor,linespace = 10):
    
#     text_list = text.splitlines()
#     for i,e in enumerate(text_list):
#         font = pygame.font.Font("sketched.ttf",size)
#         message_content = font.render(e,True,color)
#         message_content_rect = message_content.get_rect()
#         message_content_rect.center = coor[0], coor[1] + size*i + (i*linespace)
#         screen.blit(message_content,message_content_rect)

# def show_text(screen,text,coor,color,size):
#     font = pygame.font.Font("sketched.ttf",size)
#     content = font.render(text,True,color)
#     content_rect = content.get_rect()
#     content_rect.center = coor[0],coor[1]
#     screen.blit(content,content_rect)
    
# clickedflag = False
# def clicked(rect):
#     global clickedflag
#     if rect.collidepoint(pygame.mouse.get_pos()):
#         if clickedflag == False and pygame.mouse.get_pressed()[0]:
#             clickedflag = True
#             return True
#         elif clickedflag == True and pygame.mouse.get_pressed()[0] == False:
#             clickedflag = False

# def a():    
#     screenwidth = 1000
#     screenheight = 1000
#     screen = pygame.display.set_mode((screenwidth, screenheight))
#     screen.fill(color["black"])
#     mouse_point = pygame.mouse.get_pos()
#     #print(mouse_point)
#     current_count = time.time()
#     if 1 < current_count - start_count < 1.3:
#         pygame.draw.rect(screen, color["red"], first[0], border_radius = 5)
#     if 1.2 < current_count - start_count < 1.5:
#         pygame.draw.rect(screen, color["orange"], first[1], border_radius = 5)
#     if 1.4 < current_count - start_count < 1.7:
#         pygame.draw.rect(screen, color["yellow"], first[2], border_radius = 5)
#     if 1.6 < current_count - start_count < 1.9:
#         pygame.draw.rect(screen, color["green"], second[0], border_radius = 5)
#     if 1.8 < current_count - start_count < 2.1:
#         pygame.draw.rect(screen, color["light green"], second[1], border_radius = 5)        
#     if 2 < current_count - start_count < 2.3:
#         pygame.draw.rect(screen, color["sky blue"], second[2], border_radius = 5)
#     if 2.2 < current_count - start_count < 2.5:
#         pygame.draw.rect(screen, color["blue"], third[0], border_radius = 5)
#     if 2.4 < current_count - start_count < 2.7:
#         pygame.draw.rect(screen, color["purple"], third[1], border_radius = 5)        
#     if 2.6 < current_count - start_count < 2.9:
#         pygame.draw.rect(screen, color["dark grey"], third[2], border_radius = 5)
#     if 3 < current_count - start_count < 3.2:
#         for n in range(3):
#             pygame.draw.rect(screen, color["white"], first[n], border_radius = 5)
#             pygame.draw.rect(screen, color["white"], third[n], border_radius = 5)
#         pygame.draw.rect(screen, color["white"], second[0], border_radius = 5)
#         pygame.draw.rect(screen, color["white"], second[2], border_radius = 5)
#         show_text(screen, texts_mainmenu[0],(350 + 150, 350 + 150, 300), color["white"],74)
#     if current_count - start_count < 3.2:
#         for n in range(3):
#             pygame.draw.rect(screen, color["black"], first[n], width = 3, border_radius = 5)
#             pygame.draw.rect(screen, color["black"], second[n], width = 3, border_radius = 5)
#             pygame.draw.rect(screen, color["black"], third[n], width = 3, border_radius = 5)
#     else:
#         for i in range(len(tile_location)):
#             if tile_location[i].collidepoint(mouse_point):
#                 pygame.draw.rect(screen, color["green"], tile_location[i], width = 10, border_radius= 10)
#             else:
#                 pygame.draw.rect(screen, color["white"], tile_location[i], width = 3, border_radius = 5)
        
#         # for index,a in enumerate(buttonlist):
#         #     a.hovered(mouse_shape = True)
#         for n in range(9):
#             if buttonlist[n].clicked():
#                 if n == 0:
#                     print("How to play clicked")
#                 elif n == 2:
#                     print("Scoreboard clicked")
#                 elif n == 4:
#                     game = 1
#                     screenheight = 1200
#                     screen = pygame.display.set_mode((screenwidth, screenheight))
#                     pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
#                     print(f"current_nback : {current_nback}")
#                 elif n == 6:
#                     print("Game settings clicked")
#                 elif n == 8: 
#                     run = False
#         # if buttonlist[4].clicked():
#         #     game = 1
#         #     screenheight = 1200
#         #     screen = pygame.display.set_mode((screenwidth, screenheight))
#         #     pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
#         # if buttonlist[8].clicked():
#         #     run = False
#         if tile_location[4].collidepoint(mouse_point) == False:
#             texts_mainmenu[0] = "N back"
#         else:
#             texts_mainmenu[0] = "Play"
#         multiline_text(screen, 70, texts_mainmenu[1], color["yellow"],(30 + 150, 20 + 80),1)
#         multiline_text(screen, 68, texts_mainmenu[3], color["green"],(30 + 150, 670 + 110),1)
#         multiline_text(screen, 70, texts_mainmenu[4],color["sky blue"],(670 + 150, 140))
#         show_text(screen, texts_mainmenu[0],(350 + 150, 350 + 150, 300), color["white"],74)
#         show_text(screen, texts_mainmenu[2],(670 + 150, 670 + 150), color["red"],90)

