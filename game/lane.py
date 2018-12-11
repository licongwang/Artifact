class Lane(object):
    def __init__(self, gc):
        self.gc = gc
        self.crystal = 3
        self.tower_hp = 40
        self.tower_broken = False
        self.improvement = []
        self.player_units = [[0], [0]]
        self.deployment_list = [[], []]
        pass

    def add_to_deployment_list(self, player, unit):
        self.deployment_list[player].append(unit)

    def deploy(self):
        self.player_deploy(0)
        self.player_deploy(1)

    def player_deploy(self, player_num):
        self.gc.random.shuffle(self.deployment_list[player_num])
        for unit in self.deployment_list[player_num]:
            self.player_deploy_unit(player_num, unit)

    def player_deploy_unit(self, player_num, unit):
        units = self.player_units[player_num]
        possible_slot = [i for i in range(len(units)) if units[i] == 0]
        chosen_slot = self.gc.choice(possible_slot)
        self.player_units[player_num][possible_slot] = unit
        extended = (possible_slot == 0 or possible_slot == len(self.player_units[player_num]) - 1 and
        self.update_possible_slot()

    def update_possible_slot(self):
        for units in self.player_units:
            if 0 not in units:
                units = [0] + units + [0]

    def battle(self):
        pass
