class Lane(object):
    def __init__(self, gc):
        self.gc = gc
        self.crystal = 3
        self.tower_hp = 40
        self.tower_broken = False
        self.improvement = []
        self.player_units = [[-1, 0], [-1, 0]]
        self.deployment_list = [[], []]
        pass

    def add_to_deployment_list(self, player, unit):
        self.deployment_list[player].append(unit)

    def deploy(self):
        self.player_deploy_all(0)
        self.player_deploy_all(1)

    def player_deploy_all(self, player_num):
        self.gc.random.shuffle(self.deployment_list[player_num])
        for unit_to_deploy in self.deployment_list[player_num]:
            units = self.player_units[player_num]
            possible_index = [i for i in range(len(units)) if units[i] == 0]
            chosen_index = self.gc.choice(possible_index)
            self.player_deploy_unit(player_num, unit_to_deploy, chosen_index)

    def player_deploy_unit(self, player_num, unit, position_index):
        self.player_units[player_num][position_index] = unit
        self.update_possible_slot(player_num)

    def update_possible_slot(self, player_num):
        units = self.player_units[player_num]
        if units[1] != 0:
            units.insert(1, 0)
        if units[-1] != 0:
            units += [0]
        self.player_units[player_num] = units


    def battle(self):
        pass
