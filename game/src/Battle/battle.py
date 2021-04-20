from random import randint
from Classes.character import Character
from UI.action import choose_action
from StartGame.render import render_battle
from StartGame.render import render_game_over
import pygame
# pylint: disable=no-member
pygame.init()
screen_width = pygame.image.load("src/Sprites/background_full.png").get_width()
screen_height = pygame.image.load("src/Sprites/background_full.png").get_height()
wall = pygame.image.load("src/Sprites/wall_length.png").get_height()
door_wide = pygame.image.load("src/Sprites/wide_length_door.png").get_width()
door_tall = pygame.image.load("src/Sprites/tall_length_door.png").get_height()
window = pygame.display.set_mode((screen_width, screen_height)) 
font = pygame.font.SysFont("Arial", 25)


def battle(party,monster):
    active_skills = []
    while True:
        for skill in active_skills:
            skill.duration -= 1
            if skill.duration == 0:
                skill.deactivate(party,monster)
                active_skills.remove(skill)
        for character in party:
            if character.alive:
                while True:
                    move_on = True
                    render_battle(party,monster,character,"battle")

                    while True:
                        action = choose_action("battle")
                        if 1 <= action <= 4:
                            break

                    if action == 1:
                        character.attack(monster,0)
                        break       
                     
                    if action == 2:
                        render_battle(party,monster,character,"choose_skill")
                        while True:
                            choice = choose_action("choose skill")
                            if choice <= len(character.skills):
                                break
                        if choice != 0:
                            if character.mp - character.skills[choice-1].cost >= 0:
                                skill = character.skills[choice-1]
                                character.mp -= skill.cost
                                character.used_mp += skill.cost
                                if skill.aoe == 0:
                                    if skill.buff == 0 and skill.recover == 0 and skill.resurrect == 0:
                                        #target = choose_action("battle")
                                        #render_battle(party,monster,character,"battle")
                                        skill.activate(character,monster)
                                    elif skill.recover == 1:
                                        render_battle(party,monster,character,"choose_target_ally")
                                        while True:
                                            target = choose_action("choose target")
                                            try:
                                                if target == 0 or party[target-1].alive is True:
                                                    break
                                            except IndexError:
                                                pass
                                        if target == 0:
                                            move_on = False
                                        else:
                                            skill.activate(character,party[target-1])  
                                    elif skill.resurrect == 1:
                                        render_battle(party,monster,character,"choose_target_ally")
                                        while True:
                                            target = choose_action("choose target")
                                            try:
                                                if target == 0 or party[target-1].alive is False:
                                                    break
                                            except IndexError:
                                                pass
                                        if target == 0:
                                            move_on = False
                                        else:
                                            skill.activate(character,party[target-1])                                        
                                    else:
                                        if skill in active_skills:
                                            skill.deactivate(party,monster)
                                            active_skills.remove(skill)
                                        skill.activate(character,character)
                                        skill.user = character.name
                                        active_skills.append(skill)
                                else:
                                    if skill.buff == 0 and skill.recover == 0:
                                        skill.activate(character,monster)
                                    elif skill.recover == 1:
                                        for party_member in party:
                                            skill.activate(character,party_member)
                                    else:
                                        if skill in active_skills:
                                            skill.deactivate(party,monster)
                                            active_skills.remove(skill)
                                        for party_member in party:
                                            skill.activate(character,party_member)
                                        active_skills.append(skill)
                                if move_on is True:
                                    break

            if monster.alive is False:
                for skill in active_skills:
                    skill.deactivate(party,monster)
                return

        alive_characters = 4
        for character in party:
            if character.alive is False:
                alive_characters -= 1
        if alive_characters == 0:
            render_game_over("defeat")
            while True:
                choose_action("defeat")

        while True:
            target = randint(0,3)
            if party[target].alive:
                break
        monster.attack(party[target],0)
