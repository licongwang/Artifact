from cards.units.base_unit import BaseUnit

# name, color, attack, armor, hp, retaliate, cleave, spell
creep_base = [
    ('dummy_creep', None, 1, 0, 1, 0, 0, None),
    ('radiant_creep', None, 2, 0, 4, 0, 0, None),
]

creeps = {}

for creep_info in creep_base:
    name, color, attack, armor, health, retaliate, cleave, spell = creep_info
    creep_info = (attack, color, armor, health, spell, retaliate, cleave)
    creeps[name] = BaseUnit(creep_info)
