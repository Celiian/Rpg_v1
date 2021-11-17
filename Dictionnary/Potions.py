def potion():
    potion = {
        "1" : {
            "name": "life potion",
            "type": "potion",
            "effect_type": "restore_hp",
            "duration": 0,
            "effect": 40,
            "price": 15,
            "description" : "This potion will restore you 40 hp. (note that you can't have more hp than your maximum "
                            "hp) "
        },
        "2" : {
            "name": "force potion",
            "type": "potion",
            "effect_type": "atk_buff",
            "duration": 3,
            "effect": 10,
            "price": 15,
            "description": "This potion will boost your atk by 10 for 3 turn. (cumulative)"

        },
        "3" : {
            "name": "mana potion",
            "type": "potion",
            "effect_type": "restore_mana",
            "duration": 0,
            "effect": 40,
            "price": 15,
            "description": "This potion will restore you 40 mana. (note that you can have more mana than your maximum "
                           "mana) "
        },

    }
    return potion





















