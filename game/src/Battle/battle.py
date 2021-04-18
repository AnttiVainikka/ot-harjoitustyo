from random import randint
from Classes.character import Character
from UI.action import choose_action
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

def render_battle(party,monster,character,setting):
    window.fill((0, 0, 0))
    window.blit(font.render(f"{monster.name}:   {monster.hp}/{monster.hp+monster.taken_dmg}", True, (200, 0, 0)), (20, 0))
    window.blit(font.render(character.name, True, (200,200,200)),(0,screen_height-125))
    window.blit(monster.sprite,(screen_width-monster.sprite.get_width()-10,450))

    for i in range(0,4):
            window.blit(party[i].sprite,(i*10+10,300+i*100))

    if setting == "battle":
        window.blit(font.render("1. Attack", True, (200,200,200)),(0,screen_height-100))
        window.blit(font.render("2. Skill", True, (200,200,200)),(0,screen_height-75))
        window.blit(font.render("3. Item", True, (200,200,200)),(0,screen_height-50))
        window.blit(font.render("4. Run", True, (200,200,200)),(0,screen_height-25))

        for i in range(0,4):
            window.blit(font.render(party[i].name, True, (0,200,0)),(250,screen_height-100+i*25))
            window.blit(font.render(f"HP  {party[i].hp}/{party[i].hp+party[i].taken_dmg}", True, (0,200,0)),(450,screen_height-100+i*25))
            window.blit(font.render(f"MP  {party[i].mp}/{party[i].mp+party[i].used_mp}", True, (0,200,0)),(700,screen_height-100+i*25))
            window.blit(font.render(f"LVL  {party[i].level[0]}/10", True, (0,200,0)),(900,screen_height-100+i*25))
            #window.blit(font.render(f"ATK  {party[i].atk}", True, (0,200,0)),(900,screen_height-100+i*25))

    if setting == "choose_skill":
        counter = 0
        for skill in character.skills:
            if counter < 4:
                window.blit(font.render(f"{counter+1}. {skill.name}  ({skill.cost} MP)", True, (200,200,200)),(0,screen_height-100+counter*25))
            else:
                window.blit(font.render(f"{counter+1}. {skill.name}  ({skill.cost} MP)", True, (200,200,200)),(300,screen_height-200+counter*25))
            counter += 1
    

    pygame.display.flip()


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
                                    if skill.buff == 0:
                                        #target = choose_action("battle")
                                        skill.activate(character,monster)
                                    else:
                                        if skill in active_skills:
                                            skill.deactivate(party,monster)
                                            active_skills.remove(skill)
                                        skill.activate(character,character)
                                        skill.user = character.name
                                        active_skills.append(skill)
                                else:
                                    if skill.buff == 0:
                                        skill.activate(character,monster)
                                    else:
                                        if skill in active_skills:
                                            skill.deactivate(party,monster)
                                            active_skills.remove(skill)
                                        for party_member in party:
                                            skill.activate(character,party_member)
                                        active_skills.append(skill)
                                break

            if monster.alive == False:
                for skill in active_skills:
                    skill.deactivate(party,monster)
                return
        while True:
            target = randint(0,3)
            if party[target].alive:
                break
        monster.attack(party[target],0)