from Core import Functions
from Hero_class import Hero, Paladin, Assasin, Mage
import pickle


def load():
    pickle_in = open("Saves/save", "rb")
    dict_load = pickle.load(pickle_in)
    dict_player = dict_load["player"]
    dict_arena = dict_load["arena"]
    pickle_in.close()

    inventoryFile = open('Saves/inventory.obj', 'rb')
    inventory = pickle.load(inventoryFile)
    inventoryFile.close()

    name = dict_player["name"]
    class_name = dict_player["class"]
    atk = dict_player["atk"]
    max_hp = dict_player["max_hp"]
    actual_hp = dict_player["actual_hp"]
    max_mana = dict_player["max_mana"]
    actual_mana = dict_player["actual_mana"]
    speed = dict_player["speed"]
    xp = dict_player["xp"]
    level = dict_player["level"]
    arena_id = dict_arena["id"]
    monster_needed = dict_arena["monster_needed"]
    monster_kill = dict_arena["monster_kill"]
    skills = dict_player["skills"]
    money = dict_player["money"]

    if class_name == "assassin":
        player = Assasin.AssassinStat(name, atk, max_hp, max_mana, speed, xp, level, skills, money, inventory)
        shadow_player = Assasin.AssassinStat(name, atk, actual_hp, actual_mana, speed, xp, level, skills, money,
                                             inventory)
    if class_name == "mage":
        player = Mage.MageStat(name, atk, max_hp, max_mana, speed, xp, level, skills, money, inventory)
        shadow_player = Mage.MageStat(name, atk, actual_hp, actual_mana, speed, xp, level, skills, money, inventory)
    if class_name == "paladin":
        player = Paladin.PaladinStat(name, atk, max_hp, max_mana, speed, xp, level, skills, money, inventory)
        shadow_player = Paladin.PaladinStat(name, atk, actual_hp, actual_mana, speed, xp, level, skills, money,
                                            inventory)

    dict_info = {
        "player": player,
        "shadow_player": shadow_player,
        "actual_arena": arena_id,
        "monster_needed": monster_needed,
        "monster_kill": monster_kill,
    }
    return dict_info


def save(player, shadow_player, arena, actual_arena, monster_kill):
    dict_save_info = {
        "player": {
            "name": player.name,
            "class": player.class_name,
            "level": player.level,
            "xp": player.xp,
            "speed": player.speed,
            "atk": player.atk,
            "max_hp": player.hp,
            "max_mana": player.mana,
            "actual_hp": shadow_player.hp,
            "actual_mana": shadow_player.mana,
            "skills": player.skill_list,
            "money": player.money,
        },
        "arena": {
            "id": actual_arena,
            "monster_needed": int(arena['monster_needed']),
            "monster_kill": monster_kill,
        }
    }

    inventoryObject = player.inventory
    inventoryObject.show_potions()
    file = open('Saves/inventory.obj', 'wb')
    pickle.dump(inventoryObject, file)
    file.close()

    pickle_out = open("Saves/save", "wb")
    pickle.dump(dict_save_info, pickle_out)
    pickle_out.close()
