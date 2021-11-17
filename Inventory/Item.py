import dataclasses

class Item:

    def __init__(self, name, type, effect_type, effect, price, duration, description):
        self.name = name
        self.type = type
        self.effect_type = effect_type
        self.effect = effect
        self.price = price
        self.duration = duration
        self.description = description
