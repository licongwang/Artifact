from cards.units.base_hero import BaseHero

# name, color, attack, armor, hp, retaliate, cleave, spell, signature card, base respawn time,
hero_base = [
    ('dummy_hero', 'red', 5, 0, 5, 0, 0, None, None, 2),
]

heroes = {}

for hero_info in hero_base:
    name, color, attack, armor, health, retaliate, cleave, spell, signature_card, base_respawn_time = hero_info
    hero_info = (attack, color, armor, health, spell, retaliate, cleave), signature_card, base_respawn_time
    heroes[name] = BaseHero(hero_info)
