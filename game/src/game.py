import pygame
from random import randint
#import sqlite3

#db = sqlite3.connect("characters.db")
#db.isolation_level = None
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("A Game of Dissappearing Bears (working title)")


class Character():

    def __init__(self, name :str, sprite, attack :list, defense :list, hit_points :list):

        self.name = name
        self.sprite = sprite
        self.atk = attack
        self.df = defense
        self.hp = hit_points
        self.level = [0,0,100]
        self.alive = True
        self.taken_dmg = 0


    def give_exp(self,exp :int):
        if self.level[0] < 9:
            self.level[1] += exp
            while True:
                if self.level[1] >= self.level[2]:
                    self.level[0] += 1
                    self.level[1] = self.level[1]-self.level[2]
                    self.level[2] += 50
                    self.taken_dmg = 0
                else:
                    break


    def take_dmg(self,damage):
        if damage >= self.hp[self.level[0]]:
            self.taken_dmg += self.hp[self.level[0]]
            self.hp[self.level[0]] = 0
            self.alive = False
        else:
            self.hp[self.level[0]] -= damage
            self.taken_dmg += damage
    

    def reset_health(self):
        self.hp[self.level[0]] += self.taken_dmg
        self.taken_dmg = 0

    def attack(self,target,skill):
        if skill == 0:
            damage = self.atk[self.level[0]]-target.df[self.level[0]]//3
        else:
            damage = self.atk[self.level[0]] * skill.multiplier - target.df[self.level[0]]//3
        if damage <= 0:
            damage = 1
        target.take_dmg(damage)
        


class MainCharacter(Character):

    def __init__(self, name :str, over_sprite, sprite, attack :int, defense :int, hit_points :int, x :int, y :int):

        self.name = name
        self.sprite = sprite
        self.atk = attack
        self.df = defense
        self.hp = hit_points
        self.level = [0,0,100]
        self.alive = True
        self.taken_dmg = 0

        self.over_sprite = over_sprite
        self.x = x
        self.y = y
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.direction = 2


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



class Monster(Character):

    def __init__(self, name :str, over_sprite, sprite, attack :list, defense :list, hit_points :list, level: list, speed :int,):

        self.name = name
        self.sprite = sprite
        self.atk = attack
        self.df = defense
        self.hp = hit_points
        self.level = level
        self.alive = True
        self.taken_dmg = 0

        screen_width = pygame.image.load("Sprites/background_full.png").get_width()
        screen_height = pygame.image.load("Sprites/background_full.png").get_height()
        wall = pygame.image.load("Sprites/wall_length.png").get_height()

        self.over_sprite = over_sprite
        self.x = randint(wall+10,screen_width-wall-self.over_sprite.get_width()-10)
        self.y = randint(wall+10,screen_height-wall-self.over_sprite.get_height()-10)
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.speed_x = speed
        self.speed_y = speed


    def change_speed(self,cordinate):
        if cordinate == "x":
            self.speed_x = -self.speed_x
        if cordinate == "y":
            self.speed_y = -self.speed_y
    
class Boss(Character):

    def __init__(self,name :str, over_sprite, sprite, attack :list, defense :list, hit_points :list, level :list, x :int, y :int):

        self.name = name
        self.sprite = sprite
        self.atk = attack
        self.df = defense
        self.hp = hit_points
        self.level = level
        self.alive = True
        self.taken_dmg = 0   

        self.over_sprite = over_sprite
        self.x = x
        self.y = y

class Area():
    def __init__(self,background):
        self.left = None
        self.right = None
        self.bottom = None
        self.top = None
        self.background = background
        self.monsters = randint(0,6)
        self.start = False
        self.boss = False
    
    def set_start_location(self):
        self.start = True
    
    def set_boss_room(self):
        self.boss = True
    
    def set_neighbours(self,left,right,top,bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
    
    def activate(self,party :list, monsters: list, boss):
        
        screen_width = pygame.image.load("Sprites/background_full.png").get_width()
        screen_height = pygame.image.load("Sprites/background_full.png").get_height()
        wall = pygame.image.load("Sprites/wall_length.png").get_height()
        door_wide = pygame.image.load("Sprites/wide_length_door.png").get_width()
        door_tall = pygame.image.load("Sprites/tall_length_door.png").get_height()

        window = pygame.display.set_mode((screen_width, screen_height))
        

        font = pygame.font.SysFont("Arial", 25)
        big_font = pygame.font.SysFont("Arial", 50)
        
        area_monsters = []
        if self.start == False and self.boss == False: 
            for i in range(self.monsters):
                area_monsters.append(monsters[i])
        countdown = 0
        while True:
            window.fill((0,0,0))
            window.blit(self.background,(0,0))
            move(party[0],area_monsters)

            character_width = party[0].over_sprite[party[0].direction][countdown].get_width()
            character_height = party[0].over_sprite[party[0].direction][countdown].get_height()

            if self.boss:
                window.blit(boss.over_sprite, (boss.x, boss.y))
                if collision(party[0],boss,countdown):
                    battle(party,boss)
                    pygame.quit()

            if party[0].left and party[0].x >= wall and party[0].up == False and party[0].down == False:
                party[0].x -= 6
                countdown += 1
                party[0].direction = 0

            if party[0].left and party[0].x >= wall and (party[0].up or party[0].down):
                party[0].x -= 4
                countdown += 1
                party[0].direction = 0

            if party[0].right and party[0].x <= screen_width-character_width-wall and party[0].up == False and party[0].down == False:
                party[0].x += 6
                countdown += 1
                party[0].direction = 1
            
            if party[0].right and party[0].x <= screen_width-character_width-wall and (party[0].up or party[0].down):
                party[0].x += 4
                countdown += 1
                party[0].direction = 1

            if party[0].up and party[0].y >= wall and party[0].right == False and party[0].left == False:
                party[0].y -= 6
                countdown += 1
                party[0].direction = 2
            
            if party[0].up and party[0].y >= wall and (party[0].right or party[0].left):
                party[0].y -= 4
                countdown += 1
                party[0].direction = 2

            if party[0].down and party[0].y <= screen_height-character_height-wall and party[0].right == False and party[0].left == False:
                party[0].y += 6 
                countdown += 1
                party[0].direction = 3
            
            if party[0].down and party[0].y <= screen_height-character_height-wall and (party[0].right or party[0].left):
                party[0].y += 4
                countdown += 1
                party[0].direction = 3

            if countdown > 27:
                countdown = 0

            if party[0].right and party[0].x + 6 > screen_width-character_width-wall and door_tall < party[0].y < screen_height - door_tall:
                if self.right != None:
                    party[0].x = wall
                    self.right.activate(party,monsters,boss)
            if party[0].left and party[0].x - 6 < wall and door_tall < party[0].y < screen_height - door_tall:
                if self.left != None:
                    party[0].x = screen_width-wall-character_width
                    self.left.activate(party,monsters,boss)
            if party[0].up and party[0].y - 6 < wall and door_wide < party[0].x < screen_width - door_wide:
                if self.top != None:
                    party[0].y = screen_height-wall-character_height
                    self.top.activate(party,monsters,boss)
            if party[0].down and party[0].y + 6 > screen_height-character_height-wall and door_wide < party[0].x < screen_width - door_wide:
                if self.bottom != None:
                    party[0].y = wall
                    self.bottom.activate(party,monsters,boss)

            if len(area_monsters) != 0:
                for monster in area_monsters:
                    monster.x += monster.speed_x
                    monster.y += monster.speed_y
                    if monster.x >= screen_width-monster.over_sprite.get_width()-wall:
                        monster.change_speed("x")
                    if monster.x <= wall:
                        monster.change_speed("x")
                    if monster.y >= screen_height-monster.over_sprite.get_height()-wall:
                        monster.change_speed("y")
                    if monster.y <= wall:
                        monster.change_speed("y")  
                    window.blit(monster.over_sprite, (monster.x, monster.y))

                    if collision(party[0],monster,countdown):
                        battle(party,monster)
                        for character in party:
                            character.give_exp(monster.level[0]*50)
                        monster.reset_health()
                        monster.alive = True
                        area_monsters.remove(monster)
                        party[0].right = False
                        party[0].left = False
                        party[0].up = False
                        party[0].down = False

            window.blit(party[0].over_sprite[party[0].direction][countdown],(party[0].x,party[0].y))
            pygame.display.flip()
            clock.tick(50)



class StartGame():
    def __init__(self):
        self.party = []
        self.start = Area(pygame.image.load("Sprites/background_closed.png"))
        self.monsters = []
        self.boss = ""
        self.generate_map()
        self.choose_party()
        self.pick_monsters()

        self.start.activate(self.party,self.monsters,self.boss)
    
    def generate_map(self):
        pick = 1
        screen_width = pygame.image.load("Sprites/background_full.png").get_width()
        screen_height = pygame.image.load("Sprites/background_full.png").get_height()
        wall = pygame.image.load("Sprites/wall_length.png").get_height()

        if pick == 1:
            self.boss = Boss("Necromancer",pygame.image.load("Sprites/necromancer1.png"),pygame.image.load("Sprites/necromancer2.png"),
            [12,17,21,28,42,60,80,98,132,180],
            [10,14,18,24,33,48,60,74,92,120],
            [120,170,210,280,420,600,800,980,1220,1500],
            [1,0,0],screen_width/2-pygame.image.load("Sprites/necromancer1.png").get_width()/2,screen_height-pygame.image.load("Sprites/necromancer1.png").get_height()-wall)

            self.start = Area(pygame.image.load("Sprites/background_top.png"))
            area1 = Area(pygame.image.load("Sprites/background_left_right_bottom.png"))
            area2 = Area(pygame.image.load("Sprites/background_right_top.png"))
            area3 = Area(pygame.image.load("Sprites/background_left_right.png"))
            area4 = Area(pygame.image.load("Sprites/background_top_bottom.png"))
            area5 = Area(pygame.image.load("Sprites/background_left_top.png"))
            area6 = Area(pygame.image.load("Sprites/background_full.png"))
            area7 = Area(pygame.image.load("Sprites/background_right_top_bottom.png"))
            area8 = Area(pygame.image.load("Sprites/background_top_bottom.png"))
            area9 = Area(pygame.image.load("Sprites/background_top_bottom.png"))
            area10 = Area(pygame.image.load("Sprites/background_left.png"))
            area11 = Area(pygame.image.load("Sprites/background_right_bottom.png"))
            area12 = Area(pygame.image.load("Sprites/background_top_bottom.png"))
            area13 = Area(pygame.image.load("Sprites/background_left_right.png"))
            area14 = Area(pygame.image.load("Sprites/background_left_bottom.png"))
            area15 = Area(pygame.image.load("Sprites/background_left_bottom.png"))
            area16 = Area(pygame.image.load("Sprites/background_left_right.png"))
            area17 = Area(pygame.image.load("Sprites/background_top_bottom.png"))
            area18 = Area(pygame.image.load("Sprites/background_right_bottom.png"))
            area19 = Area(pygame.image.load("Sprites/background_left_top.png"))
            area20 = Area(pygame.image.load("Sprites/background_top_bottom.png"))
            area21 = Area(pygame.image.load("Sprites/background_left_top_bottom.png"))
            area22 = Area(pygame.image.load("Sprites/background_right_top_bottom.png"))
            area23 = Area(pygame.image.load("Sprites/background_left_right.png"))
            area24 = Area(pygame.image.load("Sprites/background_left_top.png"))
            area25 = Area(pygame.image.load("Sprites/background_left_right.png"))
            area26 = Area(pygame.image.load("Sprites/background_left_right_bottom.png"))
            area27 = Area(pygame.image.load("Sprites/background_right_bottom.png"))
            area28 = Area(pygame.image.load("Sprites/background_right_top.png"))
            area29 = Area(pygame.image.load("Sprites/background_top_bottom.png"))
            area30 = Area(pygame.image.load("Sprites/background_top_bottom.png"))
            area31 = Area(pygame.image.load("Sprites/background_left_right.png"))
            boss = Area(pygame.image.load("Sprites/background_top.png"))

            self.start.set_neighbours(None,None,area1,None)
            area1.set_neighbours(area2,area3,None,self.start)
            area2.set_neighbours(None,area1,area4,None)
            area3.set_neighbours(area1,area5,None,None)
            area4.set_neighbours(None,None,area6,area2)
            area5.set_neighbours(area3,None,area7,None)
            area6.set_neighbours(area23,area10,area8,area4)
            area7.set_neighbours(None,area31,area9,area5)
            area8.set_neighbours(None,None,area12,area6)
            area9.set_neighbours(None,None,area11,area7)
            area10.set_neighbours(area6,None,None,None)
            area11.set_neighbours(None,area13,None,area9)
            area12.set_neighbours(None,None,area14,area8)
            area13.set_neighbours(area11,area15,None,None)
            area14.set_neighbours(area16,None,None,area12)
            area15.set_neighbours(area13,None,None,area17)
            area16.set_neighbours(area18,area14,None,None)
            area17.set_neighbours(None,None,area15,area19)
            area18.set_neighbours(None,area16,None,area20)
            area19.set_neighbours(area31,None,area17,None)
            area20.set_neighbours(None,None,area18,area21)
            area21.set_neighbours(area25,None,area20,area22)
            area22.set_neighbours(None,area23,area21,area24)
            area23.set_neighbours(area22,area6,None,None)
            area24.set_neighbours(area26,None,area22,None)
            area25.set_neighbours(area27,area21,None,None)
            area26.set_neighbours(area28,area24,None,area30)
            area27.set_neighbours(None,area25,None,area29)
            area28.set_neighbours(None,area26,area29,None)
            area29.set_neighbours(None,None,area27,area28)
            area30.set_neighbours(None,None,area26,boss)
            area31.set_neighbours(area7,area19,None,None)
            boss.set_neighbours(None,None,area30,None)

            self.start.set_start_location()
            boss.set_boss_room()

            

    def choose_party(self):

        screen_width = pygame.image.load("Sprites/background_full.png").get_width()
        screen_height = pygame.image.load("Sprites/background_full.png").get_height()
        wall = pygame.image.load("Sprites/wall_length.png").get_height()
        
        walking_left = [pygame.image.load("Sprites/stand_left.png")]
        walking_right = [pygame.image.load("Sprites/stand_right.png")]
        walking_top = [pygame.image.load("Sprites/stand_top.png")]
        walking_down = [pygame.image.load("Sprites/stand_bot.png")]
        
        for i in range(7):
            walking_left.append(pygame.image.load("Sprites/step_left.png"))
            walking_right.append(pygame.image.load("Sprites/step_right.png"))
            walking_top.append(pygame.image.load("Sprites/step_top.png"))
            walking_down.append(pygame.image.load("Sprites/step_bot.png"))
        for i in range(7):
            walking_left.append(pygame.image.load("Sprites/stand_left.png"))
            walking_right.append(pygame.image.load("Sprites/stand_right.png"))
            walking_top.append(pygame.image.load("Sprites/stand_top.png"))
            walking_down.append(pygame.image.load("Sprites/stand_bot.png"))
        for i in range(7):
            walking_left.append(pygame.image.load("Sprites/step_left2.png"))
            walking_right.append(pygame.image.load("Sprites/step_right2.png"))
            walking_top.append(pygame.image.load("Sprites/step_top2.png"))
            walking_down.append(pygame.image.load("Sprites/step_bot2.png"))
        for i in range(7):
            walking_left.append(pygame.image.load("Sprites/stand_left.png"))
            walking_right.append(pygame.image.load("Sprites/stand_right.png"))
            walking_top.append(pygame.image.load("Sprites/stand_top.png"))
            walking_down.append(pygame.image.load("Sprites/stand_bot.png"))

        walking_animation = [walking_left,walking_right,walking_top,walking_down]


        main_character = MainCharacter("Leon",walking_animation,pygame.image.load("Sprites/main_character.png"),
        [1200,1700,21,28,42,60,80,98,132,180],
        [10,14,18,24,33,48,60,74,92,120],
        [120,170,210,280,420,600,800,980,1220,1500],
        screen_width/2,screen_height/2)

        Knight = Character("Knight",pygame.image.load("Sprites/knight.png"),
        [3,5,8,14,19,26,42,58,70,88],
        [18,25,33,50,72,94,118,142,180,240],
        [240,320,500,680,840,1020,1300,1580,1880,2400])
        
        Archer = Character("Archer",pygame.image.load("Sprites/archer.png"),
        [9,14,18,24,36,52,72,88,102,144],
        [4,9,15,21,30,36,50,66,84,112],
        [80,120,200,350,490,600,720,910,1080,1320])
        
        Wizard = Character("Wizard",pygame.image.load("Sprites/wizard.png"),
        [4,8,13,20,28,36,50,72,98,120],
        [18,25,33,50,72,94,118,142,180,240],
        [240,320,500,680,840,1020,1300,1580,1880,2400])
        
        Assassin = Character("Assassin",pygame.image.load("Sprites/assassin.png"),
        [3,5,8,14,19,26,42,58,70,88],
        [18,25,33,50,72,94,118,142,180,240],
        [240,320,500,680,840,1020,1300,1580,1880,2400])

        Monk = Character("Monk",pygame.image.load("Sprites/monk.png"),
        [3,5,8,14,19,26,42,58,70,88],
        [18,25,33,50,72,94,118,142,180,240],
        [240,320,500,680,840,1020,1300,1580,1880,2400])

        self.party.append(main_character)
        self.party.append(Knight)
        self.party.append(Wizard)
        self.party.append(Assassin)
    

    def pick_monsters(self):

        monster1 = Monster("Demon Assassin",pygame.image.load("Sprites/demon.png"),pygame.image.load("Sprites/demon.png"),
        [12,17,21,28,42,60,80,98,132,180],
        [10,14,18,24,33,48,60,74,92,120],
        [120,170,210,280,420,600,800,980,1220,1500],
        [1,0,0],6)

        monster2 = Monster("Beholder",pygame.image.load("Sprites/eyeball.png"),pygame.image.load("Sprites/eyeball.png"),
        [12,17,21,28,42,60,80,98,132,180],
        [10,14,18,24,33,48,60,74,92,120],
        [120,170,210,280,420,600,800,980,1220,1500],
        [1,0,0],4)

        monster3 = Monster("Goblin Soldier",pygame.image.load("Sprites/goblin.png"),pygame.image.load("Sprites/goblin.png"),
        [12,17,21,28,42,60,80,98,132,180],#atk
        [10,14,18,24,33,48,60,74,92,120], #def
        [120,170,210,280,420,600,800,980,1220,1500], #hp
        [1,0,0],4)

        monster4 = Monster("Skeleton Warrior",pygame.image.load("Sprites/skeleton.png"),pygame.image.load("Sprites/skeleton.png"),
        [12,17,21,28,42,60,80,98,132,180],
        [10,14,18,24,33,48,60,74,92,120],
        [120,170,210,280,420,600,800,980,1220,1500],
        [1,0,0],3)

        monster5 = Monster("Warlock",pygame.image.load("Sprites/warlock.png"),pygame.image.load("Sprites/warlock.png"),
        [12,17,21,28,42,60,80,98,132,180],
        [10,14,18,24,33,48,60,74,92,120],
        [120,170,210,280,420,600,800,980,1220,1500],
        [1,0,0],2)

        monster6 = Monster("Dragonling",pygame.image.load("Sprites/dragonling.png"),pygame.image.load("Sprites/dragonling.png"),
        [12,17,21,28,42,60,80,98,132,180],
        [10,14,18,24,33,48,60,74,92,120],
        [120,170,210,280,420,600,800,980,1220,1500],
        [1,0,0],5)
        
        self.monsters.append(monster1)
        self.monsters.append(monster2)
        self.monsters.append(monster3)
        self.monsters.append(monster4)
        self.monsters.append(monster5)
        self.monsters.append(monster6)
    


def move(character :MainCharacter,monsters :list):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character.move_left()
            if event.key == pygame.K_RIGHT:
                character.move_right()
            if event.key == pygame.K_UP:
                character.move_up()
            if event.key == pygame.K_DOWN:
                character.move_down()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character.stop_left()
            if event.key == pygame.K_RIGHT:
                character.stop_right()
            if event.key == pygame.K_UP:
                character.stop_up()
            if event.key == pygame.K_DOWN:
                character.stop_down()     

def collision(character,monster,countdown):
    character_width = character.over_sprite[character.direction][countdown].get_width()
    character_height = character.over_sprite[character.direction][countdown].get_height()
    if monster.x-character_width/2 <= character.x+character_width/2 <= monster.x+monster.over_sprite.get_width()+character_width/2 and monster.y-character_height/2 <= character.y+character_height/2 <= monster.y+monster.over_sprite.get_height()+character_height/2:
        return True

def battle(party,monster):
    screen_width = pygame.image.load("Sprites/background_full.png").get_width()
    screen_height = pygame.image.load("Sprites/background_full.png").get_height()
    wall = pygame.image.load("Sprites/wall_length.png").get_height()
    door_wide = pygame.image.load("Sprites/wide_length_door.png").get_width()
    door_tall = pygame.image.load("Sprites/tall_length_door.png").get_height()

    window = pygame.display.set_mode((screen_width, screen_height))
        
    font = pygame.font.SysFont("Arial", 25)
    big_font = pygame.font.SysFont("Arial", 50)

    while True:
        for character in party:
            window.fill((0, 0, 0))
            window.blit(font.render(f"{monster.name}:   {monster.hp[monster.level[0]]}/{monster.hp[monster.level[0]]+monster.taken_dmg}", True, (200, 0, 0)), (20, 0))

            window.blit(font.render(character.name, True, (200,200,200)),(0,screen_height-125))
            window.blit(font.render("1. Attack", True, (200,200,200)),(0,screen_height-100))
            window.blit(font.render("2. Skill", True, (200,200,200)),(0,screen_height-75))
            window.blit(font.render("3. Item", True, (200,200,200)),(0,screen_height-50))
            window.blit(font.render("4. Run", True, (200,200,200)),(0,screen_height-25))

            for i in range(0,4):
                window.blit(font.render(party[i].name, True, (0,200,0)),(300,screen_height-100+i*25))
                window.blit(font.render(f"HP  {party[i].hp[party[i].level[0]]}/{party[i].hp[party[i].level[0]]+party[i].taken_dmg}", True, (0,200,0)),(500,screen_height-100+i*25))
                window.blit(font.render("MP  0/0", True, (0,200,0)),(750,screen_height-100+i*25))
                window.blit(font.render(f"LVL  {party[i].level[0]+1}/10", True, (0,200,0)),(950,screen_height-100+i*25))
                window.blit(party[i].sprite,(i*10+10,300+i*100))

            window.blit(monster.sprite,(screen_width-monster.sprite.get_width()-10,450))

            pygame.display.flip()
            if character.alive:
                action = choose_action(party,monster)

                if action == 1:
                    character.attack(monster,0)

            if monster.alive == False:
                return

        monster.attack(party[randint(0,3)],0)

        

def choose_action(party,monster):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    return 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    return 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    return 4

# monster design credits: Stephen "Redshrike" Challener, hosted by OpenGameArt.org
# main character overhead sprite credits: ArMM1998, hosted by OpenGameArt.org
# character sprite credits: wulax, hosted by OpenGameArt.org

if __name__ =="__main__":
    StartGame()