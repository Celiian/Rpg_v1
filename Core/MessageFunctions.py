import time
from Core import Functions


def game_explain():
    print("Hello player... ")
    print("You just appeared in the tour... it means that's you have to participate in the tour game !")
    print("All you need to do is to climb up the tower by killing monsters one after an other... Sounds easy doesn't "
          "it ?")
    print("But don't worry each 10 levels you will encounter a boss and have to face them !")
    print("May the luck be your side...")


def upgrade_stat(player, shadow_player):
    print("You leveled up !! you're now level " + str(player.show_level()))
    print("Please choose which stat you want to upgrade : ")
    print(f"1 : hp ( max : {player.hp} | left : {shadow_player.hp} )")
    print(f"2 : atk ( {player.atk} )")
    print(f"3 : mana ( max :  {player.mana} | left : {shadow_player.mana} )")
    print()


def display_info(name, stat_hero, level):
    print(f"Actually you are level {level} !")
    print("You have " + str(stat_hero["hp"]) + " hp ")
    print("You have " + str(stat_hero["atk"]) + " atk ")
    print("You have " + str(stat_hero["mana"]) + " mana")
    print()


def arena_enter(name, arena_name):
    print(f"Welcome  in {arena_name}  {name} ")
    print("May the luck be on your side...")
    print()


def arena_end(name):
    print(f"So you did it ! Well played !! {name}")
    print("Now comes a new  challenge...")
    print()


def boss_enter(name):
    print(f"You did it all the way to the boss {name}")
    print("Will you overcome the challenge that's in front of you ? ")
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    time.sleep(0.4)
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    time.sleep(0.4)
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    time.sleep(0.4)
    print("▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓")
    time.sleep(0.4)
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    time.sleep(0.4)
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    time.sleep(0.4)
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    time.sleep(0.4)
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    time.sleep(0.4)
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    time.sleep(0.4)
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("Let's see what can you do...")
    time.sleep(1.5)
    clear()


def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def monster_apparition(monster):
    print("A " + monster + " appear and wants to attack you...")
    print("Get ready to fight !")
    print()


def skills_choose(name, new_skill):
    if new_skill:
        skill_name = new_skill["name"]
        skill_description = new_skill["description"]

        print(f"Congratulation {name} ! You won a new ability !")
        print(f"Your ability is : {skill_name}, {skill_description}")
        print()
    else:
        print("You already have every skills of the game !! Incredible !")


def object_gain(object):
    object_name = object["name"]
    object_description = object["description"]

    print(f"Congratulation ! You got a new object !")
    print(f"Your ability is : {object_name}, {object_description}")
    print()


def menu(arena, player, monster_left):
    print("=============================================")
    print(f"Your current Arena is : {arena['name']}")
    print(f"You need to defeat {monster_left} monsters to go to the next arena")
    print(f"You are currently are level {player.level} and have {player.hp} hp")
    print("1 - Start a fight")
    print("2 - Stats")
    print("3 - Shop")
    print("4 - Save")
    print("5 - Load")
    print("6 - Leave")
    print("=============================================")
    print("\n\n\n")


def figth_start():
    clear()
    print("---------------------------------------------------------")
    print("     -----------------------------------------------     ")
    print("         ---------------------------------------         ")
    print("             -------------------------------             ")
    print("                 ---------------------                   ")
    print("                     -------------                       ")
    print("                         ------                          ")
    print("⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻NEW FIGHT⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻")
    Functions.space(), Functions.space()
