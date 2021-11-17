import dataclasses
import random
from Inventory import InventoryPlayer
import Effect

class HeroStats:
    skill_list = []
    protection = int
    effect_list = []

    def __init__(self, name, xp=None, level=None):
        self.inventory = InventoryPlayer.InventoryPlayer()
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
            self.atk_boost = self.atk


    def dmg_taken(self, dmg):
        dmg_taken = dmg - (dmg * self.protection / 100)
        if self.protection != 0:
            print(f"You reduced the damage of {self.protection} %")
            self.protection = 0
        return dmg_taken


    def dmg_done(self):
        self.atk_boost = self.atk
        for i in range(0, len(self.effect_list)-1):
            effect = self.effect_list[i]
            if effect.effect_type == "atk_buff":
                self.atk_boost += effect.effect
                effect.turn_left -= 1
                if effect.turn_left == 0:
                    self.effect_list.remove(self.effect_list[i])

        rand = (random.randrange(40) - 20)
        dmg = int((self.atk_boost * rand / 100) + self.atk_boost)
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

    def add_buff(self, buff, effect, turn):
        boost = Effect.Effect(buff, effect, turn)
        self.effect_list.append(boost)





    def showStat(self):
        print(f"name : {self.name} / atk : {self.atk} / hp : {self.hp} / mana : {self.mana} / speed : {self.speed}")

















