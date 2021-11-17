import dataclasses


class InventoryPlayer:

    def __init__(self, item_list=None, potion_list=None):
        if item_list is None:
            item_list = []
        if potion_list is None:
            potion_list = []
        self.item_list = item_list
        self.potion_list = potion_list
        self.item_size = 30
        self.potion_size = 10

    def add_item(self, Item):
        if Item.type == "potion":
            if len(self.potion_list) < self.potion_size:
                self.potion_list.append(Item)
                self.potion_size -= 1
        if Item.type == "item":
            if len(self.item_list) < self.item_size:
                self.item_list.append(Item)
                self.item_size -= 1

    def show_item(self):
        for i in range(0, len(self.item_list)):
            print(self.item_list[i].name)

    def use_potion(self, shadow_player, player, potion):
        if potion.effect_type == "restore_hp":
            shadow_player.hp += potion.effect
            if shadow_player.hp > player.hp:
                shadow_player.hp = player.hp
        if potion.effect_type == "restore_mana":
            shadow_player.mana += potion.effect
        if potion.effect_type == "atk_buff":
            player.add_buff(potion.effect_type, potion.effect, potion.duration)

        self.potion_list.remove(potion)
        self.potion_size += 1

    def show_items(self):
        for i in range(0, len(self.item_list)):
            item = self.item_list[i]
            print(f"You have : {item.name}; {item.description}")

    def show_potions(self):
        if len(self.potion_list) == 0:
            print("You don't have any potion")
        else:
            for i in range(0, len(self.potion_list)):
                potion = self.potion_list[i]
                print(f"{i + 1} : {potion.name} - {potion.description}")