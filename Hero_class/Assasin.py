from dataclasses import dataclass
from Hero_class.Hero import HeroStats
import random
from Inventory import InventoryPlayer


@dataclass
class AssassinStat(HeroStats):
    skill_list = []

    def __init__(self, name=None, atk=25, hp=80, mana=70, speed=45, xp=0, level=1, skill_list=None,
                 money=0, inventory=None):
        print(inventory)
        super().__init__(name, xp, level)
        if skill_list is None:
            skill_list = []
        if inventory is None:
            inventory = InventoryPlayer.InventoryPlayer()
        self.skill_list = skill_list
        self.inventory = inventory
        self.class_name = "assassin"
        self.atk = atk
        self.hp = hp
        self.mana = mana
        self.speed = speed
        self.critical = 30
        self.dodge = 30
        self.skill_list = skill_list
        self.atk_boost = self.atk
        self.money = money

    def dmg_done(self):
        stun = False
        rand = (random.randrange(40) - 20)
        dmg = int((self.atk_boost * rand / 100) + self.atk_boost)
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
        else:
            print(self.name + " is stunned ! He can't do any damage")
            self.stun = False
            return 0

    def dmg_taken(self, dmg):
        damagetaken = dmg
        randNumber = random.randrange(100)
        dodge = randNumber
        if dodge < self.dodge:
            damagetaken = 0
            print("You dodged the attack !!")
            return damagetaken
        return dmg

    def showStat(self):
        print(f"name : {self.name} / atk : {self.atk} / hp : {self.hp} / mana : {self.mana} / speed : {self.speed} / "
              f"crit rate : {self.crit} / dodge rate : {self.dodge}")
