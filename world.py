from constants import *
from level import Level
from player import Player
from camera import Camera
import pygame
import random

class World():
    def __init__(self):
        #screen for render
        self.screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()
        self.dt = 0.0
        #init player
        self.player = Player(RED, 20, 32, self)
        self.player.rect.y = 300
        #init camera for render
        self.camera = Camera(self.player)
        #level number
        self.cur_num = 0
        #color to fill screen
        self.background_color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

        #list ro store level
        self.level_list = []

        #group for collide and render
        self.platfrom_group = pygame.sprite.Group()
        self.monster_group = pygame.sprite.Group()
        self.background_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

        #make the first level
        level = self.make_level(0, 550)
        self.level_list.append(level)
    # update for all!!!
    def update(self):
        #get the ms per frame
        self.dt = self.clock.tick()
        #empty group
        self.bullet_group.empty()
        self.monster_group.empty()
        self.background_group.empty()

        for level in self.level_list:
            #update level and the monsters
            level.update()
            #need to transfer player
            if level.victory == False and len(level.monster_group) == 0:
                print('transform!!!')
                level.victory = True
                self.transfer()
                self.cur_num += 1
                self.background_color = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
            #
            self.monster_group.add(level.monster_group)
            self.background_group.add(level.background_group)
        #need to make new level ?
        if self.cur_num  >= self.level_list[-1].number:
            level = self.make_level(self.level_list[-1].x + random.randint(0,200) - 100, self.level_list[-1].y - 400)
            level.number = self.cur_num + 1
            self.level_list.append(level)
        #player update
        self.player.update()
        self.bullet_group.add(self.player.bullet_group)
        #handle collide
        self.handle_collide()

    #render for all!!!
    def render(self):
        self.camera.update()
        self.camera.update()
        self.render_layer(self.background_group)
        self.render_layer(self.platfrom_group)
        self.render_layer(self.monster_group)
        self.render_layer(self.bullet_group)
        self.render_layer(self.player_group)

    def render_layer(self, sprite_group):
        for s in sprite_group:
            self.screen.blit(s.image, [s.rect.x + self.camera.offset[0], s.rect.y + self.camera.offset[1]])

    #transfer player when player win
    def transfer(self):
        self.player.rect.x = random.randrange(self.level_list[-1].platform.rect.left, self.level_list[-1].platform.rect.right)
        self.player.rect.y = self.level_list[-1].platform.rect.top - self.player.rect.h - 2

    #make a new level
    def make_level(self, x, y):
        level = Level(x, y, self)
        #count level from 0 NOT 1
        level.number = len(self.level_list)
        #group for render & collide
        self.platfrom_group.add(level.platform)
        print('level maked!!!')
        return level

    #handle some sprite collide
    def handle_collide(self):
        #collide between monster and bullet
        for monster in self.monster_group:
            hit_list = pygame.sprite.spritecollide(monster, self.bullet_group, True)
            for bullet in hit_list:
                self.monster_group.remove(monster)
                self.level_list[self.cur_num].monster_group.remove(monster)
                print('hit')

        #collide between monster and player
        hit_list = pygame.sprite.spritecollide(self.player, self.monster_group, False)
        for sprite in hit_list:
            if sprite.vel[0] > 0:
                sprite.rect.right = self.player.rect.left
            if sprite.vel[0] < 0:
                sprite.rect.left = self.player.rect.right
            sprite.vel[0] = -sprite.vel[0]
            self.player.health -= 10