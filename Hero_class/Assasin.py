from dataclasses import dataclass
from Hero_class.Hero import HeroStats
import random


@dataclass
class AssassinStat(HeroStats):
    skill_list = []

    def __init__(self, name=None, atk=None, hp=None, mana=None, speed=None, xp=None, level=None, skill_list=None):
        if name is not None and atk is not None and hp is not None and mana is not None\
                and speed is not None and xp is not None and level is not None and skill_list is not None:
            super().__init__(name, xp, level)
            self.class_name = "assassin"
            self.atk = atk
            self.hp = hp
            self.mana = mana
            self.speed = speed
            self.critical = 30
            self.dodge = 30
            self.skill_list = skill_list
        else:
            super().__init__(name)
            self.class_name = "assassin"
            self.atk = 25
            self.hp = 80
            self.mana = 70
            self.speed = 45
            self.critical = 30
            self.dodge = 30


    def dmg_done(self):
        stun = False
        rand = (random.randrange(40) - 20)
        dmg = int((self.atk * rand / 100) + self.atk)
        if not stun:
            randNumber = random.randrange(100)
            crit = randNumber
            crit = int(crit)
            if crit <= self.critical:
                damageDone = int(dmg * 2)
                print("You made a critical attack !!")
                return damageDone
            else:
                return dmg
        else :
            print(this.name + " is stunned ! He can't do any damage")
            self.stun = False
            return 0

    def dmg_taken(self, dmg):
        damagetaken = dmg
        randNumber = random.randrange(100)
        dodge = randNumber
        print(dodge)
        if dodge < self.dodge:
            damagetaken = 0
            print("You dodged the attack !!")
            return damagetaken
        return dmg






    def showStat(self):
        print(f"name : {self.name} / atk : {self.atk} / hp : {self.hp} / mana : {self.mana} / speed : {self.speed} / "
              f"crit rate : {self.crit} / dodge rate : {self.dodge}")