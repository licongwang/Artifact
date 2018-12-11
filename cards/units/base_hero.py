from cards.units.base_unit import BaseUnit


class BaseHero(BaseUnit):
    def __init__(self, hero_info, is_alive=False):
        unit_info, signature_card, base_respawn_time = hero_info
        super().__init__(unit_info)
        self.weapon = None
        self.armor = None
        self.accessory = None
        self.signature_card = signature_card
        self.base_respawn_time = base_respawn_time
        self.respawn_time = 0

    # ==================== set hero ====================
    def set_respawn(self, respawn_time):
        self.respawn_time = respawn_time

    # ==================== hero actions ====================
    def use_item(self, item_number):
        pass

    # ==================== hero related ====================
    def destory(self):
        super().destory()
        self.set_respawn(self.base_respawn_time)
