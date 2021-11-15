import dataclasses
import random

class HeroStats:
    skill_list = list
    protection = int

    def __init__(self, name, xp=None, level=None):
        if xp and level:
            self.name = name
            self.xp = xp
            self.level = level
            self.protection = 0
            self.stun = False
        else:
            self.name = name
            self.atk = 15
            self.hp = 100
            self.mana = 100
            self.speed = 30
            self.xp = 0
            self.level = 1
            self.protection = 0
            self.stun = False

    def dmg_taken(self, dmg):
        dmg_taken = dmg - (dmg * self.protection / 100)
        if self.protection != 0:
            print(f"You reduced the damage of {self.protection} %")
            self.protection = 0
        return dmg_taken


    def dmg_done(self):
        rand = (random.randrange(40) - 20)
        dmg = int((self.atk * rand / 100) + self.atk)
        return dmg

    def show_skill_list(self):
        return self.skill_list

    def add_skill(self, skill):
        self.skill_list.append(skill)

    def show_xp(self):
        return self.xp

    def xp_up(self, xp_received):
        self.xp = xp_received + self.xp

    def show_level(self):
        return self.level

    def level_up(self):
        self.level += 1
        self.xp = 0


    def showStat(self):
        print(f"name : {self.name} / atk : {self.atk} / hp : {self.hp} / mana : {self.mana} / speed : {self.speed}")
