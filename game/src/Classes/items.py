from Classes import character
import sqlite3

db = sqlite3.connect("src/Databases/characters.db")
db.isolation_level = None

class Item():
    """The class for items. Searches its info from a database based on its name."""
    def __init__(self,name,amount):
        self.name = name
        self.desc = db.execute("SELECT desc FROM Items WHERE name = ?",
        [name]).fetchone()[0]
        self.multiplier = db.execute("SELECT multiplier FROM Items WHERE name = ?",
        [name]).fetchone()[0]
        self.aoe = db.execute("SELECT aoe FROM Items WHERE name = ?",
        [name]).fetchone()[0]
        self.hp = db.execute("SELECT hp FROM Items WHERE name = ?",
        [name]).fetchone()[0]
        self.mp = db.execute("SELECT mp FROM Items WHERE name = ?",
        [name]).fetchone()[0]
        self.resurrect = db.execute("SELECT resurrect FROM Items WHERE name = ?",
        [name]).fetchone()[0]
        self.amount = amount

    def use(self,target):
        """Uses the item on the given target. Return True if it succeeds and False if something is wrong."""
        if self.resurrect == 1:
            if target.alive is True:
                return False
            target.alive = True
            target.recover(target.taken_dmg//2,"hp")
            return True
        if target.alive is False:
            return False
        if self.hp == 1:
            if target.taken_dmg == 0:
                if self.mp == 0:
                    return False
            else:
                amount = (target.hp + target.taken_dmg) * self.multiplier
                target.recover(int(amount),"hp")
        if self.mp == 1:
            if target.used_mp == 0:
                return False
            amount = (target.mp + target.used_mp) * self.multiplier
            target.recover(int(amount),"mp")

        return True

