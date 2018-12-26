class BaseUnit(object):
    def __init__(self, info):
        self.color, self.attack, self.armor, self.health, self.spell, self.retaliate, self.cleave = info
        self.cost = 0
        self.spell = None
        self.attack_direction = None
        self.blocking_unit = None

    # ==================== unit actions ====================
    def cast_spell(self):
        pass

    # ==================== unit related ====================
    def deploy(self):
        pass

    def destory(self):
        pass

    def deal_damage(self):
        pass

    def take_damage(self):
        pass
