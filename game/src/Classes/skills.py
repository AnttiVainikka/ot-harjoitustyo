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
        if self.type != "support":
            character.attack(target,self)
        if self.buff == 1:
            if self.stat == "attack":
                original_attack = db.execute("SELECT attack FROM StatValues WHERE level = ? AND character = ?",[target.level[0],target.name]).fetchone()[0]
                target.atk += original_attack * self.multiplier
            if self.stat == "defense":
                original_defense = db.execute("SELECT defense FROM StatValues WHERE level = ? AND character = ?",[target.level[0],target.name]).fetchone()[0]
                target.df += original_defense * self.multiplier
    
    def deactivate(self,party,monster):
        for character in party:
            if self.aoe == 0:
                if character.name == self.user:
                    if self.stat == "attack":
                        original_attack = db.execute("SELECT attack FROM StatValues WHERE level = ? AND character = ?",[character.level[0],character.name]).fetchone()[0]
                        character.atk -=  original_attack * self.multiplier
                    if self.stat == "defense":
                        original_defense = db.execute("SELECT defense FROM StatValues WHERE level = ? AND character = ?",[character.level[0],character.name]).fetchone()[0]
                        character.df -=  original_defense * self.multiplier      
            else:
                if self.stat == "attack":
                    original_attack = db.execute("SELECT attack FROM StatValues WHERE level = ? AND character = ?",[character.level[0],character.name]).fetchone()[0]
                    character.atk -=  original_attack * self.multiplier
                if self.stat == "defense":
                    original_defense = db.execute("SELECT defense FROM StatValues WHERE level = ? AND character = ?",[character.level[0],character.name]).fetchone()[0]
                    character.df -=  original_defense * self.multiplier  
        self.duration = db.execute("SELECT duration FROM Skills WHERE name = ?",[self.name]).fetchone()[0]