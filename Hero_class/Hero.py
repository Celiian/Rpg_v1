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
            self.protection_turn = 0

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
            self.protection_turn = 0

    def dmg_taken(self, dmg):
        for i in range(0, len(self.effect_list)):
            effect = self.effect_list[i]
            if effect.effect_type == "restoration":
                self.hp += effect.effect
                print(f"You healed {effect.effect} hp")
                effect.turn_left -= 1
                if effect.turn_left == 0:
                    self.effect_list.remove(self.effect_list[i])

        dmg_taken = dmg - (dmg * self.protection / 100)
        if self.protection != 0:
            print(f"You reduced the damage of {self.protection} %")
            self.protection_turn -= 1
            if self.protection_turn == 0:
                self.protection = 0
        return dmg_taken

    def dmg_done(self):
        additional_damage = 0
        for i in range(0, len(self.effect_list)):
            effect = self.effect_list[i]
            if effect.effect_type == "atk_buff":
                additional_damage += effect.effect
                effect.turn_left -= 1
                if effect.turn_left == 0:
                    self.effect_list.remove(self.effect_list[i])
        if additional_damage != 0:
            print(f"You did {additional_damage} additional damage !")
        rand = (random.randrange(40) - 20)
        atk = self.atk + additional_damage
        dmg = int((atk * rand / 100) + atk)
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
