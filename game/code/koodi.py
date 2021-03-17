import pygame
from random import randint
pygame.init()
screen_width = 1000
screen_height = 800
window = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 54)



class Character():

    def __init__(self, name :str, sprite, attack :list, defense :list, hit_points :list):

        self.name = name
        self.sprite = sprite
        self.atk = attack
        self.df = defense
        self.hp = hit_points
        self.level = [1,0,100]
        self.alive = True

    def give_exp(self,exp :int):
        if self.level[0] < 10:
            self.level[1] += exp
            if self.level[1] >= self.level[2]:
                self.level[0] += 1
                self.level[1] = self.level[1]-self.level[2]
                self.level[2] += 50
    
    def take_dmg(self,damage):
        if damage >= self.hp[self.level[0]]:
            self.hp[self.level[0]] = 0
            self.alive = False
        else:
            self.hp[self.level[0]] -= damage
    
    def attack(self,target,skill):
        if skill == 0:
            damage = self.atk[self.level[0]]-target.df[self.level[0]]
        else:
            damage = self.atk[self.level[0]] * skill.multiplier - target.df[self.level[0]]
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
        self.level = [1,0,100]
        self.alive = True

        self.over_sprite = over_sprite
        self.x = x
        self.y = y
        self.right = False
        self.left = False
        self.up = False
        self.down = False
    
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

    def __init__(self, name :str, over_sprite, sprite, attack :int, defense :int, hit_points :int, level: list, speed :int, x :int, y :int):

        self.name = name
        self.sprite = sprite
        self.atk = attack
        self.df = defense
        self.hp = hit_points
        self.level = level
        self.alive = True

        self.over_sprite = over_sprite
        self.x = x
        self.y = y
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


def move(party: list,monsters :list):
    character = party[0]
    window.blit(character.over_sprite, (character.x, character.y))
    

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

    if character.right and character.x <= screen_width-character.over_sprite.get_width():
        character.x += 6
    if character.left and character.x >= 0:
        character.x -= 6
    if character.up and character.y >= 0:
        character.y -= 6
    if character.down and character.y <= screen_height-character.over_sprite.get_height():
        character.y += 6 

    if len(monsters) != 0:
        for monster in monsters:
            monster.x += monster.speed_x
            monster.y += monster.speed_y
            if monster.x >= screen_width-monster.over_sprite.get_width():
                monster.change_speed("x")
            if monster.x <= 0:
                monster.change_speed("x")
            if monster.y >= screen_height-monster.over_sprite.get_height():
                monster.change_speed("y")
            if monster.y <= 0:
                monster.change_speed("y")  
            window.blit(monster.over_sprite, (monster.x, monster.y))

            if monster.x-character.over_sprite.get_width()/2 <= character.x+character.over_sprite.get_width()/2 <= monster.x+monster.over_sprite.get_width()+character.over_sprite.get_width()/2 and monster.y-character.over_sprite.get_height()/2 <= character.y+character.over_sprite.get_height()/2 <= monster.y+monster.over_sprite.get_height()+character.over_sprite.get_height()/2:
                battle(party,monster)
    


def battle(party,monster):
    while True:
        for character in party:
            window.fill((0, 0, 0))
            window.blit(font.render(f"{monster.name}:   {monster.hp[monster.level[0]]}", True, (200, 0, 0)), (20, 0))
            window.blit(font.render(f"{party[0].name}:   {party[0].hp[party[0].level[0]]}", True, (0, 200, 0)), (20, 50))
            window.blit(font.render(f"{party[1].name}:   {party[1].hp[party[0].level[0]]}", True, (0, 200, 0)), (20, 100))
            window.blit(font.render(f"{party[2].name}:   {party[2].hp[party[0].level[0]]}", True, (0, 200, 0)), (20, 150))
            window.blit(font.render(f"{party[3].name}:   {party[3].hp[party[0].level[0]]}", True, (0, 200, 0)), (20, 200))
            pygame.display.flip()
            action = choose_action(party,monster)

            if action == 1:
                character.attack(monster,0)

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


def choose_party():
    party = []

    Leon = MainCharacter("Leon",pygame.image.load("Sprites/standing.png"),"sprite",[12,17,21,28,42,60,80,98,132,180],[10,14,18,24,33,48,60,74,92,120],[120,170,210,280,420,600,800,980,1220,1500],0,0)
    Lise = MainCharacter("Lise",pygame.image.load("Sprites/standing.png"),"sprite",[12,17,21,28,42,60,80,98,132,180],[10,14,18,24,33,48,60,74,92,120],[120,170,210,280,420,600,800,980,1220,1500],0,0)
    Tank = Character("Tank","sprite",[3,5,8,14,19,26,42,58,70,88],[18,25,33,50,72,94,118,142,180,240],[240,320,500,680,840,1020,1300,1580,1880,2400])
    Archer = Character("Archer","sprite",[9,14,18,24,36,52,72,88,102,144],[4,9,15,21,30,36,50,66,84,112],[80,120,200,350,490,600,720,910,1080,1320])
    Wizard = Character("Wizard","sprite",[4,8,13,20,28,36,50,72,98,120],[18,25,33,50,72,94,118,142,180,240],[240,320,500,680,840,1020,1300,1580,1880,2400])
    Berserker = Character("Berserker","sprite",[3,5,8,14,19,26,42,58,70,88],[18,25,33,50,72,94,118,142,180,240],[240,320,500,680,840,1020,1300,1580,1880,2400])

    party.append(Leon)
    party.append(Tank)
    party.append(Wizard)
    party.append(Archer)

    monster1 = Monster("Monnie",pygame.image.load("Sprites/standing.png"),"sprite",[12,17,21,28,42,60,80,98,132,180],[10,14,18,24,33,48,60,74,92,120],[120,170,210,280,420,600,800,980,1220,1500],[1,0,0],1,100,100)
    monster2 = Monster("Monnie",pygame.image.load("Sprites/standing.png"),"sprite",[12,17,21,28,42,60,80,98,132,180],[10,14,18,24,33,48,60,74,92,120],[120,170,210,280,420,600,800,980,1220,1500],[2,0,0],2,200,100)
    monster3 = Monster("Monnie",pygame.image.load("Sprites/standing.png"),"sprite",[12,17,21,28,42,60,80,98,132,180],[10,14,18,24,33,48,60,74,92,120],[120,170,210,280,420,600,800,980,1220,1500],[3,0,0],3,300,100)
    monster4 = Monster("Monnie",pygame.image.load("Sprites/standing.png"),"sprite",[12,17,21,28,42,60,80,98,132,180],[10,14,18,24,33,48,60,74,92,120],[120,170,210,280,420,600,800,980,1220,1500],[4,0,0],4,400,100)

    monsters = [monster1,monster2,monster3,monster4]

    area1(party,monsters)

def area1(party :list, monsters :list):
    while True:
        window.fill((0, 150, 150))
        move(party,monsters)
        pygame.display.flip()
        clock.tick(60)


choose_party()
