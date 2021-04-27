import pygame
from Classes.character import Character
# pylint: disable=no-member
pygame.init()
screen_width = pygame.image.load("src/Sprites/background_full.png").get_width()
screen_height = pygame.image.load("src/Sprites/background_full.png").get_height()
window = pygame.display.set_mode((screen_width, screen_height)) 
font = pygame.font.SysFont("Arial", 25)
big_font = pygame.font.SysFont("Arial", 100)


def render_character_screen(left):
    window.fill((0, 0, 0))
    counter = 0
    for character in left:
        if counter < 3:
            window.blit(font.render(f"{counter+1}. {character.name}", True, (200, 0, 0)), (20+200*counter, 50))
            window.blit(character.sprite,(20+200*counter,80))
        else:
            window.blit(font.render(f"{counter+1}. {character.name}", True, (200, 0, 0)), (20+200*counter-600, 350))
            window.blit(character.sprite,(20+200*counter-600,380))            
        counter += 1
    pygame.display.flip()

def render_game_over(setting):
    window.fill((0, 0, 0))
    if setting == "victory":
        window.blit(big_font.render("You Have Conquered", True, (200, 0, 0)), (50, 100))
        window.blit(big_font.render("       the Dungeon", True, (200, 0, 0)), (50, 200))
    if setting == "defeat":
        window.blit(big_font.render("Game Over", True, (200, 0, 0)), (100, 100))
    pygame.display.flip()


def render_battle(party,monster,character,setting):
    window.fill((0, 0, 0))
    window.blit(font.render(f"{monster.name}:   {monster.hp}/{monster.hp+monster.taken_dmg}", True, (200, 0, 0)), (20, 0))
    window.blit(font.render(character.name, True, (200,200,200)),(0,screen_height-125))
    window.blit(monster.sprite,(screen_width-monster.sprite.get_width()-10,screen_height/2-monster.sprite.get_height()/2+50))

    for i in range(0,4):
            window.blit(party[i].sprite,(i*10+10,300+i*100))

    if setting == "battle":
        window.blit(font.render("1. Attack", True, (200,200,200)),(0,screen_height-100))
        window.blit(font.render("2. Skill", True, (200,200,200)),(0,screen_height-75))
        window.blit(font.render("3. Item", True, (200,200,200)),(0,screen_height-50))
        window.blit(font.render("4. Run", True, (200,200,200)),(0,screen_height-25))

        for i in range(0,4):
            window.blit(font.render(party[i].name,
            True, (0,200,0)),(250,screen_height-100+i*25))

            window.blit(font.render(f"HP  {party[i].hp}/{party[i].hp+party[i].taken_dmg}",
            True, (0,200,0)),(450,screen_height-100+i*25))

            window.blit(font.render(f"MP  {party[i].mp}/{party[i].mp+party[i].used_mp}",
            True, (0,200,0)),(700,screen_height-100+i*25))

            window.blit(font.render(f"LVL  {party[i].level[0]}/10",
            True, (0,200,0)),(900,screen_height-100+i*25))

            #window.blit(font.render(f"ATK  {party[i].atk}",
            #True, (0,200,0)),(900,screen_height-100+i*25))

            #window.blit(font.render(f"DEF  {party[i].mdef}",
            #True, (0,200,0)),(900,screen_height-400+i*25))

    if setting == "choose_skill":
        counter = 0
        for skill in character.skills:
            if counter < 4:
                window.blit(font.render(f"{counter+1}. {skill.name}  ({skill.cost} MP)",
                True, (200,200,200)),(0,screen_height-100+counter*25))
            else:
                window.blit(font.render(f"{counter+1}. {skill.name}  ({skill.cost} MP)",
                True, (200,200,200)),(300,screen_height-200+counter*25))
            counter += 1
        window.blit(font.render("R to return", True, (200,200,200)),(150,screen_height-125))
        window.blit(font.render("D to see skill descriptions", True, (200,200,200)),(400,screen_height-125))

    if setting == "choose_item":
        counter = 0
        for item in party[0].items:
            if counter < 4:
                window.blit(font.render(f"{counter+1}. {item.name}  ({item.amount})",
                True, (200,200,200)),(0,screen_height-100+counter*25))
            elif counter < 8:
                window.blit(font.render(f"{counter+1}. {item.name}  ({item.amount})",
                True, (200,200,200)),(300,screen_height-200+counter*25))
            else:
                window.blit(font.render(f"{counter+1}. {item.name}  ({item.amount})",
                True, (200,200,200)),(600,screen_height-300+counter*25))
            counter += 1
        window.blit(font.render("R to return", True, (200,200,200)),(150,screen_height-125))
        window.blit(font.render("D to see item descriptions", True, (200,200,200)),(400,screen_height-125))

    if setting == "choose_target_ally":
        for i in range(0,4):
            window.blit(font.render(f"{i+1}.",
            True, (200,200,200)),(i*10+30+party[i].sprite.get_width(),300+i*100))
        window.blit(font.render("R to return", True, (200,200,200)),(150,screen_height-125))

    pygame.display.flip()


def render_info(skills):
    window.fill((0, 0, 0))
    counter = 0
    for skill in skills:
        if font.size(f"{skill.name}:  {skill.desc}")[0] > screen_width:
            window.blit(font.render(f"{skill.name}:  {skill.desc[:len(skill.desc)//2]}",
            True, (200,0,0)),(5,5+counter*50))
            window.blit(font.render(skill.desc[len(skill.desc)//2:],
            True, (200,0,0)),(5,35+counter*50))
            counter += 1
        else:
            window.blit(font.render(f"{skill.name}:  {skill.desc}",
            True, (200,0,0)),(5,5+counter*50))
        counter += 1
    window.blit(font.render("R to return", True, (200,200,200)),(150,screen_height-125))

    pygame.display.flip()
