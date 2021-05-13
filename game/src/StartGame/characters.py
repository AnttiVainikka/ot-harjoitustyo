import pygame
from Classes.character import Character
from Classes.monster import Monster
from Classes.items import Item
from UI.action import choose_action
from UI.render import render_character_screen

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
    give_items(main_character)

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
    #for character in party:
    #    character.give_exp(9001)

def generate_monsters(monsters :list):
    """Adds monsters to the monster-list"""
    sprite = pygame.image.load("src/Sprites/demon.png")
    demon = Character("Demon Assassin", sprite, sprite)
    demon2 = Character("Demon Assassin", sprite, sprite)

    sprite = pygame.image.load("src/Sprites/eyeball.png")
    beholder = Character("Beholder", sprite, sprite)
    beholder2 = Character("Beholder", sprite, sprite)

    sprite = pygame.image.load("src/Sprites/goblin.png")
    goblin = Character("Goblin Soldier", sprite, sprite)
    goblin2 = Character("Goblin Soldier", sprite, sprite)

    sprite = pygame.image.load("src/Sprites/skeleton.png")
    skeleton = Character("Skeleton Warrior", sprite, sprite)
    skeleton2 = Character("Skeleton Warrior", sprite, sprite)

    sprite = pygame.image.load("src/Sprites/warlock.png")
    warlock = Character("Warlock", sprite, sprite)
    warlock2 = Character("Warlock", sprite, sprite)

    sprite = pygame.image.load("src/Sprites/dragonling.png")
    dragonling = Character("Dragonling", sprite, sprite)
    dragonling2 = Character("Dragonling", sprite, sprite)

    monsters.append(Monster([demon,beholder],4))
    monsters.append(Monster([demon,demon2],5))
    monsters.append(Monster([demon],6))
    monsters.append(Monster([demon,warlock,goblin,beholder],2))
    monsters.append(Monster([beholder,warlock,warlock2,beholder2],2))
    monsters.append(Monster([skeleton,warlock,skeleton2],2))
    monsters.append(Monster([dragonling],5))
    monsters.append(Monster([dragonling,dragonling2],5))
    monsters.append(Monster([demon,dragonling],5))
    monsters.append(Monster([skeleton,warlock,goblin],3))
    monsters.append(Monster([goblin,beholder,goblin2],2))
    monsters.append(Monster([beholder,skeleton,warlock],2))
    for group in monsters:
        for monster in group.monsters:
            monster.monster = True

def give_items(character):
    """Gives the main character the starting items."""
    character.items.append(Item("Potion",9))
    character.items.append(Item("High Potion",6))
    character.items.append(Item("X Potion",3))
    character.items.append(Item("Ether",6))
    character.items.append(Item("High Ether",4))
    character.items.append(Item("X Ether",2))
    character.items.append(Item("Mega Potion",3))
    character.items.append(Item("Full Heal",1))
    character.items.append(Item("Balm of Life",3))
