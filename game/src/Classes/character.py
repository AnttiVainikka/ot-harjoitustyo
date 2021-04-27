import sqlite3
import pygame
# pylint: disable=no-member
pygame.init()
from Classes.skills import Skill


db = sqlite3.connect("src/Databases/characters.db")
db.isolation_level = None

screen_width = pygame.image.load("src/Sprites/background_full.png").get_width()
screen_height = pygame.image.load("src/Sprites/background_full.png").get_height()
wall = pygame.image.load("src/Sprites/wall_length.png").get_height()
door_wide = pygame.image.load("src/Sprites/wide_length_door.png").get_width()
door_tall = pygame.image.load("src/Sprites/tall_length_door.png").get_height()

class Character():

    def __init__(self, name :str, sprite, over_sprite):

        self.name = name
        self.sprite = sprite
        self.atk = 0
        self.df = 0
        self.mdef = 0
        self.hp = 0
        self.mp = 0
        self.skills = []
        self.level = [1,0,100]
        self.alive = True
        self.taken_dmg = 0
        self.used_mp = 0
        self.status = ["none",0]
        self.items = []


        self.over_sprite = over_sprite
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.speed_x = 1
        self.speed_y = 1
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.direction = 2
        self.boss = False

    def move_right(self):
        self.right = True
    def stop_right(self):
        self.right = False

    def move_left(self):
        self.left = True
    def stop_left(self):
        self.left = False

    def move_up(self):
        self.up = True
    def stop_up(self):
        self.up = False

    def move_down(self):
        self.down = True
    def stop_down(self):
        self.down = False


    def give_exp(self,exp :int):
        if self.level[0] < 10:
            self.level[1] += exp
            while True:
                if self.level[1] >= self.level[2]:
                    if self.level[0] < 10:
                        self.level[0] += 1
                    else:
                        break
                    self.level_up(self.level[0])
                    self.level[1] = self.level[1]-self.level[2]
                    self.level[2] += 50
                    self.taken_dmg = 0
                else:
                    break


    def level_up(self,level):
        self.taken_dmg = 0
        self.used_mp = 0
        self.atk = db.execute("SELECT attack FROM StatValues WHERE level = ? AND character = ?",
        [level,self.name]).fetchone()[0]
        self.df = db.execute("SELECT defense FROM StatValues WHERE level = ? AND character = ?",
        [level,self.name]).fetchone()[0]
        self.mdef = db.execute("SELECT mdef FROM StatValues WHERE level = ? AND character = ?",
        [level,self.name]).fetchone()[0]
        self.hp = db.execute("SELECT hp FROM StatValues WHERE level = ? AND character = ?",
        [level,self.name]).fetchone()[0]
        self.mp = db.execute("SELECT mp FROM StatValues WHERE level = ? AND character = ?",
        [level,self.name]).fetchone()[0]
        skill = db.execute("SELECT skill FROM LearnSets WHERE level = ? AND character = ?",
        [level,self.name]).fetchone()
        if skill != None:
            self.skills.append(Skill(skill[0]))
        

    def take_dmg(self,damage):
        if damage >= self.hp:
            self.taken_dmg += self.hp
            self.hp = 0
            self.alive = False
        else:
            self.hp -= damage
            self.taken_dmg += damage


    def recover(self,amount,stat):
        if stat == "hp":
            if amount > self.taken_dmg:
                amount = self.taken_dmg
            self.hp += amount
            self.taken_dmg -= amount

        if stat == "mp":
            if amount > self.used_mp:
                amount = self.used_mp
            self.mp += amount
            self.used_mp -= amount


    def reset_health(self):
        self.hp += self.taken_dmg
        self.mp += self.used_mp
        self.taken_dmg = 0
        self.used_mp = 0
        self.status = ["none",0]


    def attack(self,target,skill):
        if skill == 0:
            damage = self.atk - target.df/3
        else:
            if skill.type == "physical":
                damage = self.atk * skill.multiplier - target.df/3
            if skill.type == "magic":
                damage = self.atk * skill.multiplier - target.mdef/3  
            if skill.type == "almighty":
                damage = self.atk * skill.multiplier 
            if skill.hp == 1 and skill.recover == 0:
                self.take_dmg(int(damage/3))
        if damage <= 0:
            damage = 1
        target.take_dmg(int(damage))


    def choose_character(self,party):
        party.append(self)
        self.level_up(1)
        self.x


    def change_speed(self,cordinate):
        if cordinate == "x":
            self.speed_x = -self.speed_x
        if cordinate == "y":
            self.speed_y = -self.speed_y







