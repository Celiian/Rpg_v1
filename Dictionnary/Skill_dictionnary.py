def skills():
    """
    dictionary with all the skills of the game
    :return: dictionary
    """
    types = {
        "C": {
            "1": {
                "name": "Lightning Chain",
                "type": "electric",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "C",
                "dmg": 25,
                "mana": 15,
                "description": "Chain of Lightning is a spell that creates a lightning bolt that passes through the "
                               "enemy, dealing 25 electric damage. The skill cost 15 mana",
            },
            "2": {
                "name": "FireBall",
                "type": "fire",
                "rarity": "C",
                "effect_type": "dmg",
                "effect": "none",
                "dmg": 20,
                "mana": 10,
                "description": "Fireball is a spell that fires a projectile, dealing 20 fire damage. This skill cost "
                               "10 mana",
            },

            "3": {
                "name": "Fire Arrow",
                "type": "fire",
                "rarity": "C",
                "effect_type": "dmg",
                "effect": "none",
                "dmg": 15,
                "mana": 15,
                "description": "Fire Arrow is a spell that send a fire arrow to enemy, dealing 15 fire damage. This "
                               "skill cost 15 mana ",
            },

            "4": {
                "name": "Lightning ring",
                "type": "electric",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "C",
                "dmg": 30,
                "mana": 20,
                "description": "Lightning ring is a spell that create a ring of lightning that surround the enemy"
                               "dealing 30 electric damage. This skill cost 20 mana",
            },
            "5": {
                "name": "Dancing lightning",
                "type": "electric",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "C",
                "dmg": 35,
                "mana": 15,
                "description": "Dancing Lightning is a spell that, when used, causes lightning to strike from the sky "
                               "on the enemy."
                               "This skill deal 35 electric damage and cost 15 mana",
            },
            "6": {
                "name": "Sand Blast",
                "type": "earth",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "C",
                "dmg": 25,
                "mana": 15,
                "description": "Sand Blast is a spell that project a cone of sand and wind towards the enemy, "
                               "dealing 25 earth damage. This skill cost 15 mana",
            },
            "7": {
                "name": "WaterJet",
                "type": "water",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "C",
                "dmg": 25,
                "mana": 15,
                "description": "WaterJet is a spell that project water, dealing 25 water damage. This skill cost 15 "
                               "mana",
            },

        },
        "R": {

            "1": {
                "name": "Fist of Stone",
                "type": "earth",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "R",
                "dmg": 35,
                "mana": 20,
                "description": "Fist of Stone is a spell allow the caster to change his fist into stone before "
                               "hurting the enemy. This skill deal 35 earth damage and cost 20 mana",
            },
            "2": {
                "name": "Water Sword",
                "type": "water",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "R",
                "dmg": 30,
                "mana": 15,
                "description": "Water Sword is a spell that give the caster a water sword for 1 turn, dealing 30 "
                               "water damage. This skill cost 15 mana",
            },
            "3": {
                "name": "Water Shield",
                "type": "water",
                "effect_type": "def",
                "effect": "none",
                "rarity": "R",
                "protection": 20,
                "duration": 3,
                "mana": 20,
                "description": "Water Shield is a spell that reduce the damage taken by 20% for 3 turn. This skill cost "
                               "20 mana",
            },
            "4": {
                "name": "Ice Rain",
                "type": "water",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "R",
                "dmg": 35,
                "mana": 25,
                "description": "Ice Rain is a spell that project ice projectiles which to the sky, dealing 35 water "
                               "damage. This skill cost 25 mana",
            },
            "5": {
                "name": "Mist Spell",
                "type": "water",
                "effect_type": "effect",
                "effect": "accuracy",
                "rarity": "R",
                "mana": 20,
                "description": "Mist Spell is a spell that impact enemies vision, they now have chance to miss their "
                               "attack / skills. This skill cost 20 mana",
            },

        },
        "SR": {
            "1": {
                "name": "Lightning breath",
                "type": "electric",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "SR",
                "dmg": 45,
                "mana": 20,
                "description": "Lightning breath is a spell that exhale a blast of electrically charged air, injuring "
                               "45 electric damage. This skill cost 20 mana",
            },
            "2": {
                "name": "FireStorm",
                "type": "fire",
                "rarity": "SR",
                "effect_type": "dmg",
                "effect": "none",
                "dmg": 55,
                "mana": 40,
                "description": "FireStorm is a spell that create a big storm of fire, dealing 55 fire damage. This "
                               "skill cost 40 mana",
            },
            "3": {
                "name": "Meteorite",
                "type": "earth",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "SR",
                "dmg": 70,
                "mana": 50,
                "description": "The meteorite is a big spell that, when used, "
                               "materializes a large sphere of rock that fall from the sky on the enemy"
                               "This skill deals 70 earth damage and costs 50 mana ",
            },
            "4": {
                "name": "Lightning bolt",
                "type": "electric",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "SR",
                "dmg": 40,
                "mana": 25,
                "description": "Lightning bolt is a spell that send an electric projectile, dealing 40 "
                               "electric damage. This skill cost 25 mana",
            },
            "5": {
                "name": "Earthquake",
                "type": "earth",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "SR",
                "dmg": 45,
                "mana": 25,
                "description": "Earthquake is a spell that unleashed a powerful earthquake to attack the enemy"
                               " This skill deal 45 earth damage and cost 25 mana",
            },
            "6": {
                "name": "Lightning storm",
                "type": "electric",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "SR",
                "dmg": 50,
                "mana": 35,
                "description": "Lightning Storm is a spell that inflict series of lightning strikes in a big storm "
                               "This skill deal 50 electric damage and cost 35 mana",
            },
        },

        "SSR": {
            "1": {
                "name": "Fire Dragon ",
                "type": "fire",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "SSR",
                "dmg": 120,
                "mana": 70,
                "description": "Fire dragon is a big explosive spell, the caster can spit fire like a real dragon,"
                               " dealing 120 fire damage. This skill costs 70 mana",
            },
            "2": {
                "name": "Wall Stone",
                "type": "earth",
                "effect_type": "def",
                "effect": "none",
                "rarity": "SSR",
                "protection": 100,
                "duration": 2,
                "mana": 20,
                "description": "The Wall Stone is a spell that prevent the caster from receiving damage for 2 turn,"
                               "This skill cost 20 mana",
            },
            "3": {
                "name": "Ice Block",
                "type": "water",
                "effect_type": "mix",
                "effect": "stun",
                "rarity": "SSR",
                "duration": 1,
                "dmg": 55,
                "mana": 15,
                "description": "Ice Block is a special spell that stun the enemy for 1 turn and  deal "
                               "55 water damage.This skill cost 45 mana",
            },
            "4": {
                "name": "Golem of Stone ",
                "type": "earth",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "SSR",
                "dmg": 100,
                "mana": 60,
                "description": "Golem of Stone is a large spell that, when activated, materializes a large "
                               "earth-destroying golem that will hit the enemy with an astonish force"
                               "This skill deal 100 earth damage and cost 60 mana",
            },
            "5": {
                "name": "Fire Meteor",
                "type": "fire",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "SSR",
                "dmg": 90,
                "mana": 60,
                "description": "Fire meteor is a spell that causes a meteor rain of fire, "
                               "dealing 90 fire damage. This skill costs 60 mana",
            },
            "6": {
                "name": "Volcano",
                "type": "fire",
                "effect_type": "dmg",
                "effect": "none",
                "rarity": "SSR",
                "dmg": 80,
                "mana": 55,
                "description": "Volcano of Fire is a spell tha materialize as a massive erupting "
                               " volcano, dealing 80 fire damage. This skill costs 55 mana",
            },
        },

        "class": {
            "paladin": {
                "2": {
                    "name": "Heal",
                    "effect_type": "effect",
                    "effect": "restoration",
                    "heal": 20,
                    "mana": 30,
                    "duration": 3,
                    "description": "This skill is exclusive to the paladins and will heal you over time,"
                                   "regenerating 20 hp each turn for 3 turn. This skill costs 30 mana",
                }
            },
            "assassin": {
                "2": {
                    "name": "Poison",
                    "effect_type": "effect",
                    "effect": "poison",
                    "dmg": 15,
                    "mana": 30,
                    "duration": 3,
                    "description": "This skill is exclusive to the assassins and will poison your enemy,"
                                   "dealing him 15 dmg each turn for 3 turn. This skill costs 30 mana"},
            },
            "mage": {
                "2": {
                    "name": "Magic strength",
                    "effect_type": "effect",
                    "effect": "atk_buff",
                    "buff": 15,
                    "mana": 30,
                    "duration": 3,
                    "description": "This skill is exclusive to the mages and will augment your attack,"
                                   "reinforcing it of 15 each turn for 3 turn. This skill costs 30 mana"},
            }
        }
    }
    return types
