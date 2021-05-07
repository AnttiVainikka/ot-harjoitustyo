"""importing pygame"""
import pygame
from StartGame.map import generate_map
from StartGame.characters import choose_party
from StartGame.characters import generate_monsters
from UI.render import render_start
from UI.render import render_map_selection
from UI.action import choose_action
pygame.display.set_caption("Dungeon Crawler")


class StartGame():
    """Lets the player choose their party and a map to play in and activates the starting area."""
    def __init__(self):
        self.party = []
        self.monsters = []
        render_map_selection()
        while True:
            pick = choose_action("Pick map")
            if pick == 1 or pick == 2:
                break
        self.map = generate_map(pick)
        self.start = self.map[0]
        self.boss = self.map[1]
        choose_party(self.party)
        generate_monsters(self.monsters)
        render_start(self.boss.name)
        self.start.activate(self.party, self.monsters, self.boss)

if __name__ == "__main__":
    StartGame()
