from dataclasses import dataclass
from Hero_class.Hero import HeroStats
from Inventory import InventoryPlayer


@dataclass
class PaladinStat(HeroStats):
    skill_list = []

    def __init__(self, name=None, atk=17, hp=130, mana=120, speed=30, xp=0, level=1, skill_list=None, money=0, inventory=None):
        super().__init__(name, xp, level)
        if skill_list is None:
            skill_list = []
        if inventory is None:
            inventory = InventoryPlayer.InventoryPlayer()

        self.skill_list = skill_list
        self.inventory = inventory
        self.class_name = "paladin"
        self.atk = atk
        self.hp = hp
        self.mana = mana
        self.speed = speed
        self.skill_list = skill_list
        self.atk_boost = self.atk
        self.money = money



    def showStat(self):
        print(f"name : {self.name} / atk : {self.atk} / hp : {self.hp} / mana : {self.mana} / speed : {self.speed}")