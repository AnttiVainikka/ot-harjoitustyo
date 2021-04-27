from random import randint
from Classes import character
import sqlite3

db = sqlite3.connect("src/Databases/characters.db")
db.isolation_level = None

class Skill():

    def __init__(self,name):
        self.name = name
        self.desc = db.execute("SELECT desc FROM Skills WHERE name = ?",[name]).fetchone()[0]
        self.multiplier = db.execute("SELECT multiplier FROM Skills WHERE name = ?",[name]).fetchone()[0]
        self.type = db.execute("SELECT type FROM Skills WHERE name = ?",[name]).fetchone()[0]
        self.cost = db.execute("SELECT cost FROM Skills WHERE name = ?",[name]).fetchone()[0]
        self.aoe = db.execute("SELECT aoe FROM Skills WHERE name = ?",[name]).fetchone()[0]
        self.buff = db.execute("SELECT buff FROM Skills WHERE name = ?",[name]).fetchone()[0]
        self.stat = db.execute("SELECT stat FROM Skills WHERE name = ?",[name]).fetchone()[0]
        self.recover = db.execute("SELECT recover FROM Skills WHERE name = ?",[name]).fetchone()[0]
        self.hp = db.execute("SELECT hp FROM Skills WHERE name = ?",[name]).fetchone()[0]
        self.mp = db.execute("SELECT mp FROM Skills WHERE name = ?",[name]).fetchone()[0]
        self.resurrect = db.execute("SELECT resurrect FROM Skills WHERE name = ?",[name]).fetchone()[0]
        self.duration = db.execute("SELECT duration FROM Skills WHERE name = ?",[name]).fetchone()[0]
        self.user = ""
    
    def activate(self,character,target):
        if self.type == "physical" or self.type == "magic" or self.type == "almighty":
            character.attack(target,self)
        if self.buff == 1:
            if self.stat == "attack":
                original_attack = db.execute("SELECT attack FROM StatValues WHERE level = ? AND character = ?",[target.level[0],target.name]).fetchone()[0]
                target.atk += original_attack * self.multiplier
            if self.stat == "defense":
                original_defense = db.execute("SELECT defense FROM StatValues WHERE level = ? AND character = ?",[target.level[0],target.name]).fetchone()[0]
                target.df += original_defense * self.multiplier
            if self.stat == "mdef":
                original_mdef = db.execute("SELECT mdef FROM StatValues WHERE level = ? AND character = ?",[target.level[0],target.name]).fetchone()[0]
                target.mdef += original_mdef * self.multiplier
        if self.type == "poison":
            if not target.boss:
                target.status = ["Poison",3]
        if self.recover == 1:
            if self.hp == 1:
                if self.stat == "attack":
                    amount = character.atk * self.multiplier
                if self.stat == "defense":
                    amount = character.df * self.multiplier
                target.recover(int(amount),"hp")
            if self.mp == 1:
                if self.stat == "attack":
                    amount = character.atk * self.multiplier
                if self.stat == "defense":
                    amount = character.df * self.multiplier
                if self.stat == "mdef":
                    amount = character.mdef * self.multiplier
                if self.stat == "hp":
                    amount = character.hp * self.multiplier
                if self.stat == "mp":
                    amount = character.mp * self.multiplier
                target.recover(int(amount),"mp")
        if self.resurrect == 1:
            target.alive = True
            target.recover(target.taken_dmg,"hp")
    
    def deactivate(self,party,monster):
        for character in party:
            if self.aoe != 1:
                if character.name == self.user:
                    if self.stat == "attack":
                        original_attack = db.execute("SELECT attack FROM StatValues WHERE level = ? AND character = ?",[character.level[0],character.name]).fetchone()[0]
                        character.atk -=  original_attack * self.multiplier
                    if self.stat == "defense":
                        original_defense = db.execute("SELECT defense FROM StatValues WHERE level = ? AND character = ?",[character.level[0],character.name]).fetchone()[0]
                        character.df -=  original_defense * self.multiplier
                    if self.stat == "mdef":
                        original_mdef = db.execute("SELECT mdef FROM StatValues WHERE level = ? AND character = ?",[character.level[0],character.name]).fetchone()[0]
                        character.mdef -=  original_mdef * self.multiplier
            else:
                if self.stat == "attack":
                    original_attack = db.execute("SELECT attack FROM StatValues WHERE level = ? AND character = ?",[character.level[0],character.name]).fetchone()[0]
                    character.atk -=  original_attack * self.multiplier
                if self.stat == "defense":
                    original_defense = db.execute("SELECT defense FROM StatValues WHERE level = ? AND character = ?",[character.level[0],character.name]).fetchone()[0]
                    character.df -=  original_defense * self.multiplier
                if self.stat == "mdef":
                    original_mdef = db.execute("SELECT mdef FROM StatValues WHERE level = ? AND character = ?",[character.level[0],character.name]).fetchone()[0]
                    character.mdef -=  original_mdef * self.multiplier
        self.duration = db.execute("SELECT duration FROM Skills WHERE name = ?",[self.name]).fetchone()[0]
