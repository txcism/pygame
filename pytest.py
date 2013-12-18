# -*- coding: utf-8 -*-
import pygame
import math
import random
from pygame.locals import *
from sys import exit

#define color
black = [  0,  0,  0]
white = [255,255,255]
red   = [255,  0,  0]
green = [  0,255,  0]
blue  = [  0,  0,255]

#define screen size
size = [800,600]

bk_filename = 'E:\python_soft\pygame\wall86.jpg'

pygame.init()
screen = pygame.display.set_mode(size,0,32)
pygame.display.set_caption('my pygame :D')

bk_sf = pygame.image.load(bk_filename)
font   = pygame.font.SysFont('arial',40)
fps_sf = font.render('0',True,(0,0,255))
clock = pygame.time.Clock()

time_sec = 0

#define block
class Block():
    def __init__(self,wh,pos,vel,col):
        self.wh  = wh       #width&height
        self.pos = pos      #position
        self.vel = vel      #velocity
        self.col = col      #colour

#initialize blocks 
b_col  = [255,255,255]
b_vel  = [random.random()-random.random(),-random.random()]
blocks = [Block([4,4],[400,400],b_vel,b_col) for i in range(1000)]

#define gravity acceleration
block_acc = [0,0.001]

###########################################################################################################
#main loop
###########################################################################################################
while True:
    
    screen.fill(white)

    #delta frame time
    time_delta = clock.tick()

    #handle keybord&mounse event
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
            
    #game logic
    print(blocks[0].pos[1])
    for block in blocks:
        if block.pos[1] <= size[1]:
            
            #update velocity
            block.vel[0] += block_acc[0]*time_delta
            block.vel[1] += block_acc[1]*time_delta

            #update position
            block.pos[0] += block.vel[0]*time_delta
            block.pos[1] += block.vel[1]*time_delta
        else:
            block.pos = [400,400]
            block.vel = [random.random()-random.random(),-random.random()]
            block.col = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

                
    #game render
    for block in blocks:
        pygame.draw.rect(screen,block.col,[block.pos[0],block.pos[1],block.wh[0],block.wh[1]])


    #get&render fps
    fps = clock.get_fps()
    fps_sf = font.render('fps:'+str(fps),True,(0,0,255))
    screen.blit(fps_sf,(0,0))

    
    #refresh screen
    pygame.display.update()

        
