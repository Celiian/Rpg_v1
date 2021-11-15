def monster_list():
    """
    Dictionnary with all monsters of the game classified by level
    :return: dictionary
    """
    monsters_index = {
        "Level1" : {
            "1" : {
                "name": "Skeleton",
                "atk": 12,
                "hp": 80,
                "mana": 60,
                "speed": 25,
                "type" : "neutral",
            },
            "2" : {
                "name": "Glob",
                "atk": 7,
                "hp": 140,
                "mana": 20,
                "speed": 15,
                "type" : "neutral",
            },
            "3": {
                "name": "Wolf",
                "atk": 12,
                "hp": 120,
                "mana": 0,
                "speed": 40,
                "type": "neutral",
            },
            "4": {
                "name": "Goblin",
                "atk": 10,
                "hp": 100,
                "mana": 0,
                "speed": 35,
                "type": "neutral",
            },
        },
        "Level2" : {
            "1" : {
                "name": "Armed Skeleton",
                "atk": 20,
                "hp": 90,
                "mana": 20,
                "speed": 30,
                "type": "neutral",
            },
            "2": {
                "name": "Big Glob",
                "atk": 10,
                "hp": 220,
                "mana": 40,
                "speed": 25,
                "type" : "fire",
            },
            "3": {
                "name": "Lycan",
                "atk": 22,
                "hp": 150,
                "mana": 20,
                "speed": 45,
                "type": "nature",
            },
            "4": {
                "name": "KillerGoblin",
                "atk": 17,
                "hp": 100,
                "mana": 0,
                "speed": 40,
                "type": "neutral",
            },
        }
    }
    return monsters_index

def xp_monster():
    xp_received = {
        "1" : 154,
        "2" : 289,
        "boss" : 500,
    }
    return xp_received