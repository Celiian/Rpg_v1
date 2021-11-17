import os
from os import path

from Core import Functions
from Hero_class import Hero, Paladin, Assasin, Mage
import pickle


def load(list_file):
    file = list_file[0]
    inventoryFile = list_file[1]
    pickle_in = open(file, "rb")
    dict_load = pickle.load(pickle_in)
    dict_player = dict_load["player"]
    dict_arena = dict_load["arena"]
    pickle_in.close()

    inventoryFile = open(inventoryFile, 'rb')
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


def save(dict_save):
    player = dict_save["player"]
    shadow_player = dict_save["shadow_player"]
    arena = dict_save["arena"]
    actual_arena = dict_save["actual_arena"]
    monster_kill = dict_save["monster_kill"]
    list_file = dict_save["list_file"]
    file = list_file[0]
    inventoryFile = list_file[1]
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
    file_ = open(inventoryFile, 'wb')
    pickle.dump(inventoryObject, file_)
    file_.close()
    pickle_out = open(file, "wb")
    pickle.dump(dict_save_info, pickle_out)
    pickle_out.close()


def save_choose(player, shadow_player, arena, actual_arena, monster_kill):
    dict_save = {
        "player": player,
        "shadow_player": shadow_player,
        "arena": arena,
        "actual_arena": actual_arena,
        "monster_kill": monster_kill,
    }

    file1 = 'Saves/save1'
    inventoryFile1 = 'Saves/inventory1.obj'
    file2 = 'Saves/save2'
    inventoryFile2 = 'Saves/inventory2.obj'
    file3 = 'Saves/save3'
    inventoryFile3 = 'Saves/inventory3.obj'
    file1_empty = True
    file2_empty = True
    file3_empty = True
    choiceDone = False
    while not choiceDone:
        try:
            if os.path.exists(file1):
                file1_empty = Functions.file_is_empty(file1)
                if file1_empty:
                    print("1 - [EMPTY]")
                else:
                    print("1 - [USED]")
            else:
                print("1 - [EMPTY]")
            if os.path.exists(file2):
                file2_empty = Functions.file_is_empty(file2)
                if file2_empty:
                    print("2 - [EMPTY]")
                else:
                    print("2 - [USED]")
            else:
                print("2 - [EMPTY]")
            if os.path.exists(file3):
                file3_empty = Functions.file_is_empty(file3)
                if file3_empty:
                    print("3 - [EMPTY]")
                else:
                    print("3 - [USED]")
            else:
                print("3 - [EMPTY]")

            print("Which slot do you want to use ?")
            choice = int(input())
            choiceDone = True
        except ValueError as e:
            print("Please choose a valid option")
            pass
        choiceDone2 = False
    while not choiceDone2:
        if choice == 1:
            if file1_empty:
                list_file = [file1, inventoryFile1]
                dict_save["list_file"] = list_file
                choiceDone2 = True
            else:
                print("Do you really want to erase data ? (y/n)")
                choice2 = input()
                if choice2 == "y":
                    list_file = [file1, inventoryFile1]
                    dict_save["list_file"] = list_file
                    choiceDone2 = True
                else:
                    choiceDone2 = True
        if choice == 2:
            if file2_empty:
                list_file = [file2, inventoryFile2]
                dict_save["list_file"] = list_file
                choiceDone2 = True
            else:
                print("Do you really want to erase data ? (y/n)")
                choice2 = input()
                if choice2 == "y":
                    list_file = [file2, inventoryFile2]
                    dict_save["list_file"] = list_file
                    choiceDone2 = True
                else:
                    choiceDone2 = True
        if choice == 3:
            if file3_empty:
                list_file = [file3, inventoryFile3]
                dict_save["list_file"] = list_file
                choiceDone2 = True
            else:
                print("Do you really want to erase data ? (y/n)")
                choice2 = input()
                if choice2 == "y":
                    list_file = [file3, inventoryFile3]
                    dict_save["list_file"] = list_file
                    choiceDone2 = True
                else:
                    choiceDone2 = True

    save(dict_save)


def load_choose():
    file1 = 'Saves/save1'
    inventoryFile1 = 'Saves/inventory1.obj'
    file2 = 'Saves/save2'
    inventoryFile2 = 'Saves/inventory2.obj'
    file3 = 'Saves/save3'
    inventoryFile3 = 'Saves/inventory3.obj'
    file1_empty = True
    file2_empty = True
    file3_empty = True
    choiceDone = False
    while not choiceDone:
        try:
            if os.path.exists(file1):
                file1_empty = Functions.file_is_empty(file1)
                if file1_empty:
                    print("1 - [EMPTY]")
                else:
                    print("1 - [USED]")
            else:
                print("1 - [EMPTY]")
            if os.path.exists(file2):
                file2_empty = Functions.file_is_empty(file2)
                if file2_empty:
                    print("2 - [EMPTY]")
                else:
                    print("2 - [USED]")
            else:
                print("2 - [EMPTY]")
            if os.path.exists(file3):
                file3_empty = Functions.file_is_empty(file3)
                if file3_empty:
                    print("3 - [EMPTY]")
                else:
                    print("3 - [USED]")
            else:
                print("3 - [EMPTY]")
            print("0 - Cancel")

            print("Which slot do you want to use ?")
            choice = int(input())
            choiceDone = True
        except ValueError as e:
            print("Please choose a valid option")
            pass
        choiceDone2 = False
        while not choiceDone2:
            if choice == 1:
                list_file = [file1, inventoryFile1]
                choiceDone2 = True
            elif choice == 2:
                list_file = [file2, inventoryFile2]
                choiceDone2 = True
            elif choice == 3:
                list_file = [file3, inventoryFile3]
                choiceDone2 = True
            elif choice == 0:
                return 0
            else:
                print("Please choose a valid option")

    dict_info = load(list_file)
    return dict_info
