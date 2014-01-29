from constants import *
import pygame
import random

class Monster(pygame.sprite.Sprite):
    def __init__(self, color, width, height, level):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.vel = [0.9,0.9]                   #speed of player
        self.face_right = True
        self.hp = 100
        self.level = level
        self.focus = self.level.world.player
    def upadte(self):
        self.wander()
        #if (self.rect.x - self.focus.rect.x)**2 + (self.rect.y - self.focus.rect.y)**2 > 300**2:
        #    self.wander(dt)
        #else:
        #    self.attack(dt)
        #if self.rect.x > self.focus.rect.x:
        #    self.rect.x -= 0.5*dt
        #else:
        #    self.rect.x += 0.5*dt
        #if self.rect.y > self.focus.rect.y:
        #    self.rect.y -= 0.5*dt
        #else:
        #    self.rect.y += 0.5*dt


    def wander(self):
        self.rect.x += self.vel[0]*self.level.world.dt
        if self.rect.left < self.level.platform.rect.left :
            self.rect.left = self.level.platform.rect.left
            self.vel[0] = -1*self.vel[0]
        if self.rect.right > self.level.platform.rect.right:
            self.rect.right = self.level.platform.rect.right
            self.vel[0] = -1*self.vel[0]

    def attack(self):
        if self.rect.x > self.focus.rect.x:
            self.rect.x -= 0.5*self.level.world.dt
            if self.rect.x < self.focus.rect.x:
                self.rect.x = self.focus.rect.x
        else:
            self.rect.x += 0.5*self.level.world.dt
            if self.rect.x > self.focus.rect.x:
                self.rect.x = self.focus.rect.x


