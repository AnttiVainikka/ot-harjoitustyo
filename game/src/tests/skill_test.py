import unittest
from Classes.character import Character
from Classes.skills import Skill

class TestSkill(unittest.TestCase):
    def setUp(self):
        self.fireball = Skill("Fireball")
        self.fireball.multiplier = 2
        self.holy = Skill("Holy Light")
        self.holy.multiplier = 2
        self.atk = Skill("Raise Attack")
        self.atk.multiplier = 2
        self.df = Skill("Raise Defense")
        self.df.multiplier = 2
        self.mdef = Skill("Raise Magic Defense")
        self.mdef.multiplier = 2
        self.meditate = Skill("Meditate")
        self.meditate.multiplier = 1
        self.resurrect = Skill("Resurrect")
        self.poison = Skill("Poison")

        self.archer = Character("Archer","sprite","sprite")
        self.archer.atk = 40
        self.archer.df = 30
        self.archer.mdef = 30
        self.archer.hp = 400
        self.archer.mp = 50

    
    def test_attacking_skills_work(self):
        self.fireball.activate(self.archer,self.archer)
        self.assertEqual(self.archer.hp,330)

    def test_recovery_skills_work(self):
        self.archer.take_dmg(100)
        self.holy.activate(self.archer,self.archer)
        self.assertEqual(self.archer.hp,360)
        self.archer.used_mp = 50
        self.meditate.activate(self.archer,self.archer)
        self.assertEqual(self.archer.mp,100)

    def test_recovery_skills_work_with_all_stats(self):
        self.holy.stat = "attack"
        self.archer.take_dmg(100)
        self.holy.activate(self.archer,self.archer)
        self.assertEqual(self.archer.hp,380)

        self.holy.stat = "mdef"
        self.archer.take_dmg(80)
        self.holy.activate(self.archer,self.archer)
        self.assertEqual(self.archer.hp,360)

        self.holy.stat = "hp"
        self.archer.take_dmg(260)
        self.holy.activate(self.archer,self.archer)
        self.assertEqual(self.archer.hp,300)


    def test_resurrecting_skills_work(self):
        self.archer.alive = False
        self.resurrect.activate(self.archer,self.archer)
        self.assertEqual(self.archer.alive,True)

    def test_buffing_skills_work(self):
        self.atk.activate(self.archer,self.archer)
        #original attack at level 1 is 21
        self.assertEqual(self.archer.atk,82)
        self.atk.deactivate([self.archer])
        self.assertEqual(self.archer.atk,40)

        self.df.activate(self.archer,self.archer)
        #original defense at level 1 is 6
        self.assertEqual(self.archer.df,42)
        self.df.deactivate([self.archer])
        self.assertEqual(self.archer.df,30)

        self.mdef.activate(self.archer,self.archer)
        #original mdef at level 1 is 7
        self.assertEqual(self.archer.mdef,44)
        self.mdef.deactivate([self.archer])
        self.assertEqual(self.archer.mdef,30)

    def test_deactivating_single_target_skills_work(self):
        self.atk.aoe = 0
        self.atk.user = "Archer"
        self.atk.activate(self.archer,self.archer)
        self.atk.deactivate([self.archer])
        self.assertEqual(self.archer.atk,40)

        self.df.aoe = 0
        self.df.user = "Archer"
        self.df.activate(self.archer,self.archer)
        self.df.deactivate([self.archer])
        self.assertEqual(self.archer.df,30)

        self.mdef.aoe = 0
        self.mdef.user = "Archer"
        self.mdef.activate(self.archer,self.archer)
        self.mdef.deactivate([self.archer])
        self.assertEqual(self.archer.mdef,30)

    def test_poisoning_works(self):
        self.poison.activate(self.archer,self.archer)
        self.assertEqual(self.archer.status,["Poison",3])
        self.archer.boss = True
        self.archer.status = [None,0]
        self.poison.activate(self.archer,self.archer)
        self.assertEqual(self.archer.status,[None,0])
