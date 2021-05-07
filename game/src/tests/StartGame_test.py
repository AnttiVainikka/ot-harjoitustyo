import unittest
from StartGame.map import generate_map
from StartGame.characters import generate_monsters
from StartGame.characters import give_items
from Classes.character import Character

class TestStartGame(unittest.TestCase):
    def setUp(self):
        self.map = None
        self.archer = Character("Archer","sprite","sprite")

    def test_generate_map_return_correctly(self):
        self.map = generate_map(1)
        self.assertEqual(self.map[0].start,True)
        self.assertEqual(self.map[1].boss,True)
        self.map = None
        self.map = generate_map(2)
        self.assertEqual(self.map[0].start,True)
        self.assertEqual(self.map[1].boss,True)

    def test_generate_monsters_generates_monsters(self):
        monsters = []
        generate_monsters(monsters)
        correct = True
        for group in monsters:
            for monster in group.monsters:
                if monster.monster is False:
                    correct = False
        self.assertEqual(correct,True)

    def test_give_items_gives_items(self):
        give_items(self.archer)
        self.assertGreater(len(self.archer.items),0)
