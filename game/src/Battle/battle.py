from random import randint
from Classes.character import Character
from UI.action import choose_action
from StartGame.render import render_battle
from StartGame.render import render_game_over
from StartGame.render import render_info
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

            if monster.alive is False:
                for skill in active_skills:
                    skill.deactivate(party,monster)
                return True

            if character.alive:
                while True:
                    render_battle(party,monster,character,"battle")

                    while True:
                        action = choose_action("battle")
                        if 1 <= action <= 4:
                            break

                    if action == 1:
                        character.attack(monster,0)
                        break       
                     
                    if action == 2:
                        if use_skill(party,monster,character,active_skills):
                            break

                    if action == 3:
                        if use_item(party,monster,character):
                            break

                    if action == 4:
                        if not monster.boss:
                            chance = randint(1,3)
                            if chance == 1:
                                return False
                            break

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
        if monster.status[0] == "Poison":
            monster.take_dmg((monster.hp+monster.taken_dmg)//6)
            monster.status[1] -= 1
            if monster.status[1] <= 0:
                monster.status = ["none",0]


def use_skill(party,monster,character,active_skills):
    render_battle(party,monster,character,"choose_skill")
    while True:
        choice = choose_action("choose skill")
        if choice == "d":
            render_info(character.skills)
            while True:
                if choose_action("choose skill") == 0:
                    render_battle(party,monster,character,"choose_skill")
                    break
        elif choice <= len(character.skills):
            if choice == 0:
                return False
            skill = character.skills[choice-1]
            if character.mp - skill.cost >= 0:
                break
    character.mp -= skill.cost
    character.used_mp += skill.cost

    if skill.aoe != 1:
        if skill.buff == 0 and skill.recover == 0 and skill.resurrect == 0:
            #target = choose_action("battle")
            #render_battle(party,monster,character,"battle")
            skill.activate(character,monster)

        elif skill.recover == 1:
            if skill.aoe == -1:
                skill.activate(character,character)
                return True
            render_battle(party,monster,character,"choose_target_ally")
            while True:
                target = choose_action("choose target")
                if 0 <= target <= 4:
                    if target == 0:
                        return False
                    if party[target-1].alive is True:
                        skill.activate(character,party[target-1])
                        break

        elif skill.resurrect == 1:
            render_battle(party,monster,character,"choose_target_ally")
            while True:
                target = choose_action("choose target")
                if 0 <= target <= 4:
                    if target == 0:
                        return False
                    if party[target-1].alive is False:
                        skill.activate(character,party[target-1])
                        break
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
    return True

def use_item(party,monster,user):
    render_battle(party,monster,user,"choose_item")
    character = party[0]
    while True:
        choice = choose_action("choose skill")
        if choice == 0:
            return False
        if choice == "d":
            render_info(character.items)
            while True:
                if choose_action("choose skill") == 0:
                    render_battle(party,monster,user,"choose_item")
                    break
        elif choice <= len(character.items):
            item = character.items[choice-1]
            if item.amount > 0:
                break
    if item.aoe == 0:
        render_battle(party,monster,character,"choose_target_ally")
        while True:
            target = choose_action("choose target")
            try:
                if target == 0:
                    return False
                if item.use(party[target-1]):
                    item.amount -= 1
                    return True
            except IndexError:
                pass
    else:
        for member in party:
            item.use(member)
        item.amount -= 1
        return True
