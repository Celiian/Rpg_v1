def items():
    """
    dictionary with all items of the game
    :return: dictionary
    """

    item = {
        "C": {
            "1": {
                "name": "stone helmet",
                "type": "armor",
                "effect_type": "def_buff",
                "buff": 20,
                "price": 15,
                "rarity": "C",
                "description": "The Stone Helmet is a defensive armor that will boost your defense stat by 20 defense."
                               "It cost 20 gold and the rarity of the item is C.",
            },
            "2": {
                "name": "Wood Sword",
                "type": "weapon",
                "effect_type": "atk_buff",
                "buff": 20,
                "price": 10,
                "rarity": "C",
                "description": "The wooden sword is a basic weapon that can help you defend yourself. "
                               "This weapon boosts your attack by 20 attack. It cost 20 gold and the rarity of the"
                               " item is C.",
            },
            "3": {
                "name": "wool vest",
                "type": "armor",
                "effect_type": "def_buff",
                "buff": 10,
                "price": 10,
                "rarity": "C",
                "description": "The woolen jacket is an armor that you wear during the winter. This armor boost your "
                               "defense by 10 defense. It cost 10 gold and the rarity of the item is C.",
            },
            "4": {
                "name": "Stone Axe",
                "type": "weapon",
                "effect_type": "atk_buff",
                "buff": 25,
                "price": 20,
                "rarity": "C",
                "description": "The stone axe is an offensive weapon from prehistoric times. This weapon boosts your "
                               "Attack stat by 25 Attack. It cost 20 gold and the rarity of the item is C.",
            }
        },
        "R": {
            "1": {
                "name": "Bow",
                "type": "weapon",
                "effect_type": "atk_buff",
                "buff": 30,
                "price": 30,
                "rarity": "R",
                "description": "The bow is a weapon where you can shoot arrows at long distances. This weapon costs "
                               "30 gold and the rarity of the item is R.",
            },
            "2": {
                "name": "Sword",
                "type": "weapon",
                "effect_type": "atk_buff",
                "buff": 30,
                "price": 30,
                "rarity": "R",
                "description": "The sword is a hand-to-hand fight weapon. This weapon has the ability to "
                               "boost your attack by 30. This weapon costs 30 gold and the rarity of the item is R.",
            },
            "3": {
                "name": "Coat Mail",
                "type": "armor",
                "effect_type": "def_buff",
                "buff": 40,
                "price": 35,
                "rarity": "R",
                "description": "The coat of mail is a combat armour used by knights. This armor boost your defense "
                               "by 40. This armor cost 35 gold and the rarity of the item is R.",

            },
            "4": {
                "name": "Copper Pant",
                "type": "armor",
                "effect_type": "buff",
                "buff": 35,
                "price": 35,
                "rarity": "R",
                "description": "The copper pants are a very practical armor because it has good protection but also "
                               "you are a little more comfortable on it. This armor boost your defense and speed by 35."
                               "This armor cost 35 gold and the rarity of the item is R",
            },
            "5": {
                "name": "Shield",
                "type": "armor",
                "armor_type": "shield",
                "effect_type": "protection",
                "buff": 40,
                "price": 35,
                "rarity": "R",
                "description": "The shield is a protection used to ward off attacks. This weapon boosts defence by"
                               "40. This armor cost 35 gold and the rarity of the item is R",

            },
            "6": {
                "name": "Magic Mushroom",
                "type": "weapon",
                "effect_type": "mana_buff",
                "restore": 40,
                "price": 35,
                "rarity": "R",
                "description": "The magic mushroom is an item to be consumed to gain 40 mana. To be consumed"
                               " in moderation. This item cost 35 gold and the rarity of the item is R.",
            },
        },
    }
    return item