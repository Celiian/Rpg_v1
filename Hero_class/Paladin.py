from dataclasses import dataclass
from Hero_class.Hero import HeroStats


@dataclass
class PaladinStat(HeroStats):
    skill_list = []

    def __init__(self, name=None, atk=None, hp=None, mana=None, speed=None, xp=None, level=None, skill_list=None):
        if name is not None and atk is not None and hp is not None and mana is not None \
                and speed is not None and xp is not None and level is not None and skill_list is not None:
            super().__init__(name, xp, level)
            self.class_name = "paladin"
            self.atk = atk
            self.hp = hp
            self.mana = mana
            self.speed = speed
            self.skill_list = skill_list
        else :
            super().__init__(name)
            self.class_name = "paladin"
            self.atk = 17
            self.hp = 130
            self.mana = 120
            self.speed = 3




    def showStat(self):
        print(f"name : {self.name} / atk : {self.atk} / hp : {self.hp} / mana : {self.mana} / speed : {self.speed}")