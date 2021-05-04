import pygame
# pylint: disable=no-member
pygame.init()
from Classes.skills import Skill

class Monster():
    """Class for the monster groups roaming the areas."""
    def __init__(self,monsters,speed):
        self.monsters = monsters
        self.x = 100
        self.y = 100
        self.speed_x = speed
        self.speed_y = speed
        self.over_sprite = monsters[0].over_sprite

    def change_speed(self,cordinate):
        """Changes a monsters speed so they bounce off the walls."""
        if cordinate == "x":
            self.speed_x = -self.speed_x
        if cordinate == "y":
            self.speed_y = -self.speed_y
