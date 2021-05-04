import pygame
# pylint: disable=no-member
pygame.init()
from random import randint
from Classes.character import Character
from Battle.battle import battle
from UI.move import move
from UI.render import render_game_over
from UI.render import render_area
from UI.action import choose_action
screen_width = pygame.image.load("src/Sprites/background_full.png").get_width()
screen_height = pygame.image.load("src/Sprites/background_full.png").get_height()
wall = pygame.image.load("src/Sprites/wall_length.png").get_height()
door_wide = pygame.image.load("src/Sprites/wide_length_door.png").get_width()
door_tall = pygame.image.load("src/Sprites/tall_length_door.png").get_height()
window = pygame.display.set_mode((screen_width, screen_height)) 
clock = pygame.time.Clock()

class Area():
    """The class for the areas the map consists of."""
    def __init__(self,background):
        self.left = None
        self.right = None
        self.bottom = None
        self.top = None
        self.background = background
        self.start = False
        self.boss = False
    
    def set_start_location(self):
        """Sets the area as the start location where the player spawns."""
        self.start = True
    
    def set_boss_room(self):
        """Sets the area as the boss room where no other monsters roam."""
        self.boss = True
    
    def set_neighbours(self,left,right,top,bottom):
        """Sets the areas connected to the area"""
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
    
    def activate(self,party :list, monsters: list, boss):
        """Lets the player move around in the area and activates battles if the player collides with a monster."""
        area_monsters = []
        if not self.start and not self.boss: 
            for _ in range(randint(0,6)):
                while True:
                    monster = monsters[randint(0,len(monsters)-1)]
                    if monster not in area_monsters:
                        area_monsters.append(monster)
                        break
                monster.x = randint(wall, screen_width-wall-monster.over_sprite.get_width())
                monster.y = randint(wall, screen_height-wall-monster.over_sprite.get_height())
        countdown = 0
        while True:
            move(party[0])
            character_width = party[0].over_sprite[party[0].direction][countdown].get_width()
            character_height = party[0].over_sprite[party[0].direction][countdown].get_height()

            if self.boss:
                if collision(party[0],boss,countdown):
                    battle(party,[boss])
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
                if self.right is not None:
                    party[0].x = wall
                    self.right.activate(party,monsters,boss)
            if party[0].left and party[0].x - 6 < wall and door_tall < party[0].y < screen_height - door_tall:
                if self.left is not None:
                    party[0].x = screen_width-wall-character_width
                    self.left.activate(party,monsters,boss)
            if party[0].up and party[0].y - 6 < wall and door_wide < party[0].x < screen_width - door_wide:
                if self.top is not None:
                    party[0].y = screen_height-wall-character_height
                    self.top.activate(party,monsters,boss)
            if party[0].down and party[0].y + 6 > screen_height-character_height-wall and door_wide < party[0].x < screen_width - door_wide:
                if self.bottom is not None:
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

                    if collision(party[0],monster,countdown):
                        if battle(party,monster.monsters):
                            for character in party:
                                character.give_exp(monster.monsters[0].level[0]*50*len(monster.monsters))
                        area_monsters.remove(monster)
                        party[0].right = False
                        party[0].left = False
                        party[0].up = False
                        party[0].down = False
            render_area(party,area_monsters,party[0].direction,countdown,self,boss)
            clock.tick(50)


def collision(character,monster,countdown):
    """Checks if the main character collides with a monster."""
    character_width = character.over_sprite[character.direction][countdown].get_width()
    character_height = character.over_sprite[character.direction][countdown].get_height()
    if monster.x-character_width/2 <= character.x+character_width/2 <= monster.x+monster.over_sprite.get_width()+character_width/2 and monster.y-character_height/2 <= character.y+character_height/2 <= monster.y+monster.over_sprite.get_height()+character_height/2:
        return True