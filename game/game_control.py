from game.player import Player
from game.lane import Lane
from random import Random
from basic.creep_define import creeps

class GameControl(object):
    def __init__(self, seed):
        self.random = Random(seed)
        self.lanes = [Lane(self), Lane(self), Lane(self)]
        self.players = [Player(0, self.lanes), Player(1, self.lanes)]
        self.current_lane, self.current_player = 0, 0
        self.pass_lane = 0
        self.initialize_game()
        pass

    def initialize_game(self):
        self.hero_deployment()
        self.creep_deployment()
        self.deploy()

    # ==================== game related ====================
    def hero_deployment(self):
        heroes1, heroes2 = [5, 5, 5], [5, 5, 5] #self.get_player_heroes(0)[:3], self.get_player_heroes(1)[:3]
        self.random.shuffle(heroes1)
        self.random.shuffle(heroes2)
        for k in range(len(self.lanes)):
            self.lanes[k].add_to_deployment_list(0, heroes1[k])
            self.lanes[k].add_to_deployment_list(1, heroes2[k])

    def creep_deployment(self):
        radiant_creep = 1 # creeps['radiant_creep']
        position1, position2 = [0, 0, 1, 1, 2, 2], [0, 0, 1, 1, 2, 2]
        self.random.shuffle(position1)
        self.random.shuffle(position2)
        for lane_num in position1[:3]:
            self.lanes[lane_num].add_to_deployment_list(0, radiant_creep)
        for lane_num in position2[:3]:
            self.lanes[lane_num].add_to_deployment_list(1, radiant_creep)

    def deploy(self):
        for lane in self.lanes:
            lane.deploy()

    def initialize_lane(self):
        self.pass_lane = 0
        self.current_player = self.priority_player

    # ==================== player related ====================
    def player_take_action(self):
        player = self.players[self.current_player]
        change_turn, no_action = player.take_action()
        self.update_lane_round(self.current_player, no_action)
        self.current_player = abs(self.current_player - change_turn)

    def update_lane_round(self, player_num, no_action):
        if no_action:
            if self.pass_lane == 0:
                self.priority_player = player_num
            self.pass_lane += 1
        else:
            self.pass_lane = 0

    def purchase_item(self):
        pass

    # ==================== check condition ====================
    def is_lane_finished(self):
        return self.pass_lane == 2

    def is_game_finished(self):
        return False

    # ==================== helper functions ====================
    def get_player_heroes(self, player_num):
        return self.players[player_num].heroes

    # ==================== others ====================
    def run(self):
        def print_lane():
            from cards.units.base_hero import BaseHero
            from cards.units.base_unit import BaseUnit
            for lane in self.lanes:
                units = lane.player_units
                for unit in units:
                    unit = [5 if isinstance(u, BaseHero) else u for u in unit]
                    unit = [1 if isinstance(u, BaseUnit) else u for u in unit]
                    print(unit)
                print()

        while not self.is_game_finished():
            while not self.is_lane_finished():
                print_lane()
                self.player_take_action()
            self.lanes[self.current_lane].battle()
            print('\nlane{} finished\n'.format(self.current_lane))
            self.current_lane = (self.current_lane + 1) % 3
            self.initialize_lane()
            if self.current_lane == 0:
                self.purchase_item()
                self.creep_deployment()




