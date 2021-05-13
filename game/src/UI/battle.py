from random import randint
from UI.action import choose_action
from UI.render import render_battle
from UI.render import render_game_over
from UI.render import render_info
from UI.render import render_action
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


def battle(party,monsters):
    """The main code for battles. Asks the player what they want to do and leads to the corresponding function. Ends when all monsters are defeated."""
    for monster in monsters:
        for i in range(1,party[0].level[0]+1):
            monster.level_up(i)
    if monsters[0].boss:
        for i in range(1,party[0].level[0]+1):
            monsters[0].level_up(min(i+3,10))
    active_skills = []
    characters = []
    for character in party:
        characters.append(character)
    for character in monsters:
        characters.append(character)
    while True:
        for skill in active_skills:
            skill.duration -= 1
            if skill.duration == 0:
                skill.deactivate(party,monsters)
                active_skills.remove(skill)
        for character in characters:
            if character.alive:
                while True:
                    render_battle(party,monsters,character,"battle")
                    if character.monster is False:
                        while True:
                            action = choose_action("battle")
                            if 1 <= action <= 4:
                                break

                        if action == 1:
                            render_battle(party,monsters,character,"choose_target_enemy")
                            while True:
                                target = choose_action("choose target")
                                if 0 <= target <= len(monsters):
                                    if monsters[target-1].alive is True or target == 0:
                                        break
                            if target != 0:
                                character.attack(monsters[target-1],0)
                                break

                        if action == 2:
                            skill = use_skill(party,monsters,character,active_skills)
                            if skill is not False:
                                render_action(skill.name,500)
                                break

                        if action == 3:
                            item = use_item(party,monsters,character)
                            if item is not False:
                                render_action(item.name,500)
                                break

                        if action == 4:
                            if not monsters[0].boss:
                                chance = randint(1,3)
                                if chance == 1:
                                    render_action("ESCAPE",1000)
                                    return False
                                render_action("ESCAPE FAILED",800)
                                break
                            render_action("CAN'T ESCAPE",800)
                    else:
                        while True:
                            target = randint(0,3)
                            if party[target].alive:
                                break
                        action = randint(1,len(character.skills)+8)
                        if character.boss:
                            action += 2
                        if action > 5:
                            if len(character.skills) > 0:
                                skill = character.skills[randint(0,len(character.skills)-1)]
                                if skill.aoe != 1:
                                    skill.activate(character,party[target])
                                else:
                                    for party_member in party:
                                        skill.activate(character,party_member)
                                render_action(skill.name,1000)
                                break
                        character.attack(party[target],0)
                        render_action("ATTACK",500)
                        break

                if character.status[0] == "Poison":
                    render_battle(party,monsters,character,"battle")
                    character.take_dmg((character.hp+character.taken_dmg)//4)
                    render_action("POISON DAMAGE",500)
                    character.status[1] -= 1
                    if character.status[1] <= 0:
                        character.status = ["none",0]
                        render_battle(party,monsters,character,"battle")
                        render_action("POISON CURED",800)
                render_battle(party,monsters,character,"battle")
                pygame.time.wait(50)
            alive_characters = 4
            alive_monsters = len(monsters)
            for character in characters:
                if character.alive is False:
                    if character.monster is False:
                        alive_characters -= 1
                    else:
                        alive_monsters -= 1
            if alive_characters == 0:
                render_game_over("defeat")
                while True:
                    choose_action("defeat")

            if alive_monsters == 0:
                for skill in active_skills:
                    skill.deactivate(party,monsters)
                render_action("VICTORY",1000)
                return True



def use_skill(party,monsters,character,active_skills):
    """Activates chosen skill and returns False if something went wrong."""
    render_battle(party,monsters,character,"choose_skill")
    while True:
        choice = choose_action("choose skill")
        if choice == "d":
            render_info(character.skills)
            while True:
                if choose_action("choose skill") == 0:
                    render_battle(party,monsters,character,"choose_skill")
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
            render_battle(party,monsters,character,"choose_target_enemy")
            while True:
                target = choose_action("choose target")
                if 0 <= target <= len(monsters):
                    if target == 0:
                        return False
                    if monsters[target-1].alive is True:
                        skill.activate(character,monsters[target-1])
                        break

        elif skill.recover == 1:
            if skill.aoe == -1:
                skill.activate(character,character)
                return skill
            render_battle(party,monsters,character,"choose_target_ally")
            while True:
                target = choose_action("choose target")
                if 0 <= target <= 4:
                    if target == 0:
                        return False
                    if party[target-1].alive is True:
                        skill.activate(character,party[target-1])
                        break
                    render_action("Target must be alive",500)
                    render_battle(party,monsters,character,"choose_target_ally")

        elif skill.resurrect == 1:
            render_battle(party,monsters,character,"choose_target_ally")
            while True:
                target = choose_action("choose target")
                if 0 <= target <= 4:
                    if target == 0:
                        return False
                    if party[target-1].alive is False:
                        skill.activate(character,party[target-1])
                        break
                    render_action("Target must be dead",500)
                    render_battle(party,monsters,character,"choose_target_ally")
        else:
            if skill in active_skills:
                skill.deactivate(party,monsters)
                active_skills.remove(skill)
            skill.activate(character,character)
            skill.user = character.name
            active_skills.append(skill)

    else:
        if skill.buff == 0 and skill.recover == 0:
            for monster in monsters:
                skill.activate(character,monster)
        elif skill.recover == 1:
            for party_member in party:
                skill.activate(character,party_member)
        else:
            if skill in active_skills:
                skill.deactivate(party,monsters)
                active_skills.remove(skill)
            for party_member in party:
                skill.activate(character,party_member)
            active_skills.append(skill)
    return skill

def use_item(party,monsters,user):
    """Activates chosen item and returns True if skill was used and False if something went wrong."""
    render_battle(party,monsters,user,"choose_item")
    character = party[0]
    while True:
        choice = choose_action("choose skill")
        if choice == 0:
            return False
        if choice == "d":
            render_info(character.items)
            while True:
                if choose_action("choose skill") == 0:
                    render_battle(party,monsters,user,"choose_item")
                    break
        elif choice <= len(character.items):
            item = character.items[choice-1]
            if item.amount > 0:
                break
    if item.aoe == 0:
        render_battle(party,monsters,character,"choose_target_ally")
        while True:
            target = choose_action("choose target")
            try:
                if target == 0:
                    return False
                if item.use(party[target-1]):
                    item.amount -= 1
                    return item
                else:
                    render_action("Does nothing on target",500)
                    render_battle(party,monsters,character,"choose_target_ally")
            except IndexError:
                pass
    else:
        for member in party:
            item.use(member)
        item.amount -= 1
        return item
