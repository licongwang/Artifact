from cards.units.base_hero import BaseHero

hero_base = [
    ('dummy_hero', 5, 0, 5, 0, 0, None, None, 2),    # name, hp, armor, attack, spell, signature card, base respawn time
]

heroes = {}

for hero_info in hero_base:
    name, attack, armor, health, retaliate, cleave, spell, signature_card, base_respawn_time = hero_info
    hero_info = (attack, armor, health, spell, retaliate, cleave), signature_card, base_respawn_time
    heroes[name] = BaseHero(hero_info)
