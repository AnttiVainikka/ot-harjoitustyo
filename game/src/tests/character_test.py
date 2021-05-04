import unittest
from Classes.character import Character
from Classes.skills import Skill

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character("Archer","sprite","sprite")
        self.character.hp = 80
        self.character.mp = 20
        self.character.atk = 40
        self.character.df = 40
        self.character.mdef = 20

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
        self.character.give_exp(100)
        self.assertEqual(self.character.level,[3,150,200])
        self.character.give_exp(9001)
        self.assertEqual(self.character.level,[10,6701,550])
        self.character.give_exp(800)
        self.assertEqual(self.character.level,[10,6701,550])

    def test_reseting_health_works(self):
        self.character.take_dmg(40)
        self.character.reset_health()
        self.assertEqual(self.character.hp,80)
        self.assertEqual(self.character.taken_dmg,0)

    def test_attacking_works(self):
        self.character.attack(self.character,0)
        self.assertEqual(self.character.hp,54)
        fireball = Skill("Fireball")
        self.character.attack(self.character,fireball)
        self.assertEqual(self.character.hp,1)
        self.character.reset_health()
        strike = Skill("Power Strike")
        self.character.attack(self.character,strike)
        self.assertEqual(self.character.hp,34)
        arrow = Skill("Piercing Arrow")
        self.character.attack(self.character,arrow)
        self.assertEqual(self.character.hp,0)
        self.character.hp = 500
        edge = Skill("Double Edge")
        self.character.attack(self.character,edge)
        self.assertEqual(self.character.hp,146)
        self.character.atk = 0
        self.character.attack(self.character,0)
        self.assertEqual(self.character.hp,145)

    def test_leveling_up_works(self):
        self.character.take_dmg(40)
        self.character.level_up(10)
        self.assertEqual(self.character.taken_dmg,0)
        self.assertGreater(self.character.hp,80)

    def test_choosing_character_works(self):
        party = []
        self.character.hp = 1
        self.character.choose_character(party)
        self.assertEqual(self.character,party[0])
        self.assertGreater(self.character.hp,1)

    def test_recovering_works(self):
        self.character.take_dmg(40)
        self.character.recover(30,"hp")
        self.assertEqual(self.character.hp,70)
        self.assertEqual(self.character.taken_dmg,10)
        self.character.recover(30,"hp")
        self.assertEqual(self.character.hp,80)
        self.assertEqual(self.character.taken_dmg,0)

        self.character.mp -= 15
        self.character.used_mp += 15
        self.character.recover(10,"mp")
        self.assertEqual(self.character.mp,15)
        self.assertEqual(self.character.used_mp,5)
        self.character.recover(10,"mp")
        self.assertEqual(self.character.mp,20)
        self.assertEqual(self.character.used_mp,0)

    def test_moving_works(self):
        self.character.move_down()
        self.assertEqual(self.character.down,True)
        self.character.stop_down()
        self.assertEqual(self.character.down,False)

        self.character.move_right()
        self.assertEqual(self.character.right,True)
        self.character.stop_right()
        self.assertEqual(self.character.right,False)

        self.character.move_left()
        self.assertEqual(self.character.left,True)
        self.character.stop_left()
        self.assertEqual(self.character.left,False)

        self.character.move_up()
        self.assertEqual(self.character.up,True)
        self.character.stop_up()
        self.assertEqual(self.character.up,False)
