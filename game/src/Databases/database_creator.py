import sqlite3

db = sqlite3.connect("characters.db")
db.isolation_level = None

db.execute("DROP TABLE Characters")
db.execute("CREATE TABLE Characters (name TEXT)")

db.execute("DROP TABLE StatValues")
db.execute("CREATE TABLE StatValues (level INT, character TEXT REFERENCES Characters (name), attack INT, defense INT, mdef INT, hp INT, mp INT)")

db.execute("DROP TABLE LearnSets")
db.execute("CREATE TABLE LearnSets (character TEXT REFERENCES Characters (name), level INT, skill TEXT REFERENCES Skills (name))")

db.execute("DROP TABLE Skills")
db.execute("CREATE TABLE Skills (name TEXT, desc TEXT, multiplier FLOAT, type TEXT, cost INT, aoe INT, buff INT, stat TEXT, recover INT, hp INT, mp INT, resurrect INT, duration INT)")




def activate():
    characters()
    skills()

def characters():

    add_character("Leon",
    [14, 18, 23, 29, 37, 48, 62, 80, 104, 135], #atk
    [12, 15, 19, 24, 31, 40, 52, 67, 87, 113], #def
    [10, 13, 16, 20, 26, 33, 42, 54, 70, 91], #mdef
    [140, 182, 236, 306, 400, 516, 670, 870, 1132, 1470], #hp
    [24, 28, 33, 39, 46, 55, 66, 79, 94, 112], #mp
    ["Power Strike","Fireball","Charge","Shockwave","Ray of Judgement","Deadly Strike"], #skills
    [1,2,3,5,8,10] #skill levels
    )

    add_character("Archer",
    [12, 15, 19, 24, 31, 40, 52, 67, 87, 113], #atk
    [6, 8, 10, 13, 17, 22, 29, 39, 52, 70], #def
    [7, 9, 12, 16, 21, 28, 37, 49, 66, 89], #mdef
    [110, 140, 180, 230, 290, 375, 480, 614, 785, 1004], #hp
    [16, 19, 22, 26, 31, 37, 44, 52, 62, 74], #mp
    ["Piercing Arrow","Fusillade","Magic Arrow","Charged Shot"], #skills
    [1,4,6,8] #skill levels
    )

    add_character("Wizard",
    [9, 12, 16, 22, 30, 41, 56, 77, 106, 146], #atk
    [4, 5, 7, 9, 12, 16, 22, 30, 42, 58], #def
    [12, 16, 21, 28, 37, 49, 66, 90, 120, 162], #mdef
    [90, 115, 144, 188, 240, 306, 392, 500, 640, 820], #hp
    [32, 40, 50, 62, 77, 96, 120, 150, 187, 234], #mp
    ["Fireball","Explosion","Thunderstrike","Meteor"], #skills
    [1,3,6,9]
    )

    add_character("Knight",
    [6, 8, 10, 13, 17, 23, 31, 42, 57, 78], #atk
    [16, 21, 27, 35, 46, 61, 81, 107, 142, 188],#def
    [4, 5, 6, 8, 11, 15, 20, 27, 37, 51], #mdef
    [240, 300, 395, 500, 640, 820, 1050, 1342, 1720, 2200], #hp
    [24, 30, 38, 48, 61, 78, 99, 126, 161, 206], #mp
    ["Shield Bash","Holy Light","Raise Defense","Resurrect","Raise Attack","Salvation"],
    [1,2,4,6,8,10]
    )

    add_character("Monk",
    [10, 13, 17, 22, 28, 36, 47, 61, 79, 100], #atk
    [10, 13, 17, 22, 28, 36, 47, 61, 79, 100],#def
    [10, 13, 17, 22, 28, 36, 47, 61, 79, 100], #mdef
    [100, 130, 170, 220, 280, 360, 470, 610, 790, 1000], #hp
    [10, 13, 17, 22, 28, 36, 47, 61, 79, 100], #mp
    ["Palm Strike","Share Energy","Meditate","Raise Magic Defense","Thousand Strikes"],
    [1,2,4,6,9]
    )

    add_character("Assassin",
    [16, 21, 27, 35, 46, 60, 79, 104, 137, 180], #atk
    [8, 10, 13, 16, 20, 26, 33, 42, 54, 70], #def
    [8, 10, 13, 16, 20, 26, 33, 42, 54, 70], #mdef
    [80, 104, 135, 175, 227, 295, 383, 497, 646, 840], #hp
    [18, 21, 25, 30, 36, 43, 52, 63, 76, 92], #mp
    ["Blade Slash","Poison","Backstab","Deadly Strike","Double Edge"], #skills
    [1,2,3,5,8,10] #skill levels
    )

    add_character("Demon Assassin",
    [16, 21, 27, 35, 46, 60, 79, 104, 137, 180], #atk
    [8, 10, 13, 16, 20, 26, 33, 42, 54, 70], #def
    [8, 10, 13, 16, 20, 26, 33, 42, 54, 70], #mdef
    [80, 104, 135, 175, 227, 295, 383, 497, 646, 840], #hp
    [18, 21, 25, 30, 36, 43, 52, 63, 76, 92], #mp
    ["Blade Slash","Poison","Backstab","Deadly Strike","Double Edge"], #skills
    [1,2,3,5,8,10] #skill levels
    )

    add_character("Warlock",
    [9, 12, 16, 22, 30, 41, 56, 77, 106, 146], #atk
    [4, 5, 7, 9, 12, 16, 22, 30, 42, 58], #def
    [12, 16, 21, 28, 37, 49, 66, 90, 120, 162], #mdef
    [90, 115, 144, 188, 240, 306, 392, 500, 640, 820], #hp
    [32, 40, 50, 62, 77, 96, 120, 150, 187, 234], #mp
    ["Fireball","Explosion","Thunderstrike","Meteor"], #skills
    [1,3,6,9]
    )

    add_character("Beholder",
    [9, 12, 16, 22, 30, 41, 56, 77, 106, 146], #atk
    [4, 5, 7, 9, 12, 16, 22, 30, 42, 58], #def
    [12, 16, 21, 28, 37, 49, 66, 90, 120, 162], #mdef
    [90, 115, 144, 188, 240, 306, 392, 500, 640, 820], #hp
    [32, 40, 50, 62, 77, 96, 120, 150, 187, 234], #mp
    ["Fireball","Explosion","Thunderstrike","Meteor"], #skills
    [1,3,6,9]
    )

    add_character("Goblin Soldier",
    [6, 8, 10, 13, 17, 23, 31, 42, 57, 78], #atk
    [16, 21, 27, 35, 46, 61, 81, 107, 142, 188],#def
    [4, 5, 6, 8, 11, 15, 20, 27, 37, 51], #mdef
    [240, 300, 395, 500, 640, 820, 1050, 1342, 1720, 2200], #hp
    [24, 30, 38, 48, 61, 78, 99, 126, 161, 206], #mp
    ["Shield Bash","Holy Light","Raise Defense","Resurrect","Raise Attack","Salvation"],
    [1,2,4,6,8,10]
    )

    add_character("Skeleton Warrior",
    [6, 8, 10, 13, 17, 23, 31, 42, 57, 78], #atk
    [16, 21, 27, 35, 46, 61, 81, 107, 142, 188],#def
    [4, 5, 6, 8, 11, 15, 20, 27, 37, 51], #mdef
    [240, 300, 395, 500, 640, 820, 1050, 1342, 1720, 2200], #hp
    [24, 30, 38, 48, 61, 78, 99, 126, 161, 206], #mp
    ["Shield Bash","Holy Light","Raise Defense","Resurrect","Raise Attack","Salvation"],
    [1,2,4,6,8,10]
    )

    add_character("Dragonling",
    [14, 18, 23, 29, 37, 48, 62, 80, 104, 135], #atk
    [12, 15, 19, 24, 31, 40, 52, 67, 87, 113], #def
    [10, 13, 16, 20, 26, 33, 42, 54, 70, 91], #mdef
    [140, 182, 236, 306, 400, 516, 670, 870, 1132, 1470], #hp
    [24, 28, 33, 39, 46, 55, 66, 79, 94, 112], #mp
    ["Power Strike","Fireball","Charge","Shockwave","Ray of Judgement","Deadly Strike"], #skills
    [1,2,3,5,8,10] #skill levels
    )

    add_character("Necromancer",
    [14, 18, 23, 29, 37, 48, 62, 80, 104, 235], #atk
    [12, 15, 19, 24, 31, 40, 52, 67, 87, 213], #def
    [10, 13, 16, 20, 26, 33, 42, 54, 70, 191], #mdef
    [140, 182, 236, 306, 400, 516, 670, 870, 1132, 14700], #hp
    [24, 28, 33, 39, 46, 55, 66, 79, 94, 1120], #mp
    ["Power Strike","Fireball","Charge","Shockwave","Ray of Judgement","Deadly Strike"], #skills
    [1,2,3,5,8,10] #skill levels
    )

def add_character(name :str,attack :list,defense :list,mdef :list,hp :list,mp :list,skills :list,skill_levels :list):
    db.execute("INSERT INTO Characters (name) VALUES (?)",[name])
    for i in range(10):
        db.execute("INSERT INTO StatValues (level, character, attack, defense,mdef,hp, mp) VALUES (?, ?, ?, ?, ?, ?,?)",[i+1,name,attack[i],defense[i],mdef[i],hp[i],mp[i]])
    counter = 0
    for skill in skills:
        db.execute("INSERT INTO LearnSets (character, level, skill) VALUES (?, ?, ?)",[name,skill_levels[counter],skill])
        counter += 1

def skills():

    add_skill("Power Strike","Strikes the enemy with great power dealing physical damage",
    1.25,"physical",4,0,0,"attack",0,0,0,0,0)

    add_skill("Charge","Charges power to deal over twice the damage next turn",
    1.5,"self",5,0,1,"attack",0,0,0,0,2)

    add_skill("Shockwave","Launch a shockwave dealing physical damage to all enemies",
    1.2,"physical",9,1,0,"attack",0,0,0,0,0)

    add_skill("Ray of Judgement","Call forth a ray of destruction from the sky dealing almighty damage to all enemies",
    1.5,"almighty",24,1,0,"attack",0,0,0,0,0)

    add_skill("Deadly Strike","Deal massive physical damage to an enemy",
    6,"physical",15,0,0,"attack",0,0,0,0,0)

    add_skill("Piercing Arrow","Shoot a piercing arrow into the enemy ignoring all defenses",
    1,"almighty",3,0,0,"attack",0,0,0,0,0)

    add_skill("Fusillade","Call a fusillade on the enemy dealing physical damage to all enemies",
    1.2,"physical",7,1,0,"attack",0,0,0,0,0)

    add_skill("Magic Arrow","Shoot an arrow infused with magic into the enemy dealing magic damage",
    2.5,"magic",8,0,0,"attack",0,0,0,0,0)

    add_skill("Charged Shot","Shoot a charged shot at the enemy dealing massive physical damage",
    5.5,"physical",15,0,0,"attack",0,0,0,0,0)

    add_skill("Fireball","Launch an fireball into the enemy dealing magic damage",
    1.25,"magic",5,0,0,"attack",0,0,0,0,0)

    add_skill("Explosion","Fire off an explosion dealing magic damage to all enemies",
    0.8,"magic",8,1,0,"attack",0,0,0,0,0)

    add_skill("Thunderstrike","Call forth thunder to strike at the enemy dealing high magic damage",
    2.5,"magic",12,0,0,"attack",0,0,0,0,0)

    add_skill("Meteor","Call forth a meteor to strike your foes dealing massive magic damage to all enemies",
    6,"magic",44,1,0,"attack",0,0,0,0,0)

    add_skill("Shield Bash","Bash the enemy with a shield dealing physical damage based on defense",
    1.25,"physical",5,0,0,"defense",0,0,0,0,0)

    add_skill("Holy Light","Pray for God to cure a party member healing them moderately",
    2.5,"support",3,0,0,"defense",1,1,0,0,0)

    add_skill("Raise Defense","Buff the party's defense for 3 turns",
    0.5,"support",12,1,1,"defense",0,0,0,0,3)

    add_skill("Resurrect","Pray to God to resurrect a party member bringing them back to the fight",
    0,"support",18,0,0,"none",0,0,0,1,0)

    add_skill("Raise Attack","Buff the party's attack for 3 turns",
    0.5,"support",12,1,1,"attack",0,0,0,0,3)

    add_skill("Salvation","Pray for God's light to heal the entire party",
    10,"support",30,1,0,"defense",1,1,0,0,0)

    add_skill("Palm Strike","Strike the foe with your palm dealing physical damage",
    1.4,"physical",5,0,0,"attack",0,0,0,0,0)

    add_skill("Share Energy","Share your energy with an ally giving them MP",
    0.5,"support",5,0,0,"mp",1,0,1,0,0)

    add_skill("Meditate","Meditate to recover your mp",
    0.5,"self",0,0,0,"mp",1,0,1,0,0)

    add_skill("Raise Magic Defense","Buff the party's magic defense for 3 turns",
    0.5,"support",12,1,1,"mdef",0,0,0,0,3)

    add_skill("Thousand Strikes","Strike the foe a thousand times in quick succession dealing massive physical damage",
    8,"physical",25,0,0,"attack",0,0,0,0,0)

    add_skill("Blade Slash","Slash the enemy with a blade dealing physical damage",
    1.6,"physical",6,0,0,"attack",0,0,0,0,0)

    add_skill("Poison","Poison the enemy for 3 turns dealing damage over time",
    5.5,"poison",4,0,0,"attack",0,0,0,0,3)

    add_skill("Backstab","Backstab the enemy dealing damage while ignoring their defense",
    2.5,"almighty",9,0,0,"attack",0,0,0,0,0)

    add_skill("Double Edge","Deal incredible damage to the enemy with the cost of recoil damage",
    9,"physical",24,0,0,"attack",0,1,0,0,0)


def add_skill(name :str,description :str,multiplier :float,damage_type :str,cost :int, aoe :int, buff :int, stat :str, recover :int, hp :int, mp :int, resurrect :int, duration :int):
    db.execute("INSERT INTO Skills (name, desc, multiplier, type, cost, aoe, buff, stat, recover, hp, mp, resurrect, duration) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",[name,description,multiplier,damage_type,cost,aoe,buff,stat,recover,hp,mp,resurrect,duration])


activate()
