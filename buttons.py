import pygame

class Buttons:
    color = {"black" : (0, 0, 0), "white" : (255, 255, 255), "green" : (0, 255, 0),
             "grey" : (175,173,169), "red" : (255,0,0), "light green" : (144,238, 144),
             "sky blue" : (50,130,230), "light red" : (255,127,127), "light green" : (144,238,144),
             "blue" : (0,0,255), "purple" : (201,71,245), "dark grey" : (120,120,120)
            }

    def __init__(self, x, y, width, height, rect_color = color["dark grey"], alpha = 255):
        # set rectangular size and its coordinates
 
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surface_rect = self.surface.get_rect()
        self.surface_rect.center = x, y
        self.surface_width = width
        self.surface_height = height
        self.surface.fill(rect_color)
        self.surface.set_alpha(alpha)

        
        
        self.font = pygame.font.Font("cleanfont.ttf", 50)
        self.content = self.font.render("",True, (255,255,255))
        self.content_rect = self.content.get_rect(center = (self.surface_width/2, self.surface_height/2))
        
        self.hovered_flag = False
        self.clicked_flag = False

    def draw_text(self, text, fontname = "cleanfont.ttf", fontsize = 50, fontcolor = color["white"]):
        self.font = pygame.font.Font(fontname,fontsize)
        self.content = self.font.render(text, True, fontcolor)
    
    def update_text(self, text):
        self.content = self.font.render(text, True, (255,255,255))
    
    def draw_rectangle(self, screen):
        self.surface.blit(self.content, self.content_rect)
        screen.blit(self.surface, self.surface_rect)

    # def draw_rect(self, screen, text = "test", draw_text_in_rectangle = False, fontname = "cleanfont.ttf", fontsize = 30, textcolor = color["white"]):
    #     if draw_text_in_rectangle == True:
    #         font = pygame.font.Font(fontname, fontsize)
    #         self.content = font.render(text, True, textcolor)
    #         self.content_rect = self.content.get_rect()
    #         self.content_rect.center = self.surface_width/2, self.surface_height/2
    #         self.surface.blit(self.content, self.content_rect)
    #         screen.blit(self.surface, self.surface_rect)
    #     else:
    #         screen.blit(self.surface, self.surface_rect)
        
    def hovered(self, mouse_shape = False):
        active = False
        if self.surface_rect.collidepoint(pygame.mouse.get_pos()) and self.hovered_flag == False:
            active = True
            self.hovered_flag = True
            if mouse_shape == True:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        elif self.surface_rect.collidepoint(pygame.mouse.get_pos()) == False and self.hovered_flag == True:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.hovered_flag = False
        return active

    def hovered_contiuously(self):
        if self.surface_rect.collidepoint(pygame.mouse.get_pos()):
            return True
        else:
            return False


    def clicked(self):
        if self.surface_rect.collidepoint(pygame.mouse.get_pos()):
            if self.clicked_flag == False and pygame.mouse.get_pressed()[0]:
                self.clicked_flag = True
                return True
            elif self.clicked_flag == True and pygame.mouse.get_pressed()[0] == False:
                self.clicked_flag = False
