# -*- coding: utf-8 -*-
from world import World
from constants import *
import pygame
######################################################################################
# Initialize Pygame
######################################################################################
pygame.init()
#Loop until the user clicks the close button.
game_quit = False
#set font to render
font   = pygame.font.SysFont('宋体',40)
fps_sf = font.render('0',True,BLUE)
#init the world
world = World()
#####################################################################################
# -------- Main Program Loop -----------
#####################################################################################
while game_quit == False:
    #clear screen
    world.screen.fill(world.background_color)
    #handle input
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            game_quit = True           # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            #move right
            if event.key == pygame.K_RIGHT:
                world.player.move_right()
            #move left
            if event.key == pygame.K_LEFT:
                world.player.move_left()
            #jump
            if event.key == pygame.K_UP:
                world.player.jump()
            #fire
            if event.key == pygame.K_SPACE:
                world.player.fire()
        if event.type == pygame.KEYUP:
            #stop
            if event.key in (pygame.K_RIGHT, pygame.K_LEFT):
                world.player.stop()
    #update and render
    world.update()
    world.render()
    #render some info
    fps = world.clock.get_fps()
    fps_sf = font.render(u'fps:' + str(fps), True,(100, 0, 100))
    world.screen.blit(fps_sf,(0,0))
    health_info = font.render(u'生命值：'+ str(world.player.health), True, (0, 100, 100))
    world.screen.blit(health_info,(0,50))
    level_info = font.render(u'关卡：' + str(world.cur_num), True, (100, 100, 0))
    world.screen.blit(level_info, (0, 100))
    #flip all to screen
    pygame.display.flip()
pygame.quit()





