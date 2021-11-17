import math
import random
from os import listdir

import Dictionnary.Skill_dictionnary
import Monster_class.Monster
from Core import MessageFunctions
from Dictionnary import Monster_dictionnary, Potions
from Hero_class import Mage, Assasin, Paladin
from Inventory import InventoryPlayer, Item
import os

level_list = []
x = 0
for i in range(1, 30):
    x = int(math.log10(i) * 1000)
    level_list.append(x)


def file_is_empty(path):
    return os.stat(path).st_size == 0


def character_create():
    print("So.. Player... What's your name ?")

    name = input()

    print(f"{name} am I right ? (y / n)")
    choice = input()

    if choice == "n":
        while True:
            print("Please enter your name ")
            name = input()
            print(f"{name} am I right ? (y / n)")
            choice = input()
            if choice == "y":
                break

    print(f"Soooo {name}... Which class do you want ?")
    list_class()
    choiceHero = int(input())
    class_info(choiceHero)
    print("Do you want to choose this class ? (y / n)")
    choice = input()
    if choice == "n":
        while True:
            print("Please choose a class ")
            list_class()
            choiceHero = int(input())
            class_info(choiceHero)
            print("Do you want to choose this class ? (y / n)")
            choice = input()
            if choice == "y":
                break

    if choiceHero == 1:
        player = Assasin.AssassinStat(name)
        shadow_player = Assasin.AssassinStat(name)
    elif choiceHero == 2:
        player = Paladin.PaladinStat(name)
        shadow_player = Paladin.PaladinStat(name)
    elif choiceHero == 3:
        player = Mage.MageStat(name)
        shadow_player = Mage.MageStat(name)
    clear()
    print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("Now you will be attributed a new skill")
    print("Skill have different type, effects, and rarity... ")
    print("The type of a skill change his damage on the enemy; the effect he have can apply bonus on yourself and "
          "penalty on your enemies")
    print("The rarity is the chance to obtain a skill : Common - 50% / Rare - 30% / Super Rare - 15% / Super Super "
          "Rare - 5%")
    print("Your first skill will be either a SR skill or a SSR skill")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
    print("press any key to continue \n")
    key = input()
    rand = (random.randrange(100))
    if rand < 40:
        rand = "SSR"
    else:
        rand = "SR"
    clear()
    player.add_skill(random_skill(player.show_skill_list(), rand))
    shadow_player.skill_list = player.skill_list
    print(f"You got the skill : {player.show_skill_list()[0]['name']}")
    display_skill(player.show_skill_list()[0])
    clear()
    list_p = [player, shadow_player]
    return list_p


def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def space():
    print("\n")


def list_class():
    y = 1

    for i in range(0, len(listdir('Hero_class'))):
        if listdir('Hero_class')[i] != "__init__.py" and listdir('Hero_class')[i] != "__pycache__" and \
                listdir('Hero_class')[i] != "Hero.py":
            x = listdir('Hero_class')[i].split(".")
            print(f"{y} : {x[0]}")
            y = y + 1

    return y


def class_info(choice):
    if choice == 1:
        print("The Assassin is a very good damage dealer that have a chance to inflict critical damage and dodge the "
              "enemy attack")
        print("His default stats are : 80 hp / 25 atk / 45 speed / 70 mana / 30 crit rate / 30 dodge rate")
    if choice == 2:
        print("The Paladin is very versatile and can heal himself during fights")
        print("His default stats are : 130 hp / 17 atk / 35 speed / 120 mana")
    if choice == 3:
        print("The Mage have a good mana reserve and a secret technique to reinforce his normal attack with mana")
        print("His default stats are : 100 hp / 12 atk / 30 speed / 150 mana")


def random_skills(list_skill):
    """
    choose a random skill
    :return: dictionary (of the skill)
    """
    skills = Dictionnary.Skill_dictionnary.skills()

    if len(list_skill) == len(skills) + 1:
        print("You already have all the skills !!")
        return

    valid_skill = False
    while not valid_skill:

        rand = (random.randrange(100))
        if rand < 5:
            rand = "SSR"
        elif 5 <= rand < 20:
            rand = "SR"
        elif 20 <= rand <= 50:
            rand = "R"
        elif rand > 50:
            rand = "C"

        under_skill_list = skills[str(rand)]

        rand2 = (random.randrange(len(under_skill_list)) + 1)
        new_skill = under_skill_list[str(rand2)]

        if not list_skill:
            return new_skill
        true = True
        for i in range(0, len(list_skill)):
            if new_skill == list_skill[i]:
                true = False
        if true:
            valid_skill = True

    return new_skill


def random_skill(list_skill, rand):
    """
    choose a random skill
    :return: dictionary (of the skill)
    """
    y = 0
    skills = Dictionnary.Skill_dictionnary.skills()

    valid_skill = False
    while not valid_skill:

        under_skill_list = skills[str(rand)]

        rand2 = (random.randrange(len(under_skill_list)) + 1)
        new_skill = under_skill_list[str(rand2)]

        if not list_skill:
            return new_skill
        true = True
        for i in range(0, len(list_skill)):
            if new_skill == list_skill[i]:
                true = False
        if true:
            valid_skill = True

    return new_skill


def display_skill(skill):
    print(skill["description"])
    print(f"The rarity of this skill is : {skill['rarity']}")
    print("Press any key to continue \n\n")
    space(), space(), space(), space()
    input()


def xp_up(player, xp, shadow_player):
    print(f"you received {xp} xp ! \n")
    level = player.show_level()
    xp_need = level_list[level]
    player.xp_up(xp)
    if player.show_xp() > xp_need:
        xp_left = abs(xp_need - player.show_xp())
        player.level_up()
        player.xp_up(xp_left)
        stat_level_up(player, shadow_player)
        level = player.show_level()
        xp_need = level_list[level]
        while xp_left > xp_need:
            xp_left = abs(xp_need - xp_left)
            player.level_up()
            player.xp_up(xp_left)
            stat_level_up(player, shadow_player)


def level_display(player):
    level = player.show_level()
    xp_need = level_list[level]
    xp = player.show_xp()
    prc = 0
    if xp != 0:
        prc = 100 * xp / xp_need
    if 10 > prc:
        print(f"XP : ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜ ({player.xp} / {xp_need})")
    elif 20 > prc:
        print(f"XP : 🟦⬜⬜⬜⬜⬜⬜⬜⬜⬜ ({player.xp} / {xp_need})")
    elif 30 > prc:
        print(f"XP : 🟦🟦⬜⬜⬜⬜⬜⬜⬜⬜ ({player.xp} / {xp_need})")
    elif 40 > prc:
        print(f"XP : 🟦🟦🟦⬜⬜⬜⬜⬜⬜⬜ ({player.xp} / {xp_need})")
    elif 50 > prc:
        print(f"XP : 🟦🟦🟦🟦⬜⬜⬜⬜⬜⬜ ({player.xp} / {xp_need})")
    elif 60 > prc:
        print(f"XP : 🟦🟦🟦🟦🟦⬜⬜⬜⬜⬜ ({player.xp} / {xp_need})")
    elif 70 > prc:
        print(f"XP : 🟦🟦🟦🟦🟦🟦⬜⬜⬜⬜ ({player.xp} / {xp_need})")
    elif 80 > prc:
        print(f"XP : 🟦🟦🟦🟦🟦🟦🟦⬜⬜⬜ ({player.xp} / {xp_need})")
    elif 90 > prc:
        print(f"XP : 🟦🟦🟦🟦🟦🟦🟦🟦⬜⬜ ({player.xp} / {xp_need})")
    else:
        print(f"XP : 🟦🟦🟦🟦🟦🟦🟦🟦🟦⬜ ({player.xp} / {xp_need})")


def display_stat(player, shadow_player):
    print("------------------------------------------------------")
    level_display(player)
    print(f"You have : \n {shadow_player.hp} hp left \n {player.atk} atk \n {shadow_player.mana} mana left")
    print(f"Your max hp is : {player.hp}, your max mana is : {player.mana}")
    print("------------------------------------------------------")
    print("Press 1 to consult your skills, 2 to consult your inventory or 0 to go back ")
    space(), space(), space()
    choice = int(input())
    if choice == 1:
        clear()
        display_skills(player)
    if choice == 2:
        clear()
        display_inventory(player)

    else:
        return


def display_inventory(player):
    print("Press 1 to see your potions, 2 to see your items or 0 to go back")
    choice = int(input())
    if choice == 1:
        player.inventory.show_potions()
    if choice == 2:
        player.inventory.show_item()


def potion_add_random(player):
    potion_random = random_potion()
    potion = Item.Item(potion_random['name'], potion_random['type'], potion_random['effect_type'],
                       potion_random['effect'], potion_random['price'], potion_random['duration'],
                       potion_random['description'])
    player.inventory.add_item(potion)


def potion_add(player, name):
    potion_random = return_potion(name)
    potion = Item.Item(potion_random['name'], potion_random['type'], potion_random['effect_type'],
                       potion_random['effect'], potion_random['price'], potion_random['duration'],
                       potion_random['description'])
    player.inventory.add_item(potion)


def display_skills(player):
    for i in range(0, len(player.skill_list)):
        print(f"{i + 1} - {player.skill_list[i]['name']}")
    print("Press a skill number to see his description or 0 to go back")
    space(), space(), space(), space(), space()
    choice = int(input())
    if choice == 0:
        return
    else:
        clear()
        display_skill(player.skill_list[choice - 1])


def stat_level_up(player, shadow_player):
    MessageFunctions.upgrade_stat(player, shadow_player)
    choice = int(input())

    if choice == 1:

        player.hp += 20
        shadow_player.hp = player.hp
        if shadow_player.mana < player.mana - 20:
            shadow_player.mana += 20
        else:
            shadow_player.mana = player.mana

    if choice == 2:

        player.atk += 2
        shadow_player.atk = player.atk
        if shadow_player.mana < player.mana - 20:
            shadow_player.mana += 20
        else:
            shadow_player.mana = player.mana
        if shadow_player.hp < player.hp - 20:
            shadow_player.hp += 20
        else:
            shadow_player.hp = player.hp

    if choice == 3:

        player.mana += 20
        shadow_player.mana = player.mana

        if shadow_player.hp < player.hp - 20:
            shadow_player.hp += 20
        else:
            shadow_player.hp = player.hp


def monster_random(level):
    monsters_list = Dictionnary.Monster_dictionnary.monster_list()
    monster_level = ("Level" + str(level))
    choose = int(random.randrange(4) + 1)

    monsters_choosen = monsters_list[monster_level][str(choose)]

    return monsters_choosen


def monster_fight(level, shadow_player, player):
    fight = True
    MessageFunctions.figth_start()
    monster_dict = monster_random(level)
    monster = Monster_class.Monster.Monster_stat(monster_dict['name'], monster_dict['atk'], monster_dict['hp'],
                                                 monster_dict['mana'], monster_dict['speed'], monster_dict['type'])

    print(f"You have to deal with a {monster.name}")
    print(f"The {monster.name} have {monster.hp} hp, {monster.atk} atk, {monster.mana} mana,"
          f" {monster.speed} speed and is {monster.type} attribute.")

    if monster.speed >= shadow_player.speed:
        print("The monster have a higher speed than you ! He start the fight \n")
        first = "monster"
    else:
        print("You have a higher speed than the monster ! You start the fight \n")
        first = "player"

    while fight:
        if first == "monster":
            dmg_done = monster.damage()
            dmg_taken = shadow_player.dmg_taken(dmg_done)
            shadow_player.hp = shadow_player.hp - dmg_taken
            print(f"You took {dmg_taken} damages. You have {shadow_player.hp} hp left \n")
            first = ""

        choice_done = False
        while not choice_done:
            print(f"What do you want to do ? The  {monster.name}  have  {monster.hp} hp left")
            print(f"You have {shadow_player.hp} hp left and {shadow_player.mana} mana left")
            print("1 : Attack")
            print("2 : skills")
            print("3 : potions")
            print("")
            choice = int(input())

            if choice == 1:
                deg = shadow_player.dmg_done()
                dmg_taken = monster.dmg_taken(deg)
                monster.hp -= dmg_taken

                print(f"You did {deg} damage")
                print(f"The monster have {monster.hp} hp left \n\n")
                choice_done = True

            if choice == 2:
                choice_skill_done = False

                while not choice_skill_done:
                    for i in range(0, len(shadow_player.skill_list)):
                        print(f"{i + 1} - {shadow_player.skill_list[i]['name']}")
                    print("Press a skill number to see his description or 0 to go back \n")
                    choice = int(input())
                    if choice == 0:
                        choice_skill_done = True
                    elif choice - 1 <= len(shadow_player.skill_list) - 1:
                        print(shadow_player.skill_list[choice - 1]["description"])
                        skill = shadow_player.skill_list[choice - 1]
                        print(f"Do you want to use {skill['name']} ?")
                        print("1 : Yes | 2 : No")
                        choice2 = int(input())
                        if choice2 == 1:
                            mana = skill["mana"]
                            if shadow_player.mana >= mana:
                                shadow_player.mana = shadow_player.mana - mana
                                dmg = use_skill(skill, monster.type, shadow_player, monster)
                                monster.hp = int(monster.hp) - dmg
                                print(f"You did {dmg} damages to {monster.name} ")
                                print(f"You used {mana} mana to use this skill")
                                print(f"You now have {shadow_player.mana} mana \n")
                                choice_skill_done = True
                                choice_done = True
                            else:
                                print("You don't have enough mana to use this skill \n")
            if choice == 3:
                player.inventory.show_potions()
                print("Press a potion number to use it or 0 to go back")
                choice = int(input())
                if choice != 0:
                    potion_used = player.inventory.potion_list[choice - 1]
                    player.inventory.use_potion(shadow_player, player, potion_used)

        if monster.hp <= 0:
            print("You killed the monster !")
            xp_dict = Dictionnary.Monster_dictionnary.xp_monster()
            xp_received = xp_dict[str(level)]
            xp_up(player, xp_received, shadow_player)
            skill = class_skill(player.class_name, player.level, player)
            if skill != "none":
                player.add_skill(skill)
                shadow_player.skill_list = player.skill_list

            rand = random.randrange(100)
            print("You got 15 gold !")
            player.money += 15
            if rand > 60:
                potion_add_random(player)
                print("you found a new potion !")
            return True

        dmg_done = monster.damage()
        dmg_taken = shadow_player.dmg_taken(dmg_done)
        shadow_player.hp = shadow_player.hp - dmg_taken
        print(f"You took {dmg_taken} damages. You have {shadow_player.hp} hp left \n")

        if shadow_player.hp <= 0:
            print("You have been killed by the monster")
            return False


def damage(player):
    atk = player.atk
    rand = (random.randrange(40) - 20)
    deg = int((atk * rand / 100) + atk)
    return deg


def use_skill(skill_used, defense_type, shadow_player, monster):
    if skill_used["effect_type"] == "dmg":
        dmg = skill_used["dmg"]
        type = skill_used["type"]

        prc = atribute_advantage(type, defense_type)

        deg = int((dmg * prc / 100) + dmg)

        return deg

    elif skill_used["effect_type"] == "def":
        shadow_player.protection = skill_used["protection"]
        shadow_player.protection_turn = skill_used["duration"]
        return 0

    elif skill_used["effect_type"] == "mix":
        if skill_used["effect"] == "stun":
            monster.receive_effect(skill_used["effect"], 0, skill_used["duration"])
        dmg = skill_used["dmg"]
        type = skill_used["type"]

        prc = atribute_advantage(type, defense_type)

        deg = int((dmg * prc / 100) + dmg)

        return deg

    elif skill_used["effect_type"] == "effect":
        if skill_used["effect"] == "accuracy":
            monster.receive_effect(skill_used["effect"], 0, skill_used["duration"])
            return 0
        elif skill_used["effect"] == "restoration":
            shadow_player.add_buff("restoration", skill_used["heal"], skill_used["duration"])
            return 0
        elif skill_used["effect"] == "atk_buff":
            shadow_player.add_buff("atk_buff", skill_used["buff"], skill_used["duration"])
            return 0
        elif skill_used["effect"] == "poison":
            monster.receive_effect(skill_used["effect"], skill_used["dmg"], skill_used["duration"])
            return 0


def atribute_advantage(atk_type, defense_type):
    if defense_type == "neutral":
        return 0
    types = ["fire", "earth", "lightning", "water"]
    for i in range(0, len(types)):
        if atk_type == types[i]:
            if i == len(types) - 1:
                i_next = types[0]
            else:
                i_next = types[i + 1]
            i_prev = types[i - 1]

            if defense_type == i_prev:
                return -20
            elif defense_type == i_next:
                return 20
            else:
                return 0


def arena_up(actual_arena):
    actual_arena = int(actual_arena) + 1
    actual_arena = str(actual_arena)
    arenas = Dictionnary.arena_names()
    arena = arenas[actual_arena]
    return arena


def find_skill(rarity, name):
    """
    choose a random skill
    :return: dictionary (of the skill)
    """
    skills = Dictionnary.Skill_dictionnary.skills()

    under_skill_list = skills[str(rarity)]

    for i in range(1, len(under_skill_list)):
        skill = under_skill_list[str(i)]

        if skill['name'] == name[1:].replace("'", ""):
            return skill

    return skill


def random_potion():
    potion_list = Dictionnary.Potions.potion()
    choose = str(random.randrange(len(potion_list)) + 1)
    potion_choosen = potion_list[choose]

    return potion_choosen


def return_potion(name):
    potion_list = Dictionnary.Potions.potion()
    for i in range(1, len(potion_list) + 1):
        if potion_list[str(i)]['name'] == name:
            potion_choosen = potion_list[str(i)]

    return potion_choosen


def shop(player):
    potion_list = Dictionnary.Potions.potion()
    cost = potion_list["1"]['price']
    print(cost)
    choiceDone = False
    while not choiceDone:
        print("----------------------------------------------------------------\n"
              "   |        |              WELCOME                 |        |   \n"
              "   |        |                                      |        |   \n"
              "   0        |                                      |        0   \n"
              "            |                                      |            \n"
              "            |                                      |            \n"
              "            |                                      |            \n"
              "            |                                      |            \n"
              "            |                                      |            \n"
              "            |                                      |            \n"
              "------------|--------------------------------------|------------\n"
              "  |     |   0            \TO THE SHOP/             0   |     |  \n"
              "  |     |                                              |     |  \n"
              "  0     |                                              |     0  \n"
              "        |                                              |        \n"
              "        |                                              |        \n"
              "        |___🧪____          ___🧪____          ___🧪____|        \n"
              "        |        |_________|        |_________|        |        \n"
              "        |        |         |        |         |        |        \n"
              "        |________|_________|________|_________|________|        \n"
              f"                                         Balance :{player.money}\n"
              )
        print("This Shop have 3 potions to sell --> \n"
              "1 - 🧪 Force Potion (Augment temporarily your attack)\n"
              "2 - 🧪 Life Potion (Restore a few Hp)\n"
              "3 - 🧪 Mana Potion (Restore a few Mana)")
        print("Which one do you want to buy ? ( press 0 to go back) \n")
        choice = int(input(""))
        if choice == 0:
            choiceDone = True
        if choice == 1:
            print("Do you want to buy a force potion ? (y/n)")
            choice = input()
            if choice == "y":
                if player.inventory.potion_size != 0:
                    if player.money >= cost:
                        potion_add(player, "force potion")
                        print(f"You just bought a Force Potion fo {cost}")
                        player.money -= cost
                        choiceDone = True
                    else:
                        print("You don't have enough gold...")
                        input("press any key to continue \n")
                else:
                    print("You already have too much potion !")

        if choice == 2:
            print("Do you want to buy a Life potion ? (y/n)")
            choice = input()
            if choice == "y":
                if player.inventory.potion_size != 0:
                    if player.money >= cost:
                        potion_add(player, "life potion")
                        player.money -= cost
                        print(f"You just bought a Life Potion fo {cost}")
                        choiceDone = True
                    else:
                        print("You don't have enough gold...")
                        input("press any key to continue \n")
                else:
                    print("You already have too much potion !")

        if choice == 3:
            print("Do you want to buy a Mana potion ? (y/n) ")
            choice = input()
            if choice == "y":
                if player.inventory.potion_size != 0:
                    if player.money >= cost:
                        potion_add(player, "mana potion")
                        print(f"You just bought a Mana Potion fo {cost}")
                        player.money -= cost
                        choiceDone = True
                    else:
                        print("You don't have enough gold...")
                        input("press any key to continue \n")
                else:
                    print("You already have too much potion !")


def class_skill(class_name, level, player):
    list_skill = player.skill_list
    skills = Dictionnary.Skill_dictionnary.skills()

    under_skill_list = skills["class"][class_name]
    if str(level) in under_skill_list:
        skill = under_skill_list[str(level)]
        for i in range(0, len(list_skill)):
            if skill == list_skill[i]:
                return "none"
        print(f"You got a new class skill : {skill['name']} - {skill['description']}")
        return skill
    else:
        return "none"
