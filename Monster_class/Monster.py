from dataclasses import dataclass
import random

@dataclass
class Monster_stat:

    def __init__(self, name, atk, hp, mana, speed, type):
        self.name = name
        self.atk = atk
        self.hp = hp
        self.mana = mana
        self.speed = speed
        self.type = type

    def damage(self):
        rand = (random.randrange(40) - 20)
        dmg = int((self.atk * rand / 100) + self.atk)
        return dmg




    def showStat(self):
        print(f"name : {self.name} / atk : {self.atk} / hp : {self.hp} / mana : {self.mana} / speed : {self.speed}")