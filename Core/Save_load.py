from Core import Functions
from Hero_class import Hero, Paladin, Assasin, Mage

def load():
    file = "/Users/celian/PycharmProjects/Projet_rpg_v2/save"
    list_line = []
    with open(file, 'r') as f:
        line = f.readline()
        list_line.append(line)
        for line in line:
            line = f.readline()
            list_line.append(line)
            line = line.split()

    skill_line = []
    skills = []
    for i in range(0, len(list_line)):
        if list_line[i].split(" ")[0] == "player":
            player_info = list_line[i].split(" ")[1].split("-")
        if list_line[i].split(" ")[0] == "arena":
            arena_info = list_line[i].split(" ")[1].split("-")
        if list_line[i].split("-")[0] == "skills":
            skill_line = list_line[i].split("-")[1]

    x = skill_line.replace("[", "")
    x = x.replace("{", "")
    x = x.replace('"', "")
    x = x.replace('}', "")
    x = x.replace(']', "")


    txt = x.split(",")
    dict_skill ={}
    rarity = ""
    y = 1
    y2 = 1
    for i in range(0, len(txt)-1):

        if txt[i].split(":")[0].replace('"', "") == " 'rarity'":
            rarity = txt[i].split(":")[1].replace('"', "")
            rarity = rarity.replace(" ", "")
            rarity = rarity.replace("'", "")
            rarity_dict = 'rarity' + str(y)
            dict_skill.update({rarity_dict: rarity})
            y += 1

        if txt[i].split(":")[0].replace('"', "") == "'name'" or txt[i].split(":")[0].replace('"', "") == " 'name'":
            name_skill = txt[i].split(":")[1].replace('"', "")
            name = "name" + str(y2)
            dict_skill.update({name: name_skill})
            y2 += 1

    len_dict = len(dict_skill) / 2
    for i in range(0, int(len_dict)):
        name = "name" + str(i+1)
        rarity_dict = 'rarity' + str(i+1)
        skills.append(Functions.find_skill(dict_skill[rarity_dict], dict_skill[name]))

    name = ""
    class_name = ""
    atk = 0
    max_hp = 0
    actual_hp = 0
    max_mana = 0
    actual_mana = 0
    speed = 0
    xp = 0
    level = 0
    arena_id = ""
    monster_needed = 0
    monster_kill = 0

    for i in range(0, len(player_info)):
        if player_info[i].split(":")[0] == "name":
            name = player_info[i].split(":")[1]
        if player_info[i].split(":")[0] == "class":
            class_name = player_info[i].split(":")[1]
        if player_info[i].split(":")[0] == "level":
            level = int(player_info[i].split(":")[1])
        if player_info[i].split(":")[0] == "xp":
            xp = int(player_info[i].split(":")[1])

        if player_info[i].split(":")[0] == "speed":
            speed = int(player_info[i].split(":")[1])
        if player_info[i].split(":")[0] == "atk":
            atk = int(player_info[i].split(":")[1])

        if player_info[i].split(":")[0] == "max_hp":
            max_hp = int(player_info[i].split(":")[1])
        if player_info[i].split(":")[0] == "max_mana":
            max_mana = int(player_info[i].split(":")[1])
        if player_info[i].split(":")[0] == "actual_hp":
            actual_hp = int(player_info[i].split(":")[1].split(".")[0])
        if player_info[i].split(":")[0] == "actual_mana":
            actual_mana = int(player_info[i].split(":")[1])

        if class_name == "assassin":
            player = Assasin.AssassinStat(name, atk, max_hp, max_mana, speed, xp, level, skills)
            shadow_player = Assasin.AssassinStat(name, atk, actual_hp, actual_mana, speed, xp, level, skills)
        if class_name == "mage":
            player = Mage.MageStat(name, atk, max_hp, max_mana, speed, xp, level, skills)
            shadow_player = Mage.MageStat(name, atk, actual_hp, actual_mana, speed, xp, level, skills)
        if class_name == "paladin":
            player = Paladin.PaladinStat(name, atk, max_hp, max_mana, speed, xp, level, skills)
            shadow_player = Paladin.PaladinStat(name, atk, actual_hp, actual_mana, speed, xp, level, skills)

    for i in range(0, len(arena_info)-1):
        if arena_info[i].split(":")[0] == "id":
            arena_id = arena_info[i].split(":")[1]
        if arena_info[i].split(":")[0] == "monster_needed":
            monster_needed = arena_info[i].split(":")[1]
        if arena_info[i].split(":")[0] == "monster_kill":
            monster_kill = arena_info[i].split(":")[1]

    dict_info = {
        "player" : player,
        "shadow_player" : shadow_player,
        "actual_arena" : arena_id,
        "monster_needed" : monster_needed,
        "monster_kill" : monster_kill,
    }
    return dict_info


def save(player, shadow_player, arena, actual_arena, monster_kill):
    file = "save"
    with open(file, 'w') as f:
        f.write(f"player name:{player.name}-class:{player.class_name}-level:{player.level}-xp:{player.xp}"
                f"-speed:{player.speed}-atk:{player.atk}-max_hp:{player.hp}-max_mana:{player.mana}"
                f"-actual_hp:{shadow_player.hp}-actual_mana:{shadow_player.mana}")
        f.write("\n")
        f.write(f"skills-{player.skill_list}")
        f.write("\n")
        f.write(f"arena id:{actual_arena}-monster_needed:{int(arena['monster_needed']-monster_kill)}-monster_kill:{monster_kill}")