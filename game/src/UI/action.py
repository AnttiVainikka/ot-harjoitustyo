# pylint: disable=no-member
import pygame
pygame.init()
def choose_action(setting):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    return 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    return 3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_4:
                    return 4
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_5:
                    return 5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_6:
                    return 6
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_7:
                    return 7
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    return 8
            if setting == "choose skill" or setting == "choose target":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return 0