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
    [14,22,34,48,62,78,94,112,136,155], #atk
    [7,13,18,26,34,44,62,74,84,96], #def
    [5,9,14,22,30,38,52,62,74,82], #mdef
    [120,180,240,450,640,820,940,1120,1360,1540], #hp
    [24,32,44,55,64,72,88,98,112,124], #mp
    ["Power Strike","Fireball","Charge","Shockwave","Ray of Judgement","Deadly Strike"], #skills
    [1,2,3,5,8,10] #skill levels
    )

    add_character("Archer",
    [9,14,18,24,36,52,72,88,102,144], #atk
    [5,9,14,22,30,38,52,62,74,82], #def
    [5,9,14,22,30,38,52,62,74,82], #mdef
    [80,120,200,350,490,600,720,910,1080,1320], #hp
    [16,19,24,28,36,45,52,62,69,82], #mp
    ["Piercing Arrow","Fusillade","Charged Shot"], #skills
    [1,4,7] #skill levels
    )

    add_character("Wizard",
    [12,18,26,40,55,66,78,92,104,124], #atk
    [4,8,12,18,25,32,40,48,55,68], #def
    [9,12,18,24,32,42,55,72,88,112], #mdef
    [80,120,200,350,490,600,720,910,1080,1320], #hp
    [32,48,66,84,97,124,144,180,215,240], #mp
    ["Fireball","Explosion","Thunderstrike","Meteor"], #skills
    [1,3,6,9]
    )

    add_character("Knight",
    [3,5,8,14,19,26,42,58,70,88], #atk
    [18,25,33,50,72,94,118,142,180,240],#def
    [4,8,12,18,25,32,40,48,55,68], #mdef
    [240,320,500,680,840,1020,1300,1580,1880,2400], #hp
    [24,32,44,64,78,92,102,116,132,150], #mp
    ["Shield Bash","Holy Light","Raise Defense","Resurrect","Raise Attack","Salvation"],
    [1,2,4,6,8,10]
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
    1.5,"physical",4,0,0,"attack",0,0,0,0,0)

    add_skill("Charge","Charges power to deal over twice the damage next turn",
    1.5,"support",5,0,1,"attack",0,0,0,0,2)

    add_skill("Shockwave","Launch a shockwave dealing physical damage to all enemies",
    1.2,"physical",9,1,0,"attack",0,0,0,0,0)

    add_skill("Ray of Judgement","Call forth a ray of destruction from the sky dealing almighty damage to all enemies",
    1.5,"almighty",24,1,0,"attack",0,0,0,0,0)

    add_skill("Deadly Strike","Deal massive physical damage to an enemy",
    7.5,"physical",15,0,0,"attack",0,0,0,0,0)

    add_skill("Piercing Arrow","Shoot a piercing arrow into the enemy ignoring all defenses",
    1,"almighty",3,0,0,"attack",0,0,0,0,0)

    add_skill("Fusillade","Call a fusillade on the enemy dealing physical damage to all enemies",
    1.2,"physical",7,1,0,"attack",0,0,0,0,0)

    add_skill("Charged Shot","Shoot a charged shot at the enemy dealing massive physical damage",
    7.5,"physical",15,0,0,"attack",0,0,0,0,0)

    add_skill("Fireball","Launch an fireball into the enemy dealing magic damage",
    1.5,"magic",5,0,0,"attack",0,0,0,0,0)

    add_skill("Explosion","Fire off an explosion dealing magic damage to all enemies",
    0.8,"magic",8,1,0,"attack",0,0,0,0,0)

    add_skill("Thunderstrike","Call forth thunder to strike at the enemy dealing high magic damage",
    3.5,"magic",12,0,0,"attack",0,0,0,0,0)

    add_skill("Meteor","Call forth a meteor to strike your foes dealing massive magic damage to all enemies",
    8,"magic",44,1,0,"attack",0,0,0,0,0)

    add_skill("Shield Bash","Bash the enemy with a shield dealing physical damage based on defense",
    8,"physical",5,0,0,"defense",0,0,0,0,0)

    add_skill("Holy Light","Pray for God to cure a party member healing them moderately",
    2.5,"support",3,0,1,"defense",1,1,0,0,0)

    add_skill("Raise Defense","Buff the party's defense for 3 turns",
    0.5,"support",12,1,1,"defense",0,0,0,0,3)

    add_skill("Resurrect","Pray to God to resurrect a party member bringing them back to the fight",
    0,"support",18,0,0,"none",0,0,0,1,0)

    add_skill("Raise Attack","Buff the party's attack for 3 turns",
    0.5,"support",12,1,1,"attack",0,0,0,0,3)

    add_skill("Salvation","Pray for God's light to heal the entire party",
    10,"support",30,1,1,"defense",1,1,0,0,0)




def add_skill(name :str,description :str,multiplier :float,damage_type :str,cost :int, aoe :int, buff :int, stat :str, recover :int, hp :int, mp :int, resurrect :int, duration :int):
    db.execute("INSERT INTO Skills (name, desc, multiplier, type, cost, aoe, buff, stat, recover, hp, mp, resurrect, duration) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",[name,description,multiplier,damage_type,cost,aoe,buff,stat,recover,hp,mp,resurrect,duration])


activate()
