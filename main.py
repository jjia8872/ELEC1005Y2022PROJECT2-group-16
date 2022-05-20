# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:22:20 2018

@author: zou
"""

import pygame
import time
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_ESCAPE
from pygame.locals import QUIT

from game import Game

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

green = pygame.Color(0, 200, 0)
bright_green = pygame.Color(0, 255, 0)
red = pygame.Color(200, 0, 0)
bright_red = pygame.Color(255, 0, 0)
blue = pygame.Color(32, 178, 170)
bright_blue = pygame.Color(32, 200, 200)
yellow = pygame.Color(255, 205, 0)
bright_yellow = pygame.Color(255, 255, 0)
dark = pygame.Color(128, 128, 128)
game = Game()
rect_len = game.settings.rect_len
snake = game.snake
pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((game.settings.width * 15, game.settings.height * 15))
pygame.display.set_caption('Gluttonous')

crash_sound = pygame.mixer.Sound('./sound/crash.wav')



def text_objects(text, font, color=black):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_display(text, x, y, color=black):
    large_text = pygame.font.SysFont('comicsansms', 50)
    text_surf, text_rect = text_objects(text, large_text, color)
    text_rect.center = (x, y)
    screen.blit(text_surf, text_rect)
    pygame.display.update()

def display_text(text, x, y, color=black):
    small_text = pygame.font.SysFont('comicsansms', 15)
    text_surf, text_rect = text_objects(text, small_text, color)
    text_rect.center = (x,y)
    screen.blit(text_surf, text_rect)
    pygame.display.update()

def button(msg, x, y, w, h, inactive_color, active_color, action=None, parameter=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            if parameter != None:
                action(parameter)
            else:
                action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h))

    smallText = pygame.font.SysFont('comicsansms', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = (x + (w / 2), y + (h / 2))
    screen.blit(TextSurf, TextRect)

def level_button(msg, x, y, w, h, inactive_color, active_color, action=None, parameter =None,parameter_two = None,parameter_three = None,parameter_four = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            if parameter != None and parameter_two != None and parameter_three != None and parameter_four != None:
                action(parameter,parameter_two,parameter_three)
                initial_interface(parameter_three,parameter_four)
            elif parameter != None and parameter_two != None:
                action(parameter,parameter_two)
            elif parameter != None:
                action(parameter,parameter_three)
            else:
                action()


    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h))
        
    smallText = pygame.font.SysFont('comicsansms', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = (x + (w / 2), y + (h / 2))
    screen.blit(TextSurf, TextRect)
    

def quitgame():
    pygame.quit()
    quit()


def crash(text_color):
    pygame.mixer.Sound.play(crash_sound)
    message_display('crashed', game.settings.width / 2 * 15, game.settings.height / 3 * 15, text_color)
    time.sleep(1)
    
def initial_interface(color = white, music = True):
    pygame.init()
    pygame.display.set_caption('Gluttonous')
    intro = True
    bg1= pygame.image.load('./images/main1.png')
    bg2= pygame.image.load('./images/main_2.png')
    moveL = pygame.image.load('./images/moveL.png')
    moveR = pygame.image.load('./images/moveR.png')
    x = 0
    y = 450
    track = pygame.mixer.music.load('./sound/main.wav')
    pygame.mixer.music.play()
    if music == False:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
        
    if color == white:
        text_color = black
        move1 = pygame.image.load('./images/snake.jpeg')
    else:
        text_color = white
        

        
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(color)
        screen.blit(pygame.transform.scale(bg1,(550,550)),(100,50))
        screen.blit(pygame.transform.scale(bg2,(550,550)),(-200,50))
        if x >450:
            x = 0
        if y <0:
            y = 450
        z = y - 200
        n = x +200
        if z < 0:
            z+=450
        if n>450:
            n -=450
        screen.blit(pygame.transform.scale(moveL,(70,70)),(y,130))
        screen.blit(pygame.transform.scale(moveL,(70,70)),(z,130))
        screen.blit(pygame.transform.scale(moveR,(70,70)),(x,30))
        screen.blit(pygame.transform.scale(moveR,(70,70)),(n,30))
        x+=10
        y-=10
        message_display('Gluttonous', game.settings.width / 2 * 15, game.settings.height / 4 * 15,text_color)
        level_button('Go!', 175, 200, 80, 40, green, bright_green, level_screen,color,music)
        button('Quit', 175, 300, 80, 40, red, bright_red, quitgame)
        level_button('Help?',0,0,80,40,blue,bright_blue,help_screen,color,music)
        level_button('Setting',370,0,80,40,green,bright_green,setting_screen,color,music)
        
        pygame.display.update()
        pygame.time.Clock().tick(15)
        
def setting_screen(color = white,music = True):
    pygame.display.set_caption('Setting')
    if color == white:
        text_color = black
    else:
        text_color = white
    intro = True
    if music == False:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(color)
        
        message_display('Setting', game.settings.width / 2 * 15, game.settings.height / 4 * 15,text_color)
        display_text('The colours of the game(Dark mode/Light mode)',220,170,text_color)
        level_button('Dark',280,210,80,40,green, bright_green,setting_screen,black,music)
        level_button('Light',350,210,80,40,green, bright_green,setting_screen,white,music)
        level_button('return',175, 350, 80, 40, red, bright_red,initial_interface,color,music)

        display_text('Background music',220,260,text_color)
        level_button('On',280,300,80,40,green, bright_green,setting_screen,color,True)
        level_button('Off',350,300,80,40,green, bright_green,setting_screen,color,False)
        
        pygame.display.update()
        pygame.time.Clock().tick(15)
        
def level_screen(color = white,music = True):
    pygame.display.set_caption('Level')
    if color == white:
        text_color = black
    else:
        text_color = white
    intro = True
    message_display('Gluttonous', game.settings.width / 2 * 15, game.settings.height / 4 * 15,text_color)
    display_text('Please select the difficulty of the game',220,170,text_color)
    display_text('(Default game difficulty is easy)',220,190,text_color)
    screen.fill(color)
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        message_display('Gluttonous', game.settings.width / 2 * 15, game.settings.height / 4 * 15,text_color)
        display_text('Please select the difficulty of the game',220,170,text_color)
        display_text('(Default game difficulty is easy)',220,190,text_color)
        screen.fill(color)
        level_button('Easy',80,240,80,40,green, bright_green,game_loop,'human',5,color,music)
        level_button('Medium',175,240,80,40,green, bright_green,game_loop,'human',15,color,music)
        level_button('Difficult',270,240,80,40,green, bright_green,game_loop,'human',30,color,music)
        level_button('return',175, 350, 80, 40, red, bright_red,initial_interface,color,music)
        pygame.display.update()
        pygame.time.Clock().tick(15)
        

    
def help_screen(color = white,music = True):
    if color == white:
        text_color = black
    else:
        text_color = white
    #help_screen = pygame.display.set_mode((game.settings.width * 15, game.settings.height * 15))
    pygame.display.set_caption('HELP')
    while True:
        #fpsClock = pygame.time.Clock()
        #pygame.display.init
        #help_screen.fill(white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill(color)
        message_display('Help', game.settings.width / 2 * 15, game.settings.height / 4 * 15,text_color)
        display_text('Use the arrow keys on the keyboard up, down, left',220,170,text_color)
        display_text('and right to control the direction of the snake, looking',220,190,text_color)
        display_text('for something to eat, each bite will get a certain number',220,210,text_color)
        display_text("of points, and the snake's body will eat longer and longer,",220,230,text_color)
        display_text("the longer the body to play the more difficult,can not touch",220,250,text_color)
        display_text("the wall, can not bite their own body, more can not bite their",220,270,text_color)
        display_text("own body, more can not bite their own tail. The only goal of",220,290,text_color)
        display_text("the snake is to grow into the longest snake!",220,310,text_color)
        level_button('return',175, 350, 80, 40, red, bright_red,initial_interface,color,music)
        button('Quit', 270, 350, 80, 40, red, bright_red, quitgame)
        
        pygame.display.update()
        pygame.time.Clock().tick(15)
    


def game_loop(player, fps,color = white):
    
    game.restart_game()
    
    
    if color == white:
        text_color = black
        bgcolor = dark
        bg= pygame.image.load('./images/day.png')
    else:
        text_color = white
        bgcolor = dark
        bg= pygame.image.load('./images/night.png')
    while not game.game_end():

        pygame.event.pump()

        move = human_move()
        

        game.do_move(move)

        screen.fill(bgcolor)
        screen.blit(pygame.transform.scale(bg,(450,450)),(0,0))
        game.snake.blit(rect_len, screen)
        game.strawberry.blit(screen)
        game.blit_score(text_color, screen)

        pygame.display.flip()

        fpsClock.tick(fps)

    crash(text_color)


def human_move():
    direction = snake.facing

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                direction = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                direction = 'left'
            if event.key == K_UP or event.key == ord('w'):
                direction = 'up'
            if event.key == K_DOWN or event.key == ord('s'):
                direction = 'down'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    move = game.direction_to_int(direction)
    return move


if __name__ == "__main__":
    initial_interface()

