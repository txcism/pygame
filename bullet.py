# -*- coding: utf-8 -*-


from constants import *
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, width, height, owner):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = owner.rect.x
        self.rect.y = owner.rect.y
        self.owner = owner
        self.dir = 0
        self.vel = [1,0]                   #speed of player
        #根据玩家的朝向来决定子弹的飞行方向
        if owner.face_right:
            self.dir =  1
        else:
            self.dir = -1

    def update(self):
        self.rect.x += self.vel[0]*self.dir*self.owner.world.dt



