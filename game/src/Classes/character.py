import sqlite3
import pygame
# pylint: disable=no-member
pygame.init()
from Classes.skills import Skill

db = sqlite3.connect("src/Databases/characters.db")
db.isolation_level = None

class Character():
    """The class for characters, monsters, and bosses. Searches their info from a database based on their name."""
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
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.direction = 2
        self.boss = False
        self.x = pygame.image.load("src/Sprites/background_full.png").get_width() / 2
        self.y = pygame.image.load("src/Sprites/background_full.png").get_height() / 2
        self.monster = False

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
        """Gives the character exp and levels them up if they gain enough."""
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
        """Gives the character the stat values corresponding with their level."""
        self.reset_health()
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
        if skill != None and skill not in self.skills:
            self.skills.append(Skill(skill[0]))
        

    def take_dmg(self,damage):
        """Makes the character take damage and kills them if the damage is fatal."""
        if damage >= self.hp:
            self.taken_dmg += self.hp
            self.hp = 0
            self.alive = False
        else:
            self.hp -= damage
            self.taken_dmg += damage


    def recover(self,amount,stat):
        """Recovers a set amount of the selected value."""
        if self.alive:
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
        """Resets the characters health and mana"""
        self.alive = True
        self.hp += self.taken_dmg
        self.mp += self.used_mp
        self.taken_dmg = 0
        self.used_mp = 0
        self.status = ["none",0]


    def attack(self,target,skill):
        """Makes the character attack the target."""
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
        """Adds the character to the party and sets them at level 1"""
        party.append(self)
        self.level_up(1)








