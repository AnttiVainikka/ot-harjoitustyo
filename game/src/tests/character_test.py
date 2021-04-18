import unittest
from Classes.character import Character

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character("Archer","sprite","sprite")
        self.character.level_up(1)

    def test_take_dmg_works(self):
        self.character.take_dmg(40)
        self.assertEqual(self.character.hp,40)
        self.assertEqual(self.character.taken_dmg,40)
        self.character.take_dmg(80)
        self.assertEqual(self.character.hp,0)
        self.assertEqual(self.character.taken_dmg,80)
        self.assertEqual(self.character.alive,False)

    def test_give_exp_works(self):
        self.character.give_exp(300)
        self.assertEqual(self.character.level,[3,50,200])
        self.character.level = [10,0,550]
        self.character.give_exp(800)
        self.assertEqual(self.character.level,[10,0,550])

    def test_reseting_health_works(self):
        self.character.take_dmg(40)
        self.character.reset_health()
        self.assertEqual(self.character.hp,80)
        self.assertEqual(self.character.taken_dmg,0)
