import unittest
from game import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character("Archer","sprite",[9,14,18,24,36,52,72,88,102,144],[4,9,15,21,30,36,50,66,84,112],[80,120,200,350,490,600,720,910,1080,1320])
    
    def test_take_dmg_works(self):
        self.character.take_dmg(40)
        self.assertEqual(self.character.hp[self.character.level[0]],40)
