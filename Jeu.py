import Dictionnary.Arena_dictionnary
from Core import Functions, MessageFunctions, Save_load
from Dictionnary import Arena_dictionnary, Monster_dictionnary, Skill_dictionnary
from Inventory import Item, InventoryPlayer

game = True
loaded = False
if not Functions.file_is_empty('Saves/save'):
    print("Voulez vous charger les données sauvegardés ? (y / n)")
    choice = input()

    if choice == "y":
        dict_info = Save_load.load()
        actual_arena = dict_info["actual_arena"]
        monster_kill = dict_info["monster_kill"]
        player = dict_info["player"]
        shadow_player = dict_info["shadow_player"]
        loaded = True
        skill_atributed = True

if not loaded:
    MessageFunctions.game_explain()
    list_p = Functions.character_create()
    player = list_p[0]
    shadow_player = list_p[1]
    actual_arena = "1"
    monster_kill = 0
    skill_atributed = False

arenas = Dictionnary.Arena_dictionnary.arenas()
arena = arenas[actual_arena]
monster_needed = arena["monster_needed"]
while game:
    monster_killed = False
    Functions.clear()
    monster_left = monster_needed - monster_kill
    MessageFunctions.menu(arena, shadow_player, monster_left)

    choice = input()
    if choice == str(1):
        monster_killed = Functions.monster_fight(arena["monster_level"], shadow_player, player)
    if choice == str(2):
        Functions.clear()
        Functions.display_stat(player, shadow_player)
    if choice == str(3):
        Functions.shop(player)
    if choice == str(4):
        Save_load.save(player, shadow_player, arena, actual_arena, monster_kill)
    if choice == str(5):
        choice2 = input("\n\nDo you want to load the last saved game ? (y / n)\n")
        if choice2 == "y":
            dict_info = Save_load.load()
            actual_arena = dict_info["actual_arena"]
            monster_kill = dict_info["monster_kill"]
            player = dict_info["player"]
            shadow_player = dict_info["shadow_player"]

    if choice == str(6):
        game = False
        Functions.clear()

    if monster_killed:
        monster_kill += 1

    if monster_kill == monster_needed:
        monster_kill = 0
        actual_arena = int(actual_arena) + 1
        actual_arena = str(actual_arena)
        arena = arenas[actual_arena]
        monster_needed = arena["monster_needed"]
        print(f"You entered a new Arena ! : {arena['name']}")
        print("Your hp and mana have been restored !!")
        shadow_player.hp = player.hp
        shadow_player.mana = player.mana
        input("Press any key to continue \n")

    if player.level % 2 == 0 and not skill_atributed:
        player.add_skill(Functions.random_skills(player.show_skill_list()))
        print(f"You got the skill : {player.show_skill_list()[len(player.show_skill_list()) - 1]['name']}")
        Functions.display_skill(player.show_skill_list()[len(player.show_skill_list()) - 1])
        Functions.clear()
        skill_atributed = True
    if player.level % 2 != 0:
        skill_atributed = False

    if shadow_player.mana > player.mana:
        shadow_player.mana = player.mana
    shadow_player.level = player.level
    shadow_player.xp = player.xp
