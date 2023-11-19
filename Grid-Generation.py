import pygame, sys
from pygame.locals import QUIT
import random
pygame.init()

WINDOW = pygame.display.set_mode((1300, 1100))
pygame.display.set_caption('Grid Modulo Art for Discrete Math (this took me 8 hours please give me extra credit)')

U_W, U_H = 50, 50

R = (255, 0, 0)
B = (0, 0, 255)
G = (0, 255, 0)

unit0 = pygame.image.load("unit1.png")
unit1 = pygame.image.load("unit2.png")
unit2 = pygame.image.load("unit3.png")
unit3 = pygame.image.load("unit4.png")
unit4 = pygame.image.load("unit5.png")
unit5 = pygame.image.load("unit6.png")
unit6 = pygame.image.load("unit7.png")
unit7 = pygame.image.load("unit8.png")
unit8 = pygame.image.load("unit9.png")
unit9 = pygame.image.load("unit10.png")



base_font = pygame.font.Font(None, 32)
font = pygame.font.SysFont('Arial', 25)
base_text = 'Mod: '
user_text = '1'

input_x, input_y = WINDOW.get_width()/2 - 110, 950
  
input_rect = pygame.Rect(input_x, input_y, 100, 32)
active = False

submit = pygame.Rect(input_x+input_rect.w, input_y-3, 120, 38)

mode = pygame.Rect(input_x - 170, input_y - 3, 170, 38)
mode_text = 'Addition'

color_active = (0, 204, 255)

color_passive = (0, 100, 255)
color = color_passive
color2 = (255, 80, 80)
color3 = (102, 255, 102)

def draw_window(color, user_text, color2, mode_text, color3):
    pygame.draw.rect(WINDOW, color, input_rect)
    pygame.draw.rect(WINDOW, color2, submit)
    pygame.draw.rect(WINDOW, color3, mode)    

    text_surface = base_font.render(base_text + user_text, True, (255, 255, 255))
    button_text_surface = base_font.render('Generate', True, (255, 255, 255))
    mode_text = base_font.render(mode_text, True, (255, 255, 255))

    credit = font.render("Made by Faris Dababneh for Mr. Snow (Please give me extra credit)", True, (255,255, 255))

    WINDOW.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    WINDOW.blit(button_text_surface, (submit.x+10, submit.y+8))
    WINDOW.blit(mode_text, (mode.x + 5, mode.y + 8))

    WINDOW.blit(credit, (10, 1070))

    pygame.display.flip()

def match_unit(num, x, y, key_list):
    
    match num:
        case 0:
            WINDOW.blit(key_list[0], (x,y))
        case 1:
            WINDOW.blit(key_list[1], (x, y))
        case 2:
            WINDOW.blit(key_list[2], (x, y))
        case 3:
            WINDOW.blit(key_list[3], (x, y))
        case 4:
            WINDOW.blit(key_list[4], (x, y))
        case 5:
            WINDOW.blit(key_list[5], (x, y))
        case 6:
            WINDOW.blit(key_list[6], (x, y))
        case 7:
            WINDOW.blit(key_list[7], (x, y))
        case 8:
            WINDOW.blit(key_list[8], (x, y))
        case 9:
            WINDOW.blit(key_list[9], (x, y))    
        
             
def draw_grid(user_text, mode_text):
    # Get the mod desired by user
    mod = int(user_text)

    if mod > 9 or mod < 1:
        WINDOW.fill((0, 0, 0))
        error = pygame.Rect(WINDOW.get_width()/2 - 200, WINDOW.get_height()/2 - 50, 300, 50)
        pygame.draw.rect(WINDOW, R, error)
        error_text = base_font.render('ENTER VALID MOD (1-9)', True, (255, 255, 255))
        WINDOW.blit(error_text, (error.x + 5, error.y + 15))
        pygame.display.update()
    else:
        WINDOW.fill((0, 0, 0))
        
        unit_list = [unit0, unit1, unit2, unit3, unit4, unit5, unit6, unit7, unit8, unit9]
        key_list = []
        
        matrix = []

        for i in range (10):
            current = random.choice(unit_list)
            key_list.append(current)
            unit_list.remove(current)

        temp = []
        for j in range(mod):
            temp.append(j+1)
        matrix.insert(0, temp)
        
        for j in range (mod-1):
            temp = []
            temp.append(j+2)
            for z in range(mod-1):
                if mode_text == "Multiplication":
                    temp.append(((matrix[0][z+1]) * (j+2)) % 9)
                else:    
                    temp.append(((matrix[0][z+1] + (j+2))) % 9)
            matrix.insert(j+1, temp)


        rows, cols = (mod, mod)
        x = 0
        y = 0
        
        for i in range (rows):
            x = 0
            for j in range(cols):
                match_unit(matrix[i][j], x, y, key_list)
                x += 50
            y += 50    

        for i in range(mod):
            num = base_font.render(str(i), True, (255, 255, 255))
            WINDOW.blit(num, (1050, 10 + (i*100)))
            match_unit(matrix[0][i], 1070, 10 + (i*100), key_list)


        rect = pygame.Rect(0, 0, mod*50 + 1, mod*50 + 1)
        sub = WINDOW.subsurface(rect)
        pygame.image.save(sub, "temp.jpg")
        quarter2 = pygame.transform.rotate(pygame.image.load("temp.jpg"), 270) 
        WINDOW.blit(quarter2, (mod*50, 0))

        rect2 = pygame.Rect(0, 0, mod*50 * 2 + 1, mod*50 + 1)
        sub2 = WINDOW.subsurface(rect2)
        pygame.image.save(sub2, "temp.jpg")
        half2 = pygame.transform.rotate(pygame.image.load("temp.jpg"), 180) 
        WINDOW.blit(half2, (0, mod*50))


        # SAVES GRID
        final = pygame.Rect(0, 0, mod*50 * 2 + 1, mod*50 * 2 + 1)
        final_sub = WINDOW.subsurface(final)
        pygame.image.save(final_sub, "final-grid.jpg")

        key = pygame.Rect(1049, 9, 90, 10+(mod*100))
        key_sub = WINDOW.subsurface(key)
        pygame.image.save(key_sub, "final-key.jpg")


        
        pygame.display.update()
    

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            if input_rect.collidepoint(event.pos):
                active = True
            elif submit.collidepoint(event.pos):
                color2 = (255, 0, 0)
            elif mode.collidepoint(event.pos):
                color3 = G    
            else:
                active = False    
                color2 = (255, 80, 80)
                color3 = (102, 255, 102)
        # Checking for user typing        
        if event.type == pygame.KEYDOWN:
            # Checking for user deleting input
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            # Inputting user characters
            else:
                if len(user_text) < 2:
                    user_text += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mode.collidepoint(event.pos):
                if mode_text == "Addition":
                    mode_text = "Multiplication"
                    draw_grid(user_text, mode_text)
                else:
                    mode_text = "Addition"
                    draw_grid(user_text, mode_text)
            if submit.collidepoint(event.pos):
                draw_grid(user_text, mode_text)        
        
        
    if active:
        color = color_passive
    else:
        color = color_active

    draw_window(color, user_text, color2, mode_text, color3)