from monster import Monster
from constants import *
from block import Block
import pygame
import random
#from platform import Platform

class Level():
    def __init__(self, x, y, world):
        self.number = 0
        self.victory = False
        self.platform = []
        self.monster_group = pygame.sprite.Group()
        self.world = world
        self.background_group = pygame.sprite.Group()
        #level position
        self.x = x
        self.y = y

        self.make_platform()
        self.make_monsters()
        self.make_background()

    def make_platform(self):
        self.platform = Block([random.randint(0,255),random.randint(0,255),random.randint(0,255)], 2000, 10)
        self.platform.rect.x = self.x
        self.platform.rect.y = self.y

    def make_monsters(self):
        #make 2 monster
        for i in range(2):
            monster = Monster(BLUE, 20, 80, self)
            monster.rect.x = self.x + random.randint(0,self.platform.rect.right - 20)
            monster.rect.y = self.y - monster.rect.h
            monster.level = self
            self.monster_group.add(monster)

    def make_background(self):
        for x in range(self.platform.rect.left, self.platform.rect.right, 40):
            background = Block([random.randint(0,255),random.randint(0,255),random.randint(0,255)], 40, random.randint(200,300))
            background.rect.x = x
            background.rect.y = random.randrange(self.platform.rect.y - background.rect.h, self.platform.rect.y + background.rect.h)
            background.image.set_alpha(random.randint(50,150))
            self.background_group.add(background)

    def update(self):
        for monster in self.monster_group:
            monster.upadte()

