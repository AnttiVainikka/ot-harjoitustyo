import pygame
from Classes.character import Character
from UI.action import choose_action
from StartGame.render import render_character_screen

def choose_party(party :list):
    """Let's the player choose their party"""
    walking_left = [pygame.image.load("src/Sprites/stand_left.png")]
    walking_right = [pygame.image.load("src/Sprites/stand_right.png")]
    walking_top = [pygame.image.load("src/Sprites/stand_top.png")]
    walking_down = [pygame.image.load("src/Sprites/stand_bot.png")]

    for _ in range(7):
        walking_left.append(pygame.image.load("src/Sprites/step_left.png"))
        walking_right.append(pygame.image.load("src/Sprites/step_right.png"))
        walking_top.append(pygame.image.load("src/Sprites/step_top.png"))
        walking_down.append(pygame.image.load("src/Sprites/step_bot.png"))
    for _ in range(7):
        walking_left.append(pygame.image.load("src/Sprites/stand_left.png"))
        walking_right.append(pygame.image.load("src/Sprites/stand_right.png"))
        walking_top.append(pygame.image.load("src/Sprites/stand_top.png"))
        walking_down.append(pygame.image.load("src/Sprites/stand_bot.png"))
    for _ in range(7):
        walking_left.append(pygame.image.load("src/Sprites/step_left2.png"))
        walking_right.append(pygame.image.load("src/Sprites/step_right2.png"))
        walking_top.append(pygame.image.load("src/Sprites/step_top2.png"))
        walking_down.append(pygame.image.load("src/Sprites/step_bot2.png"))
    for _ in range(7):
        walking_left.append(pygame.image.load("src/Sprites/stand_left.png"))
        walking_right.append(pygame.image.load("src/Sprites/stand_right.png"))
        walking_top.append(pygame.image.load("src/Sprites/stand_top.png"))
        walking_down.append(pygame.image.load("src/Sprites/stand_bot.png"))

    walking_animation = [walking_left, walking_right, walking_top, walking_down]
    sprite = pygame.image.load("src/Sprites/main_character.png")

    main_character = Character("Leon", sprite, walking_animation)

    sprite = pygame.image.load("src/Sprites/knight.png")
    knight = Character("Knight", sprite, sprite)

    sprite = pygame.image.load("src/Sprites/archer.png")
    archer = Character("Archer", sprite, sprite)

    sprite = pygame.image.load("src/Sprites/wizard.png")
    wizard = Character("Wizard", sprite, sprite)

    sprite = pygame.image.load("src/Sprites/assassin.png")
    assassin = Character("Assassin", sprite, sprite)

    sprite = pygame.image.load("src/Sprites/monk.png")
    monk = Character("Monk", sprite, sprite)

    main_character.choose_character(party)
    left = [assassin,archer,knight,monk,wizard]
    while len(party) < 4:
        render_character_screen(left)
        while True:
            choice = choose_action("party")
            if choice <= len(left):
                break
        left[choice-1].choose_character(party)
        left.remove(left[choice-1])

    for character in party:
        character.give_exp(9001)

def generate_monsters(monsters :list):
    """Adds monsters to the monster-list"""
    sprite = pygame.image.load("src/Sprites/demon.png")
    monster1 = Character("Demon Assassin", sprite, sprite)
    monster1.speed_x = 4
    monster1.speed_y = 4

    sprite = pygame.image.load("src/Sprites/eyeball.png")
    monster2 = Character("Beholder", sprite, sprite)
    monster2.speed_x = 2
    monster2.speed_y = 2

    sprite = pygame.image.load("src/Sprites/goblin.png")
    monster3 = Character("Goblin Soldier", sprite, sprite)
    monster3.speed_x = 3
    monster3.speed_y = 3

    sprite = pygame.image.load("src/Sprites/skeleton.png")
    monster4 = Character("Skeleton Warrior", sprite, sprite)
    monster4.speed_x = 2
    monster4.speed_y = 2

    sprite = pygame.image.load("src/Sprites/warlock.png")
    monster5 = Character("Warlock", sprite, sprite)
    monster5.speed_x = 2
    monster5.speed_y = 2

    sprite = pygame.image.load("src/Sprites/dragonling.png")
    monster6 = Character("Dragonling", sprite, sprite)
    monster6.speed_x = 3
    monster6.speed_y = 3

    monsters.append(monster1)
    monsters.append(monster2)
    monsters.append(monster3)
    monsters.append(monster4)
    monsters.append(monster5)
    monsters.append(monster6)
    for character in monsters:
        character.give_exp(9001)
