# -*- coding: utf-8 -*-
from constants import *
from block import Block
import pygame

class Camera():
    def __init__(self, target):
        self.target = target
        self.offset = [0,0]

    def update(self):
        #获得目标位置，设置偏离量,偏移后的位置减去实际位置
        self.offset = [int(SCREEN_WIDTH /2) - self.target.rect.x, int(SCREEN_HEIGHT/2) - self.target.rect.y]
    #
    #def draw_layer(self, sprite_list):
    #    for s in sprite_list:
    #        self.screen.blit(s.image, [s.rect.x + self.offset[0], s.rect.y + self.offset[1]])
    #
    #def draw(self, background, platform, player, bullet, monster):
    #    self.draw_layer(background)
    #    self.draw_layer(platform)
    #    self.draw_layer(player)
    #    self.draw_layer(monster)
    #    self.draw_layer(bullet)
