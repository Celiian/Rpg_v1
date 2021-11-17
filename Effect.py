import dataclasses


class Effect:
    def __init__(self, effect_type, effect, turn):
        self.effect_type = effect_type
        self.effect = effect
        self.turn = turn
        self.turn_left = turn
