from game.lane import Lane
from basic.hero_define import heroes

class Player(object):
    def __init__(self, player_number, lanes):
        self.player_number = player_number
        self.lanes = lanes
        self.current_cards = []
        self.remained_cards = []
        self.all_cards = []
        self.heroes = []
        self.initialize_heroes()

    def initialize_heroes(self):
        self.heroes = [heroes['dummy_hero']] * 5
        for k, hero in enumerate(self.heroes):
            if k in [0, 1, 2]:
                hero.set_respawn(0)
            if k == 3:
                hero.set_respawn(1)
            else:
                hero.set_respawn(2)

    def take_action(self):
        print('player{} taking turn'.format(self.player_number))
        change_turn = int(input()) > 0
        no_action = int(input()) > 0
        print(change_turn, no_action)
        return change_turn, no_action

    # ==================== player actions ====================
    def deploy_hero(self):
        pass
