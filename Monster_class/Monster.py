from dataclasses import dataclass
import random

import Effect


@dataclass
class Monster_stat:
    effect_list = []

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
        print(f"The {self.name} attacked !")
        for i in range(0, len(self.effect_list)):
            effect = self.effect_list[i]
            if effect.effect_type == "stun":
                dmg = 0
                print("The monster is stunned he can't do any damage !")
                effect.turn_left -= 1
                if effect.turn_left == 0:
                    self.effect_list.remove(self.effect_list[i])
            if effect.effect_type == "accuracy":
                rand = random.randrange(100)
                if rand < 40:
                    dmg = 0
                    print("The monster can't see ! He can't do any damage !")
                effect.turn_left -= 1
                if effect.turn_left == 0:
                    self.effect_list.remove(self.effect_list[i])

        return dmg

    def dmg_taken(self, dmg):
        additional_dmg = 0
        poisoned = False
        for i in range(0, len(self.effect_list)):
            effect = self.effect_list[i]
            if effect.effect_type == "poison":
                poisoned = True
                additional_dmg += effect.effect
                effect.turn_left -= 1
                if effect.turn_left == 0:
                    self.effect_list.remove(self.effect_list[i])
        if poisoned:
            print(f"The monster is poisoned he took {additional_dmg} additional damage")
        dmg_taken = dmg + additional_dmg
        return dmg_taken

    def receive_effect(self, effect_type, effect, turn):
        effect = Effect.Effect(effect_type, effect, turn)
        self.effect_list.append(effect)
        print(f"You inflicter the effect : {effect_type}")

    def showStat(self):
        print(f"name : {self.name} / atk : {self.atk} / hp : {self.hp} / mana : {self.mana} / speed : {self.speed}")