"""importing pygame"""
import pygame
from StartGame.map import generate_map
from StartGame.characters import choose_party
from StartGame.characters import generate_monsters
pygame.display.set_caption("Dungeon Crawler")


class StartGame():
    """A Class for starting the game"""
    def __init__(self):
        self.party = []
        self.monsters = []
        self.map = generate_map(1)
        self.start = self.map[0]
        self.boss = self.map[1]
        choose_party(self.party)
        generate_monsters(self.monsters)

        self.start.activate(self.party, self.monsters, self.boss)


StartGame()

# monster design credits: Stephen "Redshrike" Challener, hosted by OpenGameArt.org
# main character overhead sprite credits: ArMM1998, hosted by OpenGameArt.org
# character sprite credits: wulax, hosted by OpenGameArt.org
