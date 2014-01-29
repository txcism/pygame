from constants import *
import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, world):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.vel = [0,0]                   #speed of player
        self.face_right = True
        self.health = 100
        #group to hold bullets that fired by player
        self.bullet_group = pygame.sprite.Group()
        #world that hold player
        self.world = world
        #acc of the player's vel
        self.acc = 0.005
    def move_right(self):
        self.vel[0] = 0.8
        self.face_right = True
    def move_left(self):
        self.vel[0] = -0.8
        self.face_right = False
    def stop(self):
        self.vel[0] = 0
    def jump(self):
        self.rect.y += 2
        hit_list = pygame.sprite.spritecollide(self, self.world.platfrom_group, False)
        self.rect.y -= 2
        for sprite in hit_list:
            self.vel[1] = -1.5
    def fire(self):
        bullet = Bullet(RED, 20, 5, self)
        self.bullet_group.add(bullet)
    def update(self):
        ##############################################################################
        #handle collide, very important!!!!!!!!!
        ##############################################################################
        #first test the left and right
        self.rect.x += self.vel[0]*self.world.dt
        hit_list = pygame.sprite.spritecollide(self, self.world.platfrom_group, False)
        for sprite in hit_list:
            if self.vel[0] > 0:
                self.rect.right = sprite.rect.left
            if self.vel[0] < 0:
                self.rect.left = sprite.rect.right
        #then test the up and down
        self.vel[1] += self.acc * self.world.dt                        #gravity effect
        self.rect.y += self.vel[1]*self.world.dt
        hit_list = pygame.sprite.spritecollide(self, self.world.platfrom_group, False)
        for sprite in hit_list:
            if self.vel[1] > 0:
                self.rect.bottom = sprite.rect.top
            if self.vel[1] < 0:
                self.rect.top = sprite.rect.bottom
            self.vel[1] = 0
        ###############################################################################

        #update bullets
        for bullet in self.bullet_group:
            bullet.update()
            if bullet.rect.x < -1000 or bullet.rect.x > 20000:
                self.bullet_group.remove(bullet)




