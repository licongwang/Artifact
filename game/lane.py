class Lane(object):
    def __init__(self, gc):
        self.gc = gc
        self.crystal = 3
        self.tower_hp = 40
        self.tower_broken = False
        self.improvement = []
        self.player_units = [[0, 0]]
        self.deployment_list = [[], []]

    def add_to_deployment_list(self, player, unit):
        self.deployment_list[player].append(unit)

    def deploy(self):
        self.player_deploy_all(0)
        self.player_deploy_all(1)

    def player_deploy_all(self, player_num):
        self.gc.random.shuffle(self.deployment_list[player_num])
        for unit_to_deploy in self.deployment_list[player_num]:
            possible_index = [i for i in range(len(self.player_units)) if self.player_units[i][player_num] == 0]
            chosen_index = self.gc.random.choice(possible_index)
            self.player_units[chosen_index][player_num] = unit_to_deploy
            if self.player_units[chosen_index][1 - player_num] == -1:
                self.player_units[chosen_index][1 - player_num] = 0
            self.update_possible_slot(player_num)

    def update_possible_slot(self, player_num):
        exist_empty_slot = len([pair for pair in self.player_units if pair[player_num] == 0]) > 0
        exist_unblocked_slot = len([pair for pair in self.player_units if pair[player_num] == -1]) > 0
        new_slot = [0, 0]
        new_slot[1 - player_num] = -1
        if not exist_empty_slot:
            if exist_unblocked_slot:
                for index in range(len(self.player_units)):
                    if self.player_units[index][player_num] == -1:
                        self.player_units[index][player_num] = 0
            else:
                self.player_units.insert(0, new_slot[:])
                self.player_units.insert(len(self.player_units), new_slot[:])
        elif not exist_unblocked_slot:
            insert_index = 0 if self.player_units[0][player_num] != 0 else len(self.player_units)
            self.player_units.insert(insert_index, new_slot[:])

    def battle(self):
        pass

