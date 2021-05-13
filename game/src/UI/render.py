import pygame
# pylint: disable=no-member
pygame.init()
screen_width = pygame.image.load("src/Sprites/background_full.png").get_width()
screen_height = pygame.image.load("src/Sprites/background_full.png").get_height()
window = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont("Arial", 25)
medium_font = pygame.font.SysFont("Arial", 50)
big_font = pygame.font.SysFont("Arial", 100)

def render_area(party,monsters,direction,countdown,area,boss):
    window.fill((0,0,0))
    window.blit(area.background,(0,0))
    for monster in monsters:
        window.blit(monster.over_sprite, (monster.x, monster.y))
    window.blit(party[0].over_sprite[party[0].direction][countdown],(party[0].x,party[0].y))
    if area.boss:
        window.blit(boss.over_sprite, (boss.x, boss.y))
    pygame.display.flip()

def render_character_screen(left):
    """Renders the screen where the player chooses their characters."""
    window.fill((0, 0, 0))
    counter = 0
    length = medium_font.size("Choose your characters")[0]
    window.blit(medium_font.render("Choose your characters",
    True, (200, 0, 0)), (screen_width/2-length/2,10))
    for character in left:
        if counter < 3:
            window.blit(font.render(f"{counter+1}. {character.name}",
            True, (200, 0, 0)), (20+200*counter, 250))
            window.blit(character.sprite,(20+200*counter,280))
        else:
            window.blit(font.render(f"{counter+1}. {character.name}",
            True, (200, 0, 0)), (20+200*counter-600, 550))
            window.blit(character.sprite,(20+200*counter-600,580))
        counter += 1
    pygame.display.flip()

def render_start(boss):
    window.fill((0, 0, 0))
    length = big_font.size("Find and kill the")[0]
    window.blit(big_font.render("Find and kill the",
    True, (200, 0, 0)), (screen_width/2-length/2,300))
    length = big_font.size(boss)[0]
    window.blit(big_font.render(boss,
    True, (200, 0, 0)), (screen_width/2-length/2,425))
    pygame.display.flip()
    pygame.time.wait(3000)

def render_map_selection():
    """Renders the screen where the player chooses the map they want to play in."""
    window.fill((0, 0, 0))
    length = big_font.size("Choose your map")[0]
    window.blit(big_font.render("Choose your map",
    True, (200, 0, 0)), (screen_width/2-length/2,10))
    window.blit(medium_font.render("1. Necromancer's Palace",
    True, (200, 0 ,0)), (50, 250))
    window.blit(medium_font.render("2. Dragon's Lair",
    True, (200, 0 ,0)), (50, 350))
    pygame.display.flip()

def render_game_over(setting):
    """Renders the game over screen."""
    window.fill((0, 0, 0))
    if setting == "victory":
        window.blit(big_font.render("You Have Conquered",
        True, (200, 0, 0)), (50, 100))
        window.blit(big_font.render("       the Dungeon",
        True, (200, 0, 0)), (50, 200))
        window.blit(font.render("Credits:",
        True,(200,200,200)),(10,screen_height-120))
        window.blit(font.render("monster design credits: Stephen 'Redshrike' Challener, hosted by OpenGameArt.org",
        True,(200,200,200)),(10,screen_height-90))
        window.blit(font.render("main character overhead sprite credits: ArMM1998, hosted by OpenGameArt.org",
        True,(200,200,200)),(10,screen_height-60))
        window.blit(font.render("character sprite credits: wulax, hosted by OpenGameArt.org",
        True,(200,200,200)),(10,screen_height-30))
    if setting == "defeat":
        length = big_font.size("Game Over")[0]
        window.blit(big_font.render("Game Over",
        True, (200, 0, 0)), (screen_width/2-length/2, 100))
    pygame.display.flip()


def render_battle(party,monsters,character,setting):
    """Renders the battle screen based on what the setting is."""
    window.fill((0, 0, 0))
    window.blit(font.render(character.name,
    True, (200,200,200)),(0,screen_height-125))
    counter = 0
    length = 300
    for monster in monsters:
        if monster.alive:
            window.blit(font.render(f"{monster.name}:   {monster.hp}/{monster.hp+monster.taken_dmg}",
            True, (200, 0, 0)), (20, counter*30))
            window.blit(monster.sprite,(screen_width-monster.sprite.get_width()-10,length))
        if setting == "choose_target_enemy" and monster.alive:
            window.blit(font.render(f"{counter+1}.",
            True, (200,200,200)),(screen_width-monster.sprite.get_width()-20,length))
            window.blit(font.render("R to return", True, (200,200,200)),(150,screen_height-125))
        counter += 1
        length += monster.sprite.get_height() + 30

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
    """Renders the descriptions of the characters skills or the items held by the party."""
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

def render_action(action,time):
    length = medium_font.size(action)[0]
    window.blit(medium_font.render(action,
    True, (200,0,0)),(screen_width/2-length/2,100))
    pygame.display.flip()
    pygame.time.wait(time)
