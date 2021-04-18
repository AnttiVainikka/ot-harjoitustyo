# pylint: disable=no-member
import pygame
pygame.init()
from Classes.character import Character

def move(character,monsters :list):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character.move_left()
            if event.key == pygame.K_RIGHT:
                character.move_right()
            if event.key == pygame.K_UP:
                character.move_up()
            if event.key == pygame.K_DOWN:
                character.move_down()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character.stop_left()
            if event.key == pygame.K_RIGHT:
                character.stop_right()
            if event.key == pygame.K_UP:
                character.stop_up()
            if event.key == pygame.K_DOWN:
                character.stop_down()  