import unittest
from game import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character("Test","sprite",
        [9,14,18,24,36,52,72,88,102,144],
        [4,9,15,21,30,36,50,66,84,112],
        [80,120,200,350,490,600,720,910,1080,1320])
    
    def test_take_dmg_works(self):
        self.character.take_dmg(40)
        self.assertEqual(self.character.hp[self.character.level[0]],40)
        self.assertEqual(self.character.taken_dmg,40)
        self.character.take_dmg(80)
        self.assertEqual(self.character.hp[self.character.level[0]],0)
        self.assertEqual(self.character.taken_dmg,80)
        self.assertEqual(self.character.alive,False)
    
    def test_give_exp_works(self):
        self.character.give_exp(300)
        self.assertEqual(self.character.level,[2,50,200])
        self.character.level = [9,0,550]
        self.character.give_exp(800)
        self.assertEqual(self.character.level,[9,0,550])

    def test_reseting_health_works(self):
        self.character.take_dmg(40)
        self.character.reset_health()
        self.assertEqual(self.character.hp[self.character.level[0]],80)
        self.assertEqual(self.character.taken_dmg,0)