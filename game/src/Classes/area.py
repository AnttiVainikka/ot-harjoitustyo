import pygame
# pylint: disable=no-member
pygame.init()
from random import randint
from Classes.character import Character
from Battle.battle import battle
from UI.move import move
from StartGame.render import render_game_over
from UI.action import choose_action
screen_width = pygame.image.load("src/Sprites/background_full.png").get_width()
screen_height = pygame.image.load("src/Sprites/background_full.png").get_height()
wall = pygame.image.load("src/Sprites/wall_length.png").get_height()
door_wide = pygame.image.load("src/Sprites/wide_length_door.png").get_width()
door_tall = pygame.image.load("src/Sprites/tall_length_door.png").get_height()
window = pygame.display.set_mode((screen_width, screen_height)) 
clock = pygame.time.Clock()

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
        area_monsters = []
        if not self.start and not self.boss: 
            for i in range(self.monsters):
                area_monsters.append(monsters[i])
                monsters[i].x = randint(wall, screen_width-wall-monsters[i].over_sprite.get_width())
                monsters[i].y = randint(wall, screen_height-wall-monsters[i].over_sprite.get_height())
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
                    render_game_over("victory")
                    while True:
                        choose_action("victory")

            if party[0].left and party[0].x >= wall and party[0].up is False and party[0].down is False:
                party[0].x -= 6
                countdown += 1
                party[0].direction = 0

            if party[0].left and party[0].x >= wall and (party[0].up or party[0].down):
                party[0].x -= 4
                countdown += 1
                party[0].direction = 0

            if party[0].right and party[0].x <= screen_width-character_width-wall and party[0].up is False and party[0].down is False:
                party[0].x += 6
                countdown += 1
                party[0].direction = 1
            
            if party[0].right and party[0].x <= screen_width-character_width-wall and (party[0].up or party[0].down):
                party[0].x += 4
                countdown += 1
                party[0].direction = 1

            if party[0].up and party[0].y >= wall and party[0].right is False and party[0].left is False:
                party[0].y -= 6
                countdown += 1
                party[0].direction = 2
            
            if party[0].up and party[0].y >= wall and (party[0].right or party[0].left):
                party[0].y -= 4
                countdown += 1
                party[0].direction = 2

            if party[0].down and party[0].y <= screen_height-character_height-wall and party[0].right is False and party[0].left is False:
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


def collision(character,monster,countdown):
    character_width = character.over_sprite[character.direction][countdown].get_width()
    character_height = character.over_sprite[character.direction][countdown].get_height()
    if monster.x-character_width/2 <= character.x+character_width/2 <= monster.x+monster.over_sprite.get_width()+character_width/2 and monster.y-character_height/2 <= character.y+character_height/2 <= monster.y+monster.over_sprite.get_height()+character_height/2:
        return True